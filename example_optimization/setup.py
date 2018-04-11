import numpy
from distutils.core import setup
from distutils.extension import Extension

# Produce annotated html files
import Cython
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import Cython.Build


setup(
 ext_modules = Cython.Build.cythonize([Extension("rotate_cython", ["myfunc.pyx"],
                                include_dirs=[numpy.get_include()])]))
