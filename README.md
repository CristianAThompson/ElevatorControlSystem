## ElevatorControlSystem 
____
##### Python project to build a basic Elevator Control system
____

### Notes
* I consciously chose to use only the most basic tooling I was able to with this implementation of the MVP
* This doesn't make use of any advanced technologies such as running a venv, this is specifically because we are not using any PIP packages or have any needs for more elaborate config. If I moved to a level of complexity that required me to use packages of some sort I would want to start encapsulating my python environment to prevent OS corruption and improve ease of maintenance.

### Steps to run tests
1. In order to run this and see the passing tests you will need to `cd <YOUR_DIRECTORY_CONTAINING_ElevatorControlSystem.py>`
2. Once in the same directory as the python files we can execute the tests without needing to install anything further by executing `python3 ElevatorControlSystem_Tests.py`

    <sub>this may vary based on your particular system see pre-requisites if you don't already have python 3.x</sub> 
3. You should then be able to observe 5 tests with multiple assertions in each test passing in nearly not time at all.

### Pre-requisites
* Install Python 3.x, I don't specify which version as long as it's 3.7+ to ensure complete compatability
