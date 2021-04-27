import unittest
import ElevatorControlSystem

class TestStringMethods(unittest.TestCase):

    def test_im_here(self):
        self.assertEqual(ElevatorControlSystem.testFunction(), 'I\'m here.')

if __name__ == '__main__':
    unittest.main()