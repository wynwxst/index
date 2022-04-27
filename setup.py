from distutils.core import setup
import py2exe
import upmcore
import upmguess
import upmindex
import flags
import sys
import index
import lxml
import requests
import lxml.etree
import lxml._elementpath
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
setup(console=['index.py'],options={"py2exe": {"includes": ['upmcore', 'upmguess', 'upmindex',"flags","lxml","requests","lxml._elementpath"]}})
