# TestingTravisCI
 Part 1: Test travis.yml setup with flake8, encryption, and requirements.txt. 
 Added unit testing to the travis.yml path. Obtained the green light!

Part 2: Testing Jupyter notebooks with Travis.ci (https://github.com/ghego/travis_anaconda_jupyter)

Barebone example of how to check for execution errors in Jupyter notebook using Travis CI and a custom conda environment file.

The notebook is executed using jupyter nbconvert in a subprocess while monitoring for errors.

Requirements:

jupyter
py.test
