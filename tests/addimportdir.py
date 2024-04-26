"""Adds the current working directory to the PYTHONPATH
variable, to make the package accessible for the unittest script."""

import sys
import os
workdir = os.getcwd()

def importdir():
    sys.path.append(workdir)

def removedir():
    sys.path.remove(workdir)