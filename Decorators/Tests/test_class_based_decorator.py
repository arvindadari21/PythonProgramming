"""
Unittest cases for class based decorator
"""

import unittest
from Decorators.class_based_decorators import CustomDecorator


class TestClassBasedDecorator(unittest.TestCase):
    """
    Test cases for class based decorator
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_custom_class_decorator(self):

        def method_needs_decorator():
            print("This method needs class decorator")

        # Call the method which is wrapped with decorator
        method_needs_decorator = CustomDecorator()(method_needs_decorator)
        method_needs_decorator()
