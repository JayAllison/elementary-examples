# Elementary School Coding Examples
This repository contains coding examples for many different types of coding.

Even these words are an example of coding! This page is formattted using [markdown](https://guides.github.com/features/mastering-markdown/). To see the actual code that generated these words, look at readme.md in the repository.

## Scratch

Scratch is a graphical programming language for beginners - you can do it online at [https://scratch.mit.edu/](https://scratch.mit.edu/) or download it to install from [https://scratch.mit.edu/scratch_1.4/](https://scratch.mit.edu/scratch_1.4/).

The polygon example files in the scratch folder are from Scratch 1.4. That is the original offline version and the version that comes on the Raspberry Pi. The polygon examples are similar to the other languages' examples here, except that Scratch 1.4 does not support procedures (aka functions or methods) so the code is less structured and contains more duplication.

When you get more advanced with Scratch and you want to work in a 3D world, on the Raspberry Pi you can interface to Minecraft. Check out: https://github.com/scratch2mcpi/scratch2mcpi

## Logo turtle

The Logo programming language has been used for decades to visualize programming for beginners.
 
Many Logo tutorials are available at [https://turtleacademy.com/](https://turtleacademy.com/)

The `/turtle` folder contains examples that can be used at [https://turtleacademy.com/program/new/en_US](https://turtleacademy.com/program/new/en_US)

Learn how to draw pictures like this:

![alt text](https://github.com/JayAllison/elementary-examples/raw/master/turtle/squares.png "Logo Turtle Squares" )

## Python turtle

Python is a great programming language for learning text-based programming, and it is supported on many platforms. You can download it here: [https://www.python.org/downloads/](https://www.python.org/downloads/). The examples I have provided were tested with Python 2.7.

I'm assuming that you are running Python on your Raspberry Pi or other Linux machine, so I'm going to give you instructions for Linux setup, although the installation instructions will likely work under Windows, too, once you have installed python and pip.

Run these commands to make sure everything is up to date (these apply only to Linux, not to Windows):
```commandline
sudo apt-get update
sudo apt-get upgrade
```

Now run these commands to install iPython, an interactive Python shell (this should work on Linux and Windows, if python and pip are already installed)
```commandline
sudo pip install python-dev
sudo pip install ipython
```
_Note: on Windows, leave off the ``sudo`` keyword._

Now you can run Python interactively, including tab completion, by typing:

```commandline
ipython
```

You can then enter commands into ipython. Some of the examples included in the '/python' folder can be entered directly into ipython. For the turtle examples, doing it interactively rather than in a scripted file is a lot more fun for kids. When you're done, just type `exit`.

Here's an example of what you can do with turtle in Python:

![alt text](https://github.com/JayAllison/elementary-examples/raw/master/python/squares.png "Python Turtle Squares" )

If you change to the directory that contains the python files and open interactive python using the ``ipython`` command, then you can draw this image by entering these commands:

```python
from basic_geometry import *
my_turtle = turtle.Turtle()
draw_grid_of_randomly_colored_squares(my_turtle, 5, 50, 10)
```

## Python and Minecraft Pi

If you're comfortable commanding the turtle to move in 2D, then it's time to step up to 3D, and Minecraft on the Raspberry Pi is a fun way to do that in an environment that the students are probably familiar with. The library that allows Python to control Minecraft on the Raspberry Pi is probably already installed, but if not you can get it by running this command:

```commandline
sudo pip install mcpi
```

Then, you can use the minecraft examples in the `/python` folder to explore and create.
