from unittest import TestCase


class Test(TestCase):
    def test_fibonacci_recursive(self):
        from unittest_example_src import fibonacci_recursive
        self.assertEqual(fibonacci_recursive(5), fibonacci_recursive(4)+ fibonacci_recursive(3))
        self.assertIn("Test", ("Test","Test2"), "Test not in container")
        self.assertListEqual(["one","two","three"], ["one","two"], "Lists not equal")







