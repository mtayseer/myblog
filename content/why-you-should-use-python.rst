Why you should use Python
#########################
:date: 2007-04-09 04:03
:category: Uncategorized

Dynamic languages are very productive. This is why they are very popular
in the UNIX community, because they form an essential part of their
culture. In the Windows community very few people used them. People
believed that dynamic languages are slow. In 2006, the situation changed
dramatically. I think there are two reasons for this:

#. **Ruby on rails**: Rails was created to optimize programmer's
   *happiness*, thus leading to *much* higher productivity.
#. **C# 3.0**: A lot of the new features in C# 3.0 are inspired by
   dynamic languages like Python.

I will try to explain what makes Python unique. Almost everything I
mention here applies for other dynamic languages as well.

This is not meant to be a Python tutorial. A lot of Python tutorials and
free books are available and easy to find and the syntax is very clear
that you don't need a tutorial to read the examples here.

**Interactive**
You can just launch the interpreter, write code and see the result
immediately. No need for a lengthy compile-run-debug loop, thus reducing
developing time.

**Strongly typed**: Python is

#. Interpreted: It is parsed and executed at runtime.
#. Strongly typed: It *does* type checking.
#. Dynamic: Everything happens at runtime (including type checking).

   For example the following function

   .. code-block:: python

      >>> def add(x, y):
      ...   return x + y

   will work if

   #. ``x`` and ``y`` are of the same type (or compatible type).
   #. This type provides the ``+`` operation.

   If one of the above conditions is broken, Python will raise an exception
   at runtime, stating the exact error.

   .. code-block:: python

    >>> add(3, 5)
    8
    >>> add("hello", " world")
    'hello world'
    >>> add(3, " world")
    Traceback (most recent call last): 
    File "<stdin>", line 1, in ? 
    File "<stdin>", line 2, in add
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

**Readability**
Python is known for its readability. You can learn the syntax of Python
in a day.

.. code-block:: python

    if x in (1, 2, 3, 7, 4): 
      print 'Not found'
    else: 
      print 'found'

**Rich data types**
Python has a lot of data-types built-in, which makes your life a lot
easier. Take a dictionary for example

.. code-block:: python

    >>> d = {'name': 'Bond. James Bond!!', 'car': 'Aston Martin'}

You can use any hashable object as a dictionary key. To access a value
just use

.. code-block:: python

    >>> d['name']
    'Bond, James Bond!!'

For example, how to implement a graph in Python? Very easy, just use a
2D dictionary

.. code-block:: python

    graph = {'A': {'B': 14}, 'B': {'C': 3, 'D': 9}, 'C': None, 'D': None}

which represents this graph

[ImageAttachment]

To get the value of the edge from B-C, use

.. code-block:: python

    >>> graph['B']['C']
    3

This was simple, right?

The story doesn't end here. You have also built-in data structures:
list, tuple, set, etc. Learn how to use them instead of building your
own *inefficient* variants.

**Objects have types, variables don't!!**
As I mentioned before, Python is a strongly typed language, which means
that you cannot treat one type as another. For example

.. code-block:: python

    >>> x = 0
    >>> x.keys()
    Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    AttributeError: 'int' object has no attribute 'keys'

But, you can do the following

.. code-block:: python

    >>> x = 0
    >>> x = {'name': 'Bond, James Bond!!'}

The *variable* x has no type, but the *object* that x points to has a
type. You can change the object that x points to using the assignment
operator. This simple fact may be a little hard to understand at first,
but to clarify it I will show a counter example. In C# you can write

.. code-block:: csharp

    class Base {}
    class Derived : Base{
      public void MyMethod() {}
    }

    Base b = new Derived();
    b.MethodCall();

This will not work because the *reference* b is of type Base, though the
*object* itself has this method. You have to rewrite the last line to
become

.. code-block:: csharp

    ((Derived)b).MethodCall();

OK, how this can be useful? How many times you used 2 variables to point
to the same piece of information? Like

.. code-block:: csharp

    string personIdString = context.Request.Params["personId"];
    int personId = int.Parse(personIdString);

In Python, this can be written as

.. code-block:: python

    personId = context.Request.Params['personId']personId = int(personId)

**Returning multiple values**
This is a stupid problem: If you want to return more than one value, you have to use out parameters.

Python solves this by using *tuples*. Tuples are simply constant lists,
so how can we use them?

.. code-block:: python

    def return_many_values():  
      return (1, 2, 4, 8)

The above function returns a single object: The tuple object. The caller
can unpack the tuple using this

.. code-block:: python

    (a, b, c, d) = return_many_values()

After executing the last statement a = 1, b = 2, c = 4, d = 8.

Because this is a very common idiom, you can ignore the braces.

.. code-block:: python

    def return_many_values():  
      return 1, 2, 4, 8
    a, b, c, d = return_many_values()

**Keyword arguments**
 Don't you wish that you can pass parameters by name? Something like

.. code-block:: python

    Factorial(x=10)

#. It is much easier to read code: No need to search on MSDN to know
   what the parameters mean.
#. Much less errors: You remember the parameters by name, not by order.
#. The parameters can have default values, so you can send only the
   needed parameters.
#. They can be send out-of-order: CreateWindow(x=0, y=10) is the same as
   CreateWindow(y=10, x=0)

**Batteries included**
An essential part of Python's philosophy is the *'Battaries
included'*\ concept: The default installation should provide most of the
libraries need for common tasks: Threading, Mail (SMTP, IMAP, POP3),
Regex, GUI, Complex numbers, compression (Tar, Zip, …) and a lot of
other useful libraries.

**Not limited**
If you are a Java programmer, you have suffered difficulties using
platform-specific features, for example COM components. It is an
essential part of Python culture that the programmers are consenting
adults: they know what they should do, so the language must help them
doing what they want. This is why Python is not isolated from the
platform. For example, you have

#. CPython: The default Python implementation, written in C.
#. Jython: Implementation on top of JVM.
#. IronPython: Implementation on top of CLR.
#. win32all: A library for CPython to use Win32 APIs & COM components.
#. Carbon: MacOS X specific APIs.

You can write cross-platform code in Python, but you can also write
platform-specific components for best use of your platform.

**Everything is an object**
Classes are objects. Functions are objects. This makes your life easier for 2 reasons

#. You can add members at runtime:
#. You can add members to an *existing class*\ : and all *new* instances
   will have this member.
#. You can add members to an *existing object*\ : and this member will
   be specific to this object. This can be useful in GUI applications if
   you want to attach a data item to an existing widget.
#. You can *add members to a function*\ : I will explain how to use this
   in a minute how to do this.
#. You can change objects at runtime: I will explain this with an example.

You are required to implement the factorial function with caching. If
you are doing it in C#, it will look like

.. code-block:: csharp

    public class AdvancedMath{  
      static SortedDictionary<int, int> _cache = new SortedDictionary<int, int>();
      static int Factorial(int x)  {
        if (_cache.ContainsKey(x))
          return _cache[x];
        if (x == 0)
          return 1;
        int result = x * Factorial(x - 1);    
        _cache.Add(x, result);    
        return result;  
      }
    }

What is wrong with this code?

#. It couples the caching to the calculation.
#. The cache contains all intermediate values: This can be good or bad,
   depending on your usage.
#. Factorial(100) = 0. *Overflow*.

We can solve the first problem by separating the caching & the
calculation into 2 different functions

.. code-block:: csharp

    static SortedDictionary<int, int> _cache = new SortedDictionary<int, int>();
    static int Factorial(int x)
    {
      return Caching(x, _FactorialImpl);
    }
      
    delegate int MathDelegate(int x);
    static int Caching(int x, MathDelegate mathDelegate)
    {
      if (_cache.ContainsKey(x))
        return _cache[x];
      int result = mathDelegate(x);
      _cache.Add(x, result);
      return result;
    }
      
    static int _FactorialImpl(int x)
    {
      if (x == 0)
        return 1;
      return x * _FactorialImpl(x - 1);
    }

This solves the first 2 problems, but not the third. Besides, the
Caching() function is not generic enough: It handles only integers! Of
course, you can use objects instead of integers, but how can you cache
functions with more than 1 parameter! I will be happy if you send me the
generic solution in C#, but I like the generic solution in Python

.. code-block:: python

    # This function takes any function as a parameter & returns an 
    # equivalent function, but with caching
    def cached(old_fn):  
      def new_fn(*args):# *args means that it can accept any
                        # number of arguments. They will                    
                        # be contained in the tuple `args`    
        if new_fn.cache.has_key(args):      
          return new_fn.cache[args]    
        result = old_fn(*args)  # We are passing all the                           
                                # arguments to the original                           
                                # function. If the number of                           
                                # arguments is not correct,                           
                                # it will throw an exception    
        new_fn.cache[args] = result    
        return result  
      new_fn.cache = {} # the cache is a member of the                     
                        # function itself  
      return new_fn

      def factorial(n):  
        if n == 0:    
          return 1  
        return n * factorial(n - 1)

      factorial = cached(factorial)

Python solution has many advantages over the C# solution

#. The caching is decoupled from the calculation.
#. The caching contains only final values.
#. The cache is not coupled to the function itself and we are not using
   a global cache, which is a cleaner design.
#. factorial(100) =
   93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L.
   This is due to the fact that an integer *recognizes an overflow*
   (because it is an object, not just stupid 4 bytes) and converts
   itself to a long, which can represent large numbers.

#. It can handle any number of arguments.

**The power of introspection**
You can call a function at runtime by its name. This allows us to call
yet undefined functions. I will illustrate this with an example.

This is the standard C# idiom for SAX parsing of an XML document

.. code-block:: csharp

    try{  
      XmlTextReader rdr = new XmlTextReader();  
      rdr.WhitespaceHandling = WhitespaceHandling.None;  
      while(rdr.Read())  
      {    
        switch (rdr.Name)    
        {      
          case "scoresheet":      
            if (rdr.IsStartElement())      
            {      
              // handle element start      
            }      
            else      
            {      
              // handle element end      
            }      
            break;      
          // handle other cases here      
          default:      
          // handle 'unexpected element' error    
          }  
        }
      }
      catch (XmlException ex)
      {  
        // handle error
      }

You have to write a huge switch statement with a lot of nesting to read
a complex XML document, or you can modify it a little bit to forward to
an observer class.

The problem with this design is inflexibility: you have to maintain the
mapping yourself within the switch statement. With Python, you can make
a more extensible solution

This is the main driver

.. code-block:: python

    from xml.sax import parse as sax_parser
    parser = MySaxParser()
    sax_parse(file_name, parser)

The parser will be something like

.. code-block:: python

    # This is the base class that you will inherit
    class BaseSaxHandler(xml.sax.handler.ContentHandler):
      def startElement(self, tag, attributes):
        tag = str(tag) # convert unicode -> str
        
        # get a method in this object named 'start_' + tag, or
        # return None if the method doesn't exist
        handler = getattr(self, 'start_' + tag.lower(), None)
        if handler:
          handler(attributes)
        else:
          self.error_unknow_start_tag(tag, attributes)
        
      def endElement(self, tag):
        tag = str(tag)
        handler = getattr(self, 'end_' + tag.lower(), None)
        if handler:
          handler()
        else:
          self.error_unknown_end_tag(tag)

      def error_unknown_start_tag(self, tag, attributes):
        print 'Unknown start tag:', tag

      def error_unknown_end_tag(self, tag):
        print 'Unknown end tag:', tag

    class MySaxParser(BaseSaxHandler):
      def start_channel(self, attributes):
        # Look Ma, no switch  
        print '<channel>'

      def end_channel(self):
        print '</channel>'

What are the benefits?

#. No need to repeat the switch statement.
#. Isolated error handling.
#. Extensions are easy to do: You can make MySaxParserV2 which inherits
   MySaxParser and add/override methods to handle new/existing tags.

Intropection can make your life easier when implementing proxies and web
services. I suggest you read the book `Dive Into Python`_ for more
in-depth explanation.

**Used by the most successul sites**

#. `Google`_
#. Industrial Light & Magic: Makers of 'Star Wars' movies.
#. `YouTube.com`_
#. `Reddit.com`_: One of the most popular social bookmarking sites.
#. `YouOs.com`_: Online OS.
#. `And many others`_

**References**

-  `Python download link`_. I suggest using version 2.4.
-  `Dive Into Python`_: For programmers who want to learn Python
-  `Fredrik Lundh's articles`_
-  `Python cookbook`_
-  `Django`_: There are a lot of Python web frameworks, but this is the best one.
-  Join the `Python mailing list`_

.. _Dive Into Python: http://www.diveintopython.org/
.. _Google: http://www.google.com/
.. _YouTube.com: http://www.youtube.com/
.. _Reddit.com: http://www.reddit.com/
.. _YouOs.com: http://www.youos.com/
.. _And many others: http://www.python.org/about/success/
.. _Python download link: http://www.python.org/download/
.. _Fredrik Lundh's articles: http://www.effbot.org/zone/index.htm
.. _Python cookbook: http://www.activestate.com/ASPN/Python/Cookbook/
.. _Django: http://www.djangoproject.com/
.. _Python mailing list: http://mail.python.org/mailman/listinfo/python-list
