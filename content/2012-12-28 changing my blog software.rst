Changing my blog software
=========================

:status: draft
:tags: blog

I've been thinking of moving my blog from Wordpress_ to a blog based on plain-text, for many reasons.

#. I write my thoughts in plain-text files since 2004, when I was still in college working with C++ & Symbian. When I
   created my blog first on CommunityServer then on Wordpress, I was writing my posts in plain-text or MS Word, then
   converting them to HTML. It was more convenient to write them using a simple day-to-day text editor instead of 
   having to open the website editor online & writing what I want, specially that I don't write my posts all at once.

#. With reStructuredText_ & pygments_ I can highlight simply by typing code like this::

    .. code-block:: python
       print "Hello, world"

   And it will be emitted as:

    .. code-block:: python

       print "Hello, world"

How I migrated
--------------

#. Installed Pelican_, and used it to import my old Wordpress content (with some help).
#. Generate a new static blog using my old content.
#. Review the generated blog & you will find errors. Most of the errors I met were in the code blocks.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _ReST: http://docutils.sourceforge.net/rst.html
.. _Pelican: http://docs.getpelican.com/en/latest/
.. _Wordpress: http://wordpress.org/
.. _pygments: http://pygments.org/

