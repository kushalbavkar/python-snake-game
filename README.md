# Python Snake Game
Python snake game for education purpose.

Developed using pygame library.

## Pre-requisites
1. Python / Anaconda / Miniconda
2. IDE of your choice (IntelliJ Idea / Pycharm / VS Code etc...)
3. Git

## Setup environment

### Environment variables (Optional)

      $ PIPENV_VENV_IN_PROJECT  =  1          # forces virtual environment creation in project directory
      $ WORKON_HOME = {directory.of.choice}   # forces virtual enviroment in specified directory 

### Install 'pipenv' package manager

      $ pip install pipenv

### Setup 'conda' environment (Optional)

Use this step only if you are using lower version of python < 3.9 and wish to upgrade it rather than
installing separately.
However, you can still use `conda` environment + `virtual` environment created using pipenv if you wish to.


#### Create conda environment

      $ conda create --name py39 python=3.9

#### Activate conda environment

      # --- If you are using command prompt ---
      $ conda activate py39

      # --- If you are using git bash ---
      $ source activate py39

### Create virtual environment using `pipenv` & install packages from Pipfile

#### Navigate to project directory

      $ cd {project.dir}

#### Create virtual environment & install packages

      $ pipenv --site-packages install --dev --skip-lock

### Verify installation

#### Virtual environment location

      $ pipenv --venv

#### Python interpreter location

      $ pipenv run where python        # Use the python.exe location from virtual environment

#### Check Installed packages

      $ pipenv graph

### Start Game

      $ pipenv run python -m snake.main 

## References
[www.edureka.co](https://www.edureka.co/blog/snake-game-with-pygame/)