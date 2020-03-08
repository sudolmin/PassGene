import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/Python/Python38-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/Python/Python38-32/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['C:/Users/Programs/Python/Python38-32/DLLs/tcl86t.dll',
                   'C:/Users/Programs/Python/Python38-32/DLLs/tk86t.dll']
)

executables = [
    Executable('PassGene.py', base=None)
]

setup(name='PassGene',
      version = 'v1.0',
      description = 'Password Generator',
      options = dict(build_exe = buildOptions),
      executables = executables)

