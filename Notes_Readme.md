04_05_2021 bis
-------------------
I am following instructions from:
Python Tutorial - Projects Made Easy: Part #2 Adding Documentation with nbdev
From <https://www.youtube.com/watch?v=n7lMmyam9Zk> 

Your site is published at https://cailleauthierry.github.io/tcai_mages/ > Error 404 (you must provide an index.html file.)

PS C:\Users\tcailleau\Documents\Python\tcai_mages> nbdev_build_docs
converting: C:\Users\tcailleau\Documents\Python\tcai_mages\00_core.ipynb
converting: C:\Users\tcailleau\Documents\Python\tcai_mages\01_game.ipynb
converting: C:\Users\tcailleau\Documents\Python\tcai_mages\index.ipynb
Warning: Some of your Notebooks use the same title (['module name here', 'module name here']).
converting C:\Users\tcailleau\Documents\Python\tcai_mages\index.ipynb to README.md
PS C:\Users\tcailleau\Documents\Python\tcai_mages>

This creates a \docs\index.html

That worked! I get (copy/paste of the text omly of the generate page):

 tcai_mages
 Nav
github
tcai_mages
Overview
module name here
Project name here
Summary description here.
Install
How to use
This file will become your README and also the index of your documentation.

Install
pip install your_project_name

How to use
Fill me in please! Don't forget code examples:

1+1
2


View docs locally
If you want to look at your docs locally before you push to Github, you can do so by running a jekyll server. First, install Jekyll by following these steps. Then, install the modules needed for serving nbdev docs by cding to the docs directory, and typing **bundle install**. Finally, cd back to your repo root and type make docs_serve. This will launch a server on port 4000 (by default) which you can connect to with your browser to view your docs.

If Github pages fails to build your docs, running locally with Jekyll is the easiest way to find out what the problem is.

Followed:

https://jekyllrb.com/docs/installation/windows/ > rubyinstaller-devkit-2.7.2-1-x64.exe > all defaults

Done installing documentation for bundler after 5 seconds
27 gems installed

C:\Users\tcailleau>jekyll -v
jekyll 4.2.0

C:\Users\tcailleau>

To get vscode to start in the default path of the project, best use cmd/exe promt (instead of PS) it also works for python

C:\Users\tcailleau\Documents\Python\tcai_mages\docs>bundle install
Fetching gem metadata from https://rubygems.org/..........
Fetching gem metadata from https://rubygems.org/.
Resolving dependencies...
Fetching concurrent-ruby 1.1.7
Installing concurrent-ruby 1.1.7

[...]
Installing github-pages 209

Bundle complete! 5 Gemfile dependencies, 92 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
Post-install message from dnsruby:
Installing dnsruby...
  For issues and source code: https://github.com/alexdalitz/dnsruby
  For general discussion (please tell us how you use dnsruby): https://groups.google.com/forum/#!forum/dnsruby
Post-install message from sass:

Ruby Sass has reached end-of-life and should no longer be used.

* If you use Sass as a command-line tool, we recommend using Dart Sass, the new
  primary implementation: https://sass-lang.com/install

* If you use Sass as a plug-in for a Ruby web framework, we recommend using the
  sassc gem: https://github.com/sass/sassc-ruby#readme

* For more details, please refer to the Sass blog:
  https://sass-lang.com/blog/posts/7828841


PS C:\Users\tcailleau\Documents\WindowsPowerShell\Scripts> choco install make
Chocolatey v0.10.15
Installing the following packages:
make
By installing you accept licenses for the packages.
Progress: Downloading make 4.3... 100%

make v4.3 [Approved]
make package files install completed. Performing other installation steps.
 ShimGen has successfully created a shim for make.exe
 The install of make was successful.
  Software install location not explicitly set, could be in package or
  default install location if installer.

Chocolatey installed 1/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
PS C:\Users\tcailleau\Documents\WindowsPowerShell\Scripts>

PS C:\Users\tcailleau\Documents\Python\tcai_mages> make docs_serve
cd docs && bundle exec jekyll serve
Configuration file: C:/Users/tcailleau/Documents/Python/tcai_mages/docs/_config.yml
            Source: C:/Users/tcailleau/Documents/Python/tcai_mages/docs
       Destination: C:/Users/tcailleau/Documents/Python/tcai_mages/docs/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
      Remote Theme: Using theme fastai/nbdev-jekyll-theme
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                    done in 0.868 seconds.
  Please add the following to your Gemfile to avoid polling for changes:
    gem 'wdm', '>= 0.1.0' if Gem.win_platform?
 Auto-regeneration: enabled for 'C:/Users/tcailleau/Documents/Python/tcai_mages/docs'
    Server address: http://127.0.0.1:4000/tcai_mages//

The local URL "http://127.0.0.1:4000/tcai_mages//" does disaply the website!
04_05_2021
-------------------
Redoing everything from scratch to get the doc

PS C:\Users\tcailleau\Documents\Python\tcai_mages> pip install -e .
Obtaining file:///C:/Users/tcailleau/Documents/Python/tcai_mages
Installing collected packages: tcai-mages
  Running setup.py develop for tcai-mages
Successfully installed tcai-mages
PS C:\Users\tcailleau\Documents\Python\tcai_mages> 

C:\Users\tcailleau\Documents\Python\tcai_mages>jekyll -v
jekyll 4.2.0

C:\Users\tcailleau\Documents\Python\tcai_mages>cd docs



Post-install message from html-pipeline:
-------------------------------------------------
Thank you for installing html-pipeline!
You must bundle Filter gem dependencies.
See html-pipeline README.md for more details.
https://github.com/jch/html-pipeline#dependencies
-------------------------------------------------

C:\Users\tcailleau\Documents\Python\tcai_mages\docs>
04_04_2021
------------------

'from nbdev.export import notebook2script; notebook2script()' runningin the last cell of the notebook is equivalent to rung 'nbdev_build_lib' from the CLI

[13]


from nbdev.export import notebook2script; notebook2script()
Converted 00_core.ipynb.
Converted index.ipynb.

PS C:\Users\tcailleau\Documents\Python\tcai-mages> pip install -e .
Obtaining file:///C:/Users/tcailleau/Documents/Python/tcai-mages
Installing collected packages: tcail-mages
  Running setup.py develop for tcail-mages
Successfully installed tcail-mages
PS C:\Users\tcailleau\Documents\Python\tcai-mages> 
Next 
------------------

Next will be about following the 2nd video about documentation
Python Tutorial - Projects Made Easy: Part #2 Adding Documentation with nbdev

04_03_2021
-------------
I am following instructions from:
Part #1 Getting Started with nbdev

From <https://www.youtube.com/watch?v=r4RuVI-r5ZI> 

I'm not sure I'm getting all the steps right, but I got to the same point than the video but on my PC with github desktop to clone the project instead of "Codespaces"

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

Transcript started, output file is C:\Users\tcailleau\Documents\WindowsPowerShell\PSTranscript\PSTranscript4_3_2021.txt
Date: 4/3/2021
Time: 12:46 AM
Loading personal and system profiles took 1180ms.
PS C:\Users\tcailleau\Documents\WindowsPowerShell\Scripts> & C:/Users/tcailleau/AppData/Local/Programs/Python/Python39/python.exe c:\Users\tcailleau\.vscode\extensions\ms-python.python-2021.3.680753044\pythonFiles\pyvsc-run-isolated.py c:\Users\tcailleau\.vscode\extensions\ms-python.python-2021.3.680753044\pythonFiles\shell_exec.py C:/Users/tcailleau/AppData/Local/Programs/Python/Python39/python.exe c:\Users\tcailleau\.vscode\extensions\ms-python.python-2021.3.680753044\pythonFiles\pyvsc-run-isolated.py pip install -U ipykernel --user C:/Users/TCAILL~1/AppData/Local/Temp/tmp-22824DFE52J5hyGr6.log
Executing command in shell >> C:/Users/tcailleau/AppData/Local/Programs/Python/Python39/python.exe c:\Users\tcailleau\.vscode\extensions\ms-python.python-2021.3.680753044\pythonFiles\pyvsc-run-isolated.py pip install 
-U ipykernel --user
Collecting ipykernel
  Downloading ipykernel-5.5.3-py3-none-any.whl (120 kB)
     |████████████████████████████████| 120 kB 6.4 MB/s
Collecting jupyter-client
  Downloading jupyter_client-6.1.12-py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 6.8 MB/s
Collecting tornado>=4.2
  Downloading tornado-6.1-cp39-cp39-win_amd64.whl (422 kB)
     |████████████████████████████████| 422 kB ...
Collecting ipython>=5.0.0
  Downloading ipython-7.22.0-py3-none-any.whl (785 kB)
     |████████████████████████████████| 785 kB ...
Collecting traitlets>=4.1.0
  Downloading traitlets-5.0.5-py3-none-any.whl (100 kB)
     |████████████████████████████████| 100 kB 2.9 MB/s
Requirement already satisfied: colorama in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel) (0.4.4)
Requirement already satisfied: setuptools>=18.5 in c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages (from ipython>=5.0.0->ipykernel) (49.2.1)
Collecting decorator
  Downloading decorator-5.0.3-py3-none-any.whl (8.6 kB)
Collecting jedi>=0.16
  Downloading jedi-0.18.0-py2.py3-none-any.whl (1.4 MB)
     |████████████████████████████████| 1.4 MB 6.4 MB/s
Collecting backcall
  Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting pickleshare
  Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting pygments
  Downloading Pygments-2.8.1-py3-none-any.whl (983 kB)
     |████████████████████████████████| 983 kB 6.8 MB/s
Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0
  Downloading prompt_toolkit-3.0.18-py3-none-any.whl (367 kB)
     |████████████████████████████████| 367 kB 6.4 MB/s
Collecting parso<0.9.0,>=0.8.0
  Downloading parso-0.8.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 1.2 MB/s
Collecting wcwidth
  Downloading wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting ipython-genutils
  Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting pyzmq>=13
  Downloading pyzmq-22.0.3-cp39-cp39-win_amd64.whl (1.2 MB)
     |████████████████████████████████| 1.2 MB 6.4 MB/s
Collecting python-dateutil>=2.1
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 6.4 MB/s
Collecting jupyter-core>=4.6.0
  Downloading jupyter_core-4.7.1-py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 5.8 MB/s
Collecting pywin32>=1.0
  Downloading pywin32-300-cp39-cp39-win_amd64.whl (9.2 MB)
Requirement already satisfied: six>=1.5 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from python-dateutil>=2.1->jupyter-client->ipykernel) (1.15.0)
Installing collected packages: ipython-genutils, wcwidth, traitlets, pywin32, parso, tornado, pyzmq, python-dateutil, pygments, prompt-toolkit, pickleshare, jupyter-core, jedi, decorator, backcall, jupyter-client, ipython, ipykernel
  WARNING: The script pygmentize.exe is installed in 'C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-migrate.exe, jupyter-troubleshoot.exe and jupyter.exe are installed in 'C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-kernel.exe, jupyter-kernelspec.exe and jupyter-run.exe are installed in 'C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  WARNING: The scripts iptest.exe, iptest3.exe, ipython.exe and ipython3.exe are installed in 'C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed backcall-0.2.0 decorator-5.0.3 ipykernel-5.5.3 ipython-7.22.0 ipython-genutils-0.2.0 jedi-0.18.0 jupyter-client-6.1.12 jupyter-core-4.7.1 parso-0.8.2 pickleshare-0.7.5 prompt-toolkit-3.0.18 pygments-2.8.1 python-dateutil-2.8.1 pywin32-300 pyzmq-22.0.3 tornado-6.1 traitlets-5.0.5 wcwidth-0.2.5
PS C:\Users\tcailleau\Documents\WindowsPowerShell\Scripts> nbdev_buuiild_lib
nbdev_buuiild_lib : The term 'nbdev_buuiild_lib' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path  
is correct and try again.
At line:1 char:1
    + CategoryInfo          : ObjectNotFound: (nbdev_buuiild_lib:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\tcailleau\Documents\WindowsPowerShell\Scripts> nbdev_build_lib
nbdev_build_lib : The term 'nbdev_build_lib' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is   
correct and try again.
At line:1 char:1
+ nbdev_build_lib
+ ~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (nbdev_build_lib:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\tcailleau\Documents\WindowsPowerShell\Scripts> cd C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts
PS C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts> pip install -U nbdev
Collecting nbdev
  Downloading nbdev-1.1.13-py3-none-any.whl (46 kB)
     |████████████████████████████████| 46 kB 1.8 MB/s
Collecting nbformat>=4.4.0
  Downloading nbformat-5.1.3-py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB ...
Collecting pyyaml
  Downloading PyYAML-5.4.1-cp39-cp39-win_amd64.whl (213 kB)
     |████████████████████████████████| 213 kB ...
Collecting fastcore>=1.3.19
  Downloading fastcore-1.3.19-py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 587 kB/s
Collecting nbconvert<6
  Downloading nbconvert-5.6.1-py2.py3-none-any.whl (455 kB)
     |████████████████████████████████| 455 kB 6.8 MB/s
Requirement already satisfied: pip in c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages (from nbdev) (21.0.1)
Requirement already satisfied: ipykernel in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from nbdev) (5.5.3)
Collecting packaging
  Downloading packaging-20.9-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB ...
Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting ghapi
  Downloading ghapi-0.1.16-py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB 2.7 MB/s
Collecting fastrelease
  Downloading fastrelease-0.1.11-py3-none-any.whl (16 kB)
Requirement already satisfied: jupyter-client in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from nbdev) (6.1.12)
Collecting testpath
  Downloading testpath-0.4.4-py2.py3-none-any.whl (163 kB)
     |████████████████████████████████| 163 kB 6.8 MB/s
Requirement already satisfied: traitlets>=4.2 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from nbconvert<6->nbdev) (5.0.5)
Collecting jinja2>=2.4
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 6.4 MB/s
Collecting entrypoints>=0.2.2
  Downloading entrypoints-0.3-py2.py3-none-any.whl (11 kB)
Collecting pandocfilters>=1.4.1
  Downloading pandocfilters-1.4.3.tar.gz (16 kB)
Collecting bleach
  Downloading bleach-3.3.0-py2.py3-none-any.whl (283 kB)
     |████████████████████████████████| 283 kB 6.8 MB/s
Collecting defusedxml
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Requirement already satisfied: jupyter-core in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from nbconvert<6->nbdev) (4.7.1)
Requirement already satisfied: pygments in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from nbconvert<6->nbdev) (2.8.1)
Collecting mistune<2,>=0.8.1
  Downloading mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp39-cp39-win_amd64.whl (16 kB)
Requirement already satisfied: ipython-genutils in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from nbformat>=4.4.0->nbdev) (0.2.0)
Collecting jsonschema!=2.5.0,>=2.4
  Downloading jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 3.8 MB/s
Requirement already satisfied: setuptools in c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4.0->nbdev) (49.2.1)
Collecting attrs>=17.4.0
  Downloading attrs-20.3.0-py2.py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB ...
Collecting pyrsistent>=0.14.0
  Downloading pyrsistent-0.17.3.tar.gz (106 kB)
     |████████████████████████████████| 106 kB ...
Requirement already satisfied: six>=1.11.0 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4.0->nbdev) (1.15.0)
Collecting webencodings
  Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: tornado>=4.2 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipykernel->nbdev) (6.1)
Requirement already satisfied: ipython>=5.0.0 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipykernel->nbdev) (7.22.0)
Requirement already satisfied: jedi>=0.16 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel->nbdev) (0.18.0)
Requirement already satisfied: decorator in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel->nbdev) (5.0.3)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel->nbdev) (3.0.18)
Requirement already satisfied: colorama in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel->nbdev) (0.4.4)
Requirement already satisfied: backcall in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel->nbdev) (0.2.0)
Requirement already satisfied: pickleshare in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from ipython>=5.0.0->ipykernel->nbdev) (0.7.5)
Requirement already satisfied: parso<0.9.0,>=0.8.0 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from jedi>=0.16->ipython>=5.0.0->ipykernel->nbdev) (0.8.2)
Requirement already satisfied: wcwidth in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.0.0->ipykernel->nbdev) (0.2.5)
Collecting ipywidgets
  Downloading ipywidgets-7.6.3-py2.py3-none-any.whl (121 kB)
     |████████████████████████████████| 121 kB 6.4 MB/s
Collecting notebook
  Downloading notebook-6.3.0-py3-none-any.whl (9.5 MB)
     |████████████████████████████████| 9.5 MB ...
Collecting jupyter-console
  Downloading jupyter_console-6.4.0-py3-none-any.whl (22 kB)
Collecting qtconsole
  Downloading qtconsole-5.0.3-py3-none-any.whl (119 kB)
     |████████████████████████████████| 119 kB ...
Collecting jupyterlab-widgets>=1.0.0
  Downloading jupyterlab_widgets-1.0.0-py3-none-any.whl (243 kB)
     |████████████████████████████████| 243 kB 6.8 MB/s 
Collecting widgetsnbextension~=3.5.0
  Downloading widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB ...
Collecting prometheus-client
  Downloading prometheus_client-0.10.0-py2.py3-none-any.whl (55 kB)
     |████████████████████████████████| 55 kB 1.8 MB/s
Requirement already satisfied: pyzmq>=17 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from notebook->jupyter->nbdev) (22.0.3)
Collecting terminado>=0.8.3
  Downloading terminado-0.9.4-py3-none-any.whl (14 kB)
Collecting Send2Trash>=1.5.0
  Downloading Send2Trash-1.5.0-py3-none-any.whl (12 kB)
Collecting argon2-cffi
  Downloading argon2_cffi-20.1.0-cp39-cp39-win_amd64.whl (42 kB)
     |████████████████████████████████| 42 kB 322 kB/s
Requirement already satisfied: python-dateutil>=2.1 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from jupyter-client->nbdev) (2.8.1)
Requirement already satisfied: pywin32>=1.0 in c:\users\tcailleau\appdata\roaming\python\python39\site-packages (from jupyter-core->nbconvert<6->nbdev) (300)
Collecting pywinpty>=0.5
  Downloading pywinpty-0.5.7.tar.gz (49 kB)
     |████████████████████████████████| 49 kB 3.2 MB/s
Collecting cffi>=1.0.0
  Downloading cffi-1.14.5-cp39-cp39-win_amd64.whl (179 kB)
     |████████████████████████████████| 179 kB ...
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB ...
Collecting pyparsing>=2.0.2
  Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 4.8 MB/s
Collecting qtpy
     |████████████████████████████████| 54 kB 3.8 MB/s
Using legacy 'setup.py install' for pandocfilters, since package 'wheel' is not installed.
Using legacy 'setup.py install' for pyrsistent, since package 'wheel' is not installed.
Using legacy 'setup.py install' for pywinpty, since package 'wheel' is not installed.
Installing collected packages: pyrsistent, pyparsing, attrs, webencodings, pycparser, packaging, MarkupSafe, jsonschema, testpath, pywinpty, pandocfilters, nbformat, mistune, jinja2, entrypoints, defusedxml, cffi, bleach, terminado, Send2Trash, prometheus-client, nbconvert, argon2-cffi, notebook, widgetsnbextension, qtpy, jupyterlab-widgets, fastcore, qtconsole, pyyaml, jupyter-console, ipywidgets, ghapi, jupyter, fastrelease, nbdev
    Running setup.py install for pyrsistent ... done
    Running setup.py install for pywinpty ... done
    Running setup.py install for pandocfilters ... done
Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 argon2-cffi-20.1.0 attrs-20.3.0 bleach-3.3.0 cffi-1.14.5 defusedxml-0.7.1 entrypoints-0.3 fastcore-1.3.19 fastrelease-0.1.11 ghapi-0.1.16 ipywidgets-7.6.3 jinja2-2.11.3 jsonschema-3.2.0 jupyter-1.0.0 jupyter-console-6.4.0 jupyterlab-widgets-1.0.0 mistune-0.8.4 nbconvert-5.6.1 nbdev-1.1.13 nbformat-5.1.3 notebook-6.3.0 packaging-20.9 pandocfilters-1.4.3 prometheus-client-0.10.0 pycparser-2.20 pyparsing-2.4.7 pyrsistent-0.17.3 pywinpty-0.5.7 pyyaml-5.4.1 qtconsole-5.0.3 qtpy-1.9.0 terminado-0.9.4 testpath-0.4.4 webencodings-0.5.1 widgetsnbextension-3.5.1
PS C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts> ls


    Directory: C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          4/3/2021  12:46 AM                __pycache__
-a----         1/26/2021  11:19 AM         106377 epylint.exe
-a----          4/3/2021  12:46 AM         106389 iptest.exe
-a----          4/3/2021  12:46 AM         106389 iptest3.exe
-a----          4/3/2021  12:46 AM         106382 ipython.exe
-a----          4/3/2021  12:46 AM         106382 ipython3.exe
-a----         1/26/2021  11:19 AM         106401 isort-identify-imports.exe
-a----         1/26/2021  11:19 AM         106367 isort.exe
-a----          4/3/2021  12:46 AM         106419 jupyter-kernelspec.exe
-a----          4/3/2021  12:46 AM         106377 jupyter-migrate.exe
-a----          4/3/2021  12:46 AM         106398 jupyter-run.exe
-a----          4/3/2021  12:46 AM         106382 jupyter-troubleshoot.exe
-a----          4/3/2021  12:46 AM         106377 jupyter.exe
-a----          4/3/2021  12:46 AM         106373 pygmentize.exe
-a----         1/26/2021  11:19 AM         106375 pylint.exe
-a----         1/26/2021  11:19 AM         106381 pyreverse.exe
-a----          4/3/2021  12:46 AM          24996 pywin32_postinstall.py
-a----          4/3/2021  12:46 AM           3251 pywin32_testall.py
-a----         1/26/2021  11:19 AM         106377 symilar.exe


PS C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts> nbdev_build_lib
Traceback (most recent call last):
    return _run_code(code, main_globals, None,
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\tcailleau\AppData\Local\Programs\Python\Python39\Scripts\nbdev_build_lib.exe\__main__.py", line 7, in <module>
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\fastcore\script.py", line 105, in _f
    tfunc(**merge(args, args_from_prog(func, xtra)))
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 483, in nbdev_build_lib
    write_tmpls()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\fastcore\foundation.py", line 261, in __init__
    assert self.config_file.exists(), f"Could not find {cfg_name}"
AssertionError: Could not find settings.ini
PS C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts> C:\Users\tcailleau\Documents\Python\tcai-mages
C:\Users\tcailleau\Documents\Python\tcai-mages : The term 'C:\Users\tcailleau\Documents\Python\tcai-mages' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of  
the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ C:\Users\tcailleau\Documents\Python\tcai-mages
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\tcaill...thon\tcai-mages:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\tcailleau\AppData\Roaming\Python\Python39\Scripts> cd C:\Users\tcailleau\Documents\Python\tcai-mages
PS C:\Users\tcailleau\Documents\Python\tcai-mages> nbdev_build_lib
Converted 00_core.ipynb.
Converted index.ipynb.
PS C:\Users\tcailleau\Documents\Python\tcai-mages> 
PS C:\Users\tcailleau\Documents\Python\tcai-mages> nbdev_build_docs
converting: C:\Users\tcailleau\Documents\Python\tcai-mages\00_core.ipynb
An error occurred while executing the following cell:

mage = Mage("Thierry", 100, Ability(10, "water"))
print(mage)

            Thierry's Current Health: 100
            Thierry's Max Health: 100
            Thierry's Ability Damage: 10
            Thierry's Ability Type: water


------------------
from nbdev.showdoc import show_doc
from tcail-mages.core import *
------------------

  File "<ipython-input-1-21a7d7eb099d>", line 2
    from tcail-mages.core import *
              ^
SyntaxError: invalid syntax

SyntaxError: invalid syntax (<ipython-input-1-21a7d7eb099d>, line 2)

Conversion failed on the following:
00_core.ipynb
Traceback (most recent call last):
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\tcailleau\AppData\Local\Programs\Python\Python39\Scripts\nbdev_build_docs.exe\__main__.py", line 7, in <module>
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\fastcore\script.py", line 105, in _f
    tfunc(**merge(args, args_from_prog(func, xtra)))
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 665, in nbdev_build_docs
    if fname is None: make_sidebar()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 730, in make_sidebar
    create_default_sidebar()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 722, in create_default_sidebar
    dic = {Config().lib_name: _create_default_sidebar()}
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 714, in _create_default_sidebar
    titles = [_get_title(f) for f in fnames if f.stem!='index']
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 714, in <listcomp>
    titles = [_get_title(f) for f in fnames if f.stem!='index']
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 704, in _get_title
    with open(fname, 'r') as f: code = f.read()
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\tcailleau\\Documents\\Python\\tcai-mages\\docs\\core.html'
PS C:\Users\tcailleau\Documents\Python\tcai-mages>
-----------------------------------------------------

# nbdev template

Use this template to more easily create your [nbdev](https://nbdev.fast.ai/) project.

_If you are using an older version of this template, and want to upgrade to the theme-based version, see [this helper script](https://gist.github.com/hamelsmu/977e82a23dcd8dcff9058079cb4a8f18) (more explanation of what this means is contained in the link to the script)_.

## Troubleshooting Tips

-  Make sure you are using the latest version of nbdev with `pip install -U nbdev`
-  If you are using an older version of this template, see the instructions above on how to upgrade your template. 
-  It is important for you to spell the name of your user and repo correctly in `settings.ini` or the website will not have the correct address from which to source assets like CSS for your site.  When in doubt, you can open your browser's developer console and see if there are any errors related to fetching assets for your website due to an incorrect URL generated by misspelled values from `settings.ini`.
-  If you change the name of your repo, you have to make the appropriate changes in `settings.ini`
-  After you make changes to `settings.ini`, run `nbdev_build_lib && nbdev_clean_nbs && nbdev_build_docs` to make sure all changes are propagated appropriately.