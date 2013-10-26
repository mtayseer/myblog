MIX09 videos
############
:date: 2009-03-25 00:26
:category: Uncategorized
:tags: old blog

MIX conference is my favorite conference. It is always full of
surprises, and it is not restricted to Microsoft technologies. It has
been a habit for me to grab the links to MIX videos since MIX 07, and
I'm keeping this habit for this year too :). Here is the source code to
the Python program which grabs the links. It generates two files:
``mix09_links.txt`` which contain only the links so you can import them
in your favorite text editor, and ``mix09_title.txt`` which contain the
title of every session and its URL, so you know the title of the
session. 

.. code-block:: python

    from urllib import urlopen 
    import re 
    links_file = open('mix09_links.txt', 'w') 
    description_file = open('mix09_title.txt', 'w') 
    try: 
        for i in range(16): 
            url = 'http://videos.visitmix.com/MIX09/page%s' % (i+1) 
            print url # for tracking 
            s = urlopen(url).read() 
            links = re.findall(r'<h2 class="title" title="(.*?)"><a href="/MIX09/(.*?)">.*?</a></h2>', s) 
            for link in links: 
                links_file.write('http://mschannel9.vo.msecnd.net/o9/mix/09/wmv-hq/%s.wmv\\n' % link[1].lower())
                description_file.write('%s\\nhttp://mschannel9.vo.msecnd.net/o9/mix/09/wmv-hq/%s.wmv\\n\\n' % (link[0].lower(), link[1])) 
    finally: 
        links_file.close()
        description_file.close()

and for the lazy person, here are the two files: `mix09_title.txt`_, `mix09_links.txt`_

.. _mix09_title.txt: /static/files/mix09_title.txt
.. _mix09_links.txt: /static/files/mix09_links.txt
