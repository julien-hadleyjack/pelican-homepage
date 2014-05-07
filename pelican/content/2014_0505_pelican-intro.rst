Creating a website using Pelican
################################

:date: 2014-05-05 20:34
:tags: python, pelican
:category: Pelican
:slug: creating-website-using-pelican
:author: Julien Hadley Jack



I didn't have many requirements for my own site so using a CMS like Wordpress would have been overkill. I just want to
make information I need for different projects public so that myself or somebody else can easily use it in the future.

Instructions
------------

First of we need python with pip. There are many different ways to achieve that. You can install it afterwards into a
Python version < 3.4, install Python 3.4 (which automatically comes with pip), install
`anaconda <https://store.continuum.io/cshop/anaconda/>`_ or create a virtualenv. Then you have to install pelican (and Markdown if you want to
use it)::

    pip install pelican Markdown

Now we can start with your website. Create a empty folder where the project should live in. Open a command line with
that folder as the workding directory. Start the quickstart and answer to your requirements::

    username@hostname:~/pelican$ pelican-quickstart
    Welcome to pelican-quickstart v3.3.0.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.


    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? Homepage of Julien Hadley Jack
    > Who will be the author of this web site? Julien Hadley Jack
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com (Y/n) n
    > Do you want to enable article pagination? (Y/n)
    > How many articles per page do you want? [10]
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
    > Do you want to upload your website using FTP? (y/N)
    > Do you want to upload your website using SSH? (y/N)
    > Do you want to upload your website using Dropbox? (y/N)
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    Done. Your new project is available at /home/username/pelican

Now lets take a look at what has been created::

    pilosafolivora@vps:~/pelican$ ls -la
    total 36
    drwxrwxr-x 4 username group 4096 May  6 06:14 .
    drwxr-xr-x 8 username group 4096 May  6 06:12 ..
    -rw-rw-r-- 1 username group 3759 May  6 06:14 Makefile
    drwxrwxr-x 2 username group 4096 May  6 06:14 content
    -rwxr-xr-x 1 username group 2179 May  6 06:14 develop_server.sh
    -rw-rw-r-- 1 username group 1481 May  6 06:14 fabfile.py
    drwxrwxr-x 2 username group 4096 May  6 06:14 output
    -rw-rw-r-- 1 username group  826 May  6 06:14 pelicanconf.py
    -rw-rw-r-- 1 username group  529 May  6 06:14 publishconf.py

The blog articles are added to the content folder. Let's start with our first post. Create a file called `first-post.rst`
and then edit the content to this::

    My first post
    #############

    :date: 2014-05-05 20:34
    :tags: hello-world, website
    :category: Pelican
    :slug: first-post
    :author: Julien Hadley Jack

    Hey, this is my first post.

Now run on of the two commands (first one doesn't work on Windows)::

    * make html
    * pelican ./content/ -s pelicanconf.py

You can add a :code:`-r` argument to the second command so that it automatically generates the output if something was
changed in the content folder. The output can be found in the newly created output folder where you can open the
`index.html` file to see the resulting website. The CSS wasn't working for me correctly on Windows. In that case you can
start a local web server by running one of these commands::

    make serve (only Linux)
    python -m SimpleHTTPServer (only Python version < 3)
    python -m http.server  (only Python version > 3)

Visit :code:`http://localhost:8000` to see the website.

Themes
------
For this site I'm using the `cait theme by hdr <https://github.com/hdra/pelican-cait>`_.

Plugins
-------


Versions
--------
* Pelican 3.3.0
* Python 2.7

Used resources
--------------
* `Official Documentation <http://docs.getpelican.com/en/latest/getting_started.html>`_
* http://willdrevo.com/starting-with-pelican.html
* http://algorithmshop.com/20131212-starting-a-blog.html
* http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/
* http://fjavieralba.com/pelican-a-static-blog-generator-for-pythonistas.html