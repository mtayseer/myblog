Stupid Type Systems - Innecessary Casting in C#
###############################################
:date: 2008-05-13 20:22
:category: Uncategorized
:tags: old blog


If ``List<>`` inherits ``IList<>``, and ``MyIdentity`` inherits
``IIdentity``, then why the heck the C# compiler cannot cast from
``List<MyIdentity>`` to ``IList<IIdentity>``??????
It is the same, the compiler is not smart enough to know this.
So to satisfy the compiler - acting as a good compiler slave - I have to
write this

.. code-block:: csharp

    IList<IIdentity> returnList = new List<IIdentity>(); 
    // A variable name cannot be stupider
    foreach (var item in originalList)
    {
        returnList.Add(item);
    }
    return returnList;

And people were wondering why dynamic languages takes less lines of
code.
