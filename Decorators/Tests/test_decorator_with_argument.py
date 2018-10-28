"""
Unittest cases for class based decorator
"""

import unittest
from Decorators.decorators_without_arguments import custom_decorator


class TestClassBasedDecorator(unittest.TestCase):
    """
    Test cases for class based decorator
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_custom_class_decorator(self):

        def method_without_argument_needs_decorator():
            print("This method needs class decorator")

        # Call the method with decorator
        method_without_argument_needs_decorator = custom_decorator(method_without_argument_needs_decorator)
        method_without_argument_needs_decorator()
