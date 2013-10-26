How to solve Symbian problems?
##############################
:date: 2007-03-04 14:24
:category: Uncategorized

In a previous post, I mentioned a lot of reasons why I hate Symbian, but
not everyone has the choice of choosing which OS to work on. In this
post I will try to mention what are the available solutions to this
(according to my own experience).

#. **J2ME**: J2ME is available on all Smart Phones. It is the most
   widely used environment for writing mobile software. Unfortunately,
   it has a lot of limitations. You cannot write C++ extensions easily
   with it & a lot of the functionality is dependent on the device
   itself. Most of these limitations are removed from newer phones (e.g.
   Now you can access the file system of your phones), but if you want
   to write programs for older phones, you are stuck 

2. **Python**: Python is available for S60 phones only. The biggest
   advantage is that you can extend it using C++, but it is not
   available on other Symbian phones.

3. **Flash**: You can use Macromedia Flash to write Symbian programs.
   It also has some limitations; the most important is not being
   extensible easily with C++. The limitations are much less than J2ME
   limitations, though. I didn’t use it myself so I don’t know more
   about it. I think it’s available on S60 phones only. 

4. **OPL**: A Basic-like language, which was created in mid-80s. It’s
   available now as an Open Source Software, but its development is very
   slow.

5. **AppForge**: They provided VB6 & .net environments for Symbian,
   Palm, BlackBerry, etc. I didn’t use this myself so I cannot make a
   decision about it.

6. **Write your own libraries in C++**: Don’t ever think you can
   extend Symbian libraries. They say that it’s very flexible &
   extensible, but to extend anything you need more than just
   object-orientation or design patterns. *You need to understand how it
   works*.

A colleague of mine tried to extend the default List Box to provide an
easy, flexible & portable version of it. He spent more than 4 months
trying to do so. He wrote it, but it was unstable – it panicked at
random times.

The above mentioned solutions are the most popular solutions. You may
find less popular tools to solve this problem.

So write your own widgets. Use your own data structures. Your programs
will be much cleaner, easier to understand & port to other platforms.

I know you cannot replace everything. There are times that you have to
use Symbian APIs, but try to reduce this to a minimum if you want to get
something done.

