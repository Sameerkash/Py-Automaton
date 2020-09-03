from cx_Freeze import setup, Executable

base = None    

executables = [Executable("tool.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ZIP Automation",
    options = options,
    version = "1.0",
    description = 'An automated software to extract any ZIP file as soon as it is downloaded',
    executables = executables
)