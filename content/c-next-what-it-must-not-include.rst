C#.Next, What it must NOT include?
##################################
:date: 2008-02-12 17:20
:category: Uncategorized
:tags: old blog

There are some talks lately about the next version of C#, and what is
should add. People has gone too far asking for new features, most
notably the `dynamic lookup`_

.. code-block:: csharp

    static void Main(string[] args)
    {    
        dynamic    
        {        
            object myDynamicObject = GetDynamicObject();        
            myDynamicObject.SomeMethod();         
            // call a method           
            myDynamicObject.someString = "value"; 
            // Set a field        
            myDynamicObject[0] = 25;              
            // Access an indexer    
        }
    }

The above looks ridiculous to me. C# is statically-typed language, and
it should stay like this. Trying to add dynamic typing to it - even if
it was optional - is stupid. For me, a language must establish a few
basic concept and stick to them, not try to satisfy every one out there.
C# has incomplete features. These should be completed first before
adding any new features. Take type inference as an example. You cannot
return anonymous types from methods, because you don't know their names.
It should allow something like

.. code-block:: csharp

    public anonymous MyMethod(string email)
    {    
        return from user in Users           
        where user.Email = email           
        select new { FullName = user.FirstName + " " + user.LastName };
    }

It can also add named parameters, and default values for them, just like
Python. It can be supported indirectly now by passing anonymous
types, but complete support for them would be better.
Dynamic languages are not just about dynamic lookup, and supporting
broken dynamic lookup - just like the above mentioned example - is going
to be, really, broken. What about dynamically adding new methods? What
about using making a class as a proxy, say, for a web service? What
about object-specific members - members which exists for a specific
member? It can get very complex, and the only known way to allow dynamic
features is to make your language dynamic.
The beauty of the CLR, is allowing different languages to run and
inter-operate. Unfortunately, it was designed with static typing in
mind, which appears clearly in the BCL design. I wish the DLR team has
these limitations in mind so they address them better, specially the
importance of providing libraries which fits the dynamic languages way
of doing things.
One language is not enough, and one language which tries to fit all
purposes is going to be very complex - just like C++. The solution is
learning different languages and using the appropriate one when it fits,
and integrating them when you need to.

.. _dynamic lookup: http://blogs.msdn.com/charlie/archive/2008/01/25/future-focus.aspx
