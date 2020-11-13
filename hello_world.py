# This project is licensed under the terms of the MIT license.
# Open command window or Windows Powershell
# change to directory with Python Scripts in
# venue        cd C:\Users\russt\OneDrive\Documents\Prog
# e5440        cd C:\Users\russ\OneDrive\Documents\Prog
# Opti760      cd /var/samba/shares/public/prog

# SCRIPTS:
# venue   c:\users\russt\appdata\local\programs\python\python36-32\lib\site-packages
# e5440   C:\Users\russ\AppData\Local\Programs\Python\Python38\Scripts

#
# use pylint to check code
#
# to run script:
# Windows 'hello_world.py '
# Linux 'python3 hello_world.py '

# A comment is anything after the # hash/octothorpe/pound sign and is ignored by python.
# Comments are so you can read your program later.

# based on Python Tutorials https://docs.python.org/3/tutorial/

"""
Outputs text "Hello World!" to the monitor.

It must be the first statement in the object’s (module, function, class, and method) definition.
You can access docstrings  using the following special variable: myobj.__doc__
e.g. print(theFunction.__doc__)
They should not be descriptive should describe what the function does, not how
and end with a period.
"""
#to view the docstring start Python
# C\:> py
# >>> import moduleName
# >>> help(moduleName)

# define function
def print_hello():
    """prints Hello World to screen"""
    print("Hello World!")


def main():
    """Calls print_hello to output "Hello World!" to the monitor """
    # pylint: disable=too-many-branches
    # call function defined above
    print_hello()
    # pylint: enable=too-many-branches

if __name__ == "__main__":
    # executes only if run as a script
    # sys.exit(main(sys.argv))
    main()


# python installed in C:\Users\russt\AppData\Local\Programs\Python\Python38
# and on Linux        /usr/bin/python3
# Open command window or Windows Powershell use cmd "py --version" to check install
# Use command "py -m pydoc [keyword]" for python documentation

# FILE:
# Typically, a Python file is any file that contains code. Most Python files have the extension .py.
# SCRIPT:
# A Python script is a file that you intend to execute from the command line to accomplish a task.
# MODULE:
# A Python module is a file that you intend to import from within another module or a script,
# or from the interactive interpreter. You can read more about modules in the Python documentation.

# Put most code into a function or class.
# Use __name__ to control execution of your code.
# Create a function called main() to contain the code you want to run.
# Call other functions from main().

# What is the order of operations in Python? The same as the US
# acronym PEMDAS which stands for
# Parentheses Exponents Multiplication Division Addition Subtraction

# Python Style guide: https://www.python.org/dev/peps/pep-0008/
# Use 4 spaces per indentation level.
# Spaces are the preferred indentation method (not tabs)
# Limit all lines to a maximum of 79 characters.
# break before binary operations
# 2 blank lines around top-level function and class definitions
# 1 blank lines around Method definitions inside a class
# blank lines in functions, sparingly, to indicate logical sections.
# Extra blank lines may be used (sparingly) to separate groups of related functions.
# Code in the core Python distribution should always use UTF-8
# IMPORTS should usually be on separate lines
# Naming Convention.............
# FUNCTION and VARIABLE names: lowercase words separated by underscores
# METHOD names and Instance Variables as function names.
# CONSTANTS: Words all capital letters separated by underscores.
# CLASS names: should normally use the CapWords convention.
