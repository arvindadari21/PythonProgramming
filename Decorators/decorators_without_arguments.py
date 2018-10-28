"""
Decorators works on the principle of `closure`

* Non local variables?
    - In Python, these non-local variables are read only by default and we must
      declare them explicitly as non-local (using nonlocal keyword) in order to
      modify them.

* Nested function?
    - A function defined inside another function is called a nested function.
      Nested functions can access variables of the enclosing scope.

The nested function is python are able to access the non-local variables. How?
- There comes the use of  concept `closure`
  This technique by which some data gets attached to the code is called
  `closure` in Python.

The criteria that must be met to create closure in Python are summarized in the
following points.
    - We must have a nested function (function inside a function).
    - The nested function must refer to a value defined in the enclosing
      function.
    - The enclosing function must return the nested function.

What are closures good for?
    - Closures can avoid the use of global values and provides some form of
      data hiding. It can also provide an object oriented solution to the
      problem.

Decorators make extensive use of `closure`.
All function objects have a __closure__ attribute that returns a tuple of cell
objects if it is a closure function.
"""


def custom_decorator(func_):
    def wrapper_method(*args, **kwargs):
        """
        This is the wrapper function.
        :param args:
        :param kwargs:
        :return:
        """
        print("This is the custom decorator called")
        print("Calling method: {}".format(func_.__name__))
        func_(*args, **kwargs)
    return wrapper_method
