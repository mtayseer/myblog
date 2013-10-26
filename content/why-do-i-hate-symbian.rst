Why do I hate Symbian?
######################
:date: 2007-03-01 16:42
:category: Uncategorized

*Update*: All the links are dead now. Symbian is dead!

#. **Removed all the good parts of C++**: No exception handling. No
   STL.

#. **Stupid alternatives**:

   #. They removed exception handling, but they added another feature
      called `Leaving`_. It is basically like exception handling, but
      it doesn't unwind the stack!! To get your object deleted, you have
      to put it on something called the *Cleanup Stack* which you have
      to manage manually (This means that we are back to manual new &
      delete).

   #. The data structures they provide is *very* hard to use. Just try
      to use a `linked list`_.

#. **Unnecessary MVC**: The Model-View-Controller is useful for large
   application(e.g. web apps, etc), but it's an overkill for small
   applications. In Symbian, the list box - the most common control - is
   divided into 5 classes, according to their implementation of the
   MVC!!

   #. `CEikListBox`_: The controller
   #. `MListBoxModel`_: The model
   #. `CListBoxView`_: Responsible for drawing the list box area which
      doesn't contain items
   #. `CLisItemDrawer`_: Responsible for drawing the items themselves.
   #. `CListItemData`_: Can you guess what is the role of this one??
      If you are not an experienced Symbian programmer, then your guess
      is wrong. This class is responsible for storing the fonts used for
      drawing items!!!

#. **Premature optimization**: They always favor optimization over
   clarity, even if they want to optimized a *single* instruction or *4
   bytes*. They reference strings using offsets, which means that you
   cannot show them in the debugger *arghhhh*

   This also made them have 6 classes for strings. see
   http://newlc.com/String-and-Descriptors.html

#. **The documentation is not clear**

#. **Deprecating APIs in months**: They deprecate APIs in months, for
   no reasons. Sometimes there is an alternative, sometimes there isn't
   (e.g. Image Conversion Library, Telehpony library, etc)

#. **It's hard to write stable systems**: As I mentioned above, they
   provide Leaving. Unfortunately, they don't use it most of the time.
   What they use most of the time for error reporting is *panics*. Even
   when there is a small error (e.g. invalid index), the program
   panics!! How can you build a stable system if every error will cause
   the program to abort!!

#. **You cannot include more than one table in a single query**: In
   other words, what they say is an RDBMS, is not an RDBMS.

#. **Most of the time, you have to reinvent the wheel**: They don't
   follow standards at all. They keep implementing their own standards.
   First, they didn't support Arabic, so we had to reimplement the
   support ourselves. Later, they added Arabic, but you have to supply
   your fonts in *.gdr* format, not `TTF`_, so we had to port the
   FreeType ourselves. Later, they added support for TTF fonts, but the
   problem is that they you cannot add your own special characters to
   the fonts. On Windows, for example, you can add characters which are
   not valid unicode characters, but as long as the TTF file has them,
   they can be viewed. On Symbian, those characters won't appear.
   Symbian *hardcodes* the validation of the characters. This is why I
   had to reimplement the support for Arabic on Symbian!!!

#. **People use it only to get jobs**: All the people I know who write
   programs for Symbian do this *only* because of the low competition!.

#. **No good support for on-device debugging**: It is there, but it's
   hard to do.

I will be happy to hear more reasons from you to hate Symbian. I hope
this will save some people from this ugly monster.

I have posted about other alternatives `here`_

.. _Leaving: http://newlc.com/LEAVE-and-TRAP.html
.. _linked list: http://www.symbian.com/Developer/techlib/v70sdocs/doc_source/DevGuides/cpp/Base/ArraysAndLists/DoublyLinkedListsOverview.guide.html
.. _CEikListBox: http://www.symbian.com/developer/techlib/v70docs/sdl_v7.0/doc_source/reference/cpp/uikoncorecontrols/class_CEikListBox.html#%3a%3aCEikListBox
.. _MListBoxModel: http://www.symbian.com/developer/techlib/v70docs/sdl_v7.0/doc_source/reference/cpp/uikoncorecontrols/class_MListBoxModel.html#%3a%3aMListBoxModel
.. _CListBoxView: http://www.symbian.com/developer/techlib/v70docs/sdl_v7.0/doc_source/reference/cpp/uikoncorecontrols/class_CListBoxView.html#%3a%3aCListBoxView
.. _CLisItemDrawer: http://www.symbian.com/developer/techlib/v70docs/sdl_v7.0/doc_source/reference/cpp/uikoncorecontrols/class_CListItemDrawer.html#%3a%3aCListItemDrawer
.. _CListItemData: http://www.symbian.com/developer/techlib/v70docs/sdl_v7.0/doc_source/reference/cpp/uikoncorecontrols/class_CListBoxData.html#%3a%3aCListBoxData
.. _TTF: http://en.wikipedia.org/wiki/TrueType
.. _here: /2007/03/04/how-to-solve-symbian-problems/
