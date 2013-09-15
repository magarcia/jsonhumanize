===============================
jsonhumanize
===============================

.. image:: https://badge.fury.io/py/jsonhumanize.png
    :target: http://badge.fury.io/py/jsonhumanize
    
.. image:: https://travis-ci.org/magarcia/jsonhumanize.png?branch=master
        :target: https://travis-ci.org/magarcia/jsonhumanize

.. image:: https://pypip.in/d/jsonhumanize/badge.png
        :target: https://crate.io/packages/jsonhumanize?version=latest


Convert JSON to human readable HTML

*This is a python version from* `json.human.js
<http://marianoguerra.github.io/json.human.js/>`_

* Free software: MIT license
* Documentation: http://jsonhumanize.rtfd.org.

============
Installation
============

At the command line::

    $ easy_install jsonhumanize

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv jsonhumanize
    $ pip install jsonhumanize

========
Usage
========

To use jsonhumanize in a project::

    import jsonhumanize

To use jsonhumanize from command line::

    $ json-humanize input.json -o output/index.html

    # For more information about command line
    $ json-humanize --help

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/magarcia/jsonhumanize/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

jsonhumanize could always use more documentation, whether as part of the 
official jsonhumanize docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/magarcia/jsonhumanize/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `jsonhumanize` for local development.

1. Fork the `jsonhumanize` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/jsonhumanize.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv jsonhumanize
    $ cd jsonhumanize/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
tests, including testing other Python versions with tox::

    $ flake8 jsonhumanize tests
      $ python setup.py test
    $ tox

  To get flake8 and tox, just pip install them into your virtualenv. 

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, and 3.3, and for PyPy. Check 
   https://travis-ci.org/magarcia/jsonhumanize/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python -m unittest tests.test_jsonhumanize