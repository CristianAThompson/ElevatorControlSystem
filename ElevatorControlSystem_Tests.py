import unittest
import ElevatorControlSystem

class ElevatorTests(unittest.TestCase):

    def test_im_here(self):
        elevator = ElevatorControlSystem.Elevator()
        testFunctionMessage = elevator.testFunction()
        self.assertEqual(testFunctionMessage, 'I\'m here.')
    
    def test_elevator_returns_levels_after_button_press(self):
        elevator = ElevatorControlSystem.Elevator({"current_level": 0})
        self.assertEqual(elevator.press_buttons([1]), [1])
        self.assertEqual(elevator.press_buttons([6]), [1, 6])
        self.assertEqual(elevator.press_buttons([4]), [1, 4, 6])

    def test_elevator_does_nothing_if_not_integer_pressed(self):
        elevator = ElevatorControlSystem.Elevator({"current_level": 0})
        self.assertFalse(elevator.press_buttons('a'))
        self.assertEqual(elevator.press_buttons([6]), [6])
        self.assertEqual(elevator.press_buttons([4]), [4, 6])

    def test_elevator_moves(self):
        elevator = ElevatorControlSystem.Elevator({"current_level": 0})
        self.assertEqual(elevator.press_buttons([1]), [1])
        # Tell the elevator to move
        elevator.move()
        # Get a report from the elevator of where it is now
        self.assertEqual(elevator.report(), {
            'current_level': 1,
            'maximum_level': 10,
            'levels': []
        })
        self.assertFalse(elevator.move())
    
    def test_elevator_moves_multiple_times(self):
        elevator = ElevatorControlSystem.Elevator({"current_level": 1})
        self.assertEqual(elevator.press_buttons([1]), [1])
        self.assertEqual(elevator.press_buttons([6]), [1, 6])
        self.assertEqual(elevator.press_buttons([4]), [1, 4, 6])        
        # Tell the elevator to move
        self.assertTrue(elevator.move())
        # Get a report from the elevator of where it is now
        self.assertEqual(elevator.report(), {
            'current_level': 1,
            'maximum_level': 10,
            'levels': [4, 6]
        })
        self.assertTrue(elevator.move())
        self.assertEqual(elevator.report(), {
            'current_level': 4,
            'maximum_level': 10,
            'levels': [6]
        })
        self.assertTrue(elevator.move())
        self.assertEqual(elevator.report(), {
            'current_level': 6,
            'maximum_level': 10,
            'levels': []
        })

if __name__ == '__main__':
    unittest.main()