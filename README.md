# pytest-exception-interact

Example of usage of pytest hook to take a screenshot in case of error when 
running selenium automated tests

# installation

These examples are intended to be self-explanatory to a Python developer, 
with minimal setup - In addition to 3.6+, you'll also need some plugins 
to use all these examples, which you can install by running:

    pip install -r requirements.txt

I recommend using a virtual environment, to not affect your local Python libraries.
Once requirements are installed, tests can be triggered by:

    pytest

Tests run in a headless mode by default. Change this line if you want to see browser

    src/conftest.py:15

