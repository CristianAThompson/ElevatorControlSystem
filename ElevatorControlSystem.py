class Elevator:
    # Declare initial values
    current_level = 0
    maximum_level = 10
    levels = []

    def __init__(self, initial_configuration = None):
        if initial_configuration is not None:
            self.current_level = initial_configuration['current_level'] if 'current_level' in initial_configuration else 0
            self.maximum_level = initial_configuration['maximum_level'] if 'maximum_level' in initial_configuration else 10

    # Tempting as it may be don't remove me, I'm proof tests are running and passing
    def testFunction(self):
        return 'I\'m here.'

    def press_buttons(self, buttons_pressed):
        if not isinstance(buttons_pressed, list):
            buttons_pressed = [buttons_pressed]
        self.levels = buttons_pressed + self.levels
        self.levels.sort()
        return self.levels
    
    def move(self):
        # If we aren't on the level declared in our stored levels let's move to that next level
        if len(self.levels) > 0:
            if self.current_level != self.levels[0]:
                self.current_level = self.levels[0]
            self.levels.pop(0)
            return True
        else:
            return False

    def report(self):
        return {
            'current_level': self.current_level,
            'maximum_level': self.maximum_level,
            'levels': self.levels
        }