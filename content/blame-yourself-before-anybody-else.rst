Blame yourself before anybody else
##################################
:date: 2007-08-21 18:25
:category: Uncategorized
:tags: old blog

Here at Silverkey, we use LLBLGen Pro as our ORM. One of the nicest
features of it is prefetching related entities, so if you have a
"CompanyEntity", you can tell it to fetch all related "Employee Entity".
This makes our jobs easier, except when it doesn't!!!
Today I had a few bugs with LLBL: Trying to save an entity threw
NullReferenceException deeply from inside LLBL code. Even though it
worked in some circumstances, it didn't work on others. It was easy to
blame LLBL, since it was the source of the exception. So instead of
letting LLBL load the related entities, I loaded them myself.
This worked OK for sometime, but it started to through the same
exception again. So it really appeard that the problem was not what I
thought.
First, I recognized two things

#. It happens in with a certain class, so this class was the source of
   the problem
#. It happens only when I changed the objects. If I didn't change them,
   it works OK.

The code for saving was like this

.. code-block:: csharp

    using (Transaction transaction = new Transaction(System.Data.IsolationLevel.ReadUncommitted, "SaveCompany"))
    {
        try
        {
            // Save related entities
            foreach (Employee employee in CompanyEmployees)
            {
                employee.Transaction = transaction;
                employee.Save();
            }

            // Save modified fields
            _entity.Transaction = transaction;
            _entity.Save();

            transaction.Commit();
        }
        catch
        {
            transaction.Rollback();
            throw;
        }
     }

Trying to access any member of the entity now will throw a `NullReferenceException`. Though the entity is not null, it will try to
connect to the database using the connection *of the closed transaction*, which will throw the NullReferenceException.
It should be like this

.. code-block:: csharp

    using (Transaction transaction = new Transaction(System.Data.IsolationLevel.ReadUncommitted, "SaveCompany"))
    {
        try
        {
            // Save related entities
            foreach (Employee employee in CompanyEmployees)
            {
                employee.Transaction = transaction;
                employee.Save();
            }

            // Save modified fields
            _entity.Transaction = transaction;
            _entity.Save();

            transaction.Commit();
        }
        catch
        {
            transaction.Rollback();
            throw;
        }
        finally
        {
            _entity.Transaction = null;
        }
     }

The lessons learnt: *It's easy to blame the tools you use, but probably it is your fault*


