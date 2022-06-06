# Python-Space-Shooter-Game

## About The Project
The project is a throwback to the old Atari game "Space-Invaders", developed in a casual bullet-hell style. The player is expected to destroy incoming enemies while simultaneouly dodging their attacks. The controls are as follows:
- UP ARROW: Moves forward
- DOWN ARROW: Moves backwards
- LEFT ARROW: Strafe Left
- RIGHT ARROW: Strafe Right

As the player destroys all enemy spaceship in each wave, the game progressively gets harder where more enemies are contained in the following waves.

## Building/Running
The **Executable** directory contains the executable(SpaceShooter.exe) of the game built using [PyInstaller](https://pyinstaller.org/en/stable/#). To run the executable, simply double click the executable.
  
The source file of the game is contained within a single **SpaceShooter.py**. The third-party module [PyGame](https://www.pygame.org/wiki/GettingStarted) is required to run the code. In the directory of the source file, use command:
** For Windows **  
_python SpaceShooter.py_  
** For Linux **  
_python3 SpaceShooter.py_
