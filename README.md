# gitSession
how to use GitHub


Clone the Master branch to your dev machine and setup your IDE and Python Environments

Add a Python virtual environment and activate it

    If you are using PyCharm this is as easy as going to File->Settings->ProjectName->Project Interpreter. 
    You then add a new Environment
    Install project dependencies using pip install -r requirements.txt. 
    All additional packages to be used in this project should be added here along with any special    instructions for running those packages
    Create a file called local_settings.py in the settings folder if you need to use local developer settings,
    this file will not be committed as it is set to be ignored in the .ignore file
    Run migrations python manage.py migrate
    
DEVELOPMENT
CODING WORKFLOW

    Never commit to Master or make a Pull Request without express permission from project lead
    Make all your branches from the staging branch and only make a Pull Request when you are satisfied with your own working branch
    Commit code to your working branch every 30 mins or at logical points whichever comes first
    Before making a PR to Staging Branch, pull in any changes from Staging into your working branch and resolve conflicts if any

CODING STYLE

-As ever the coding style is PEP-8 see https://realpython.com/python-pep8/
API DOCUMENTATION

-API documentation can be found at the /docs/ endpoint of whatever server you are using e.g http://3.106.136.45:8000/docs/ for the AWS instance

Happy Coding
