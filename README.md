# Flask_Miniblog

A Fundamental server monitoring system using flask.

## Miniblog functionalities

The miniblog to be developed will have the following characteristics:

* There will be two types of user: administrators and guests.
* An administrator user can add, modify and delete blog entries.
* Guest users can register on the blog to comment on the different entries.
* An administrator user can list and delete users, in addition to being able to assign them the administrator role.

## Download and install the project

To download the project you can clone the repository:

    git clone https://github.com/josepmartorell/Flask-Miniblog.git

### Environment Variables

For the miniblog to work you must create the following environment variables:

#### Linux / Mac

    export FLASK_APP = "entrypoint"
    export FLASK_ENV = "development"
    export APP_SETTINGS_MODULE = "config.local"

#### Windows

    set "FLASK_APP = entrypoint"
    set "FLASK_ENV = development"
    set "APP_SETTINGS_MODULE = config.local"
    
> My recommendation for testing is that you add these variables in the "activate" or "activate.bat" file
> if you are using virtualenv
 
### Installing dependencies

A file (requirements.txt) with all the dependencies is distributed in the project. To install them
just run:

    pip install -r requirements.txt

## Execution with the server that Flask brings

Once you have downloaded the project, created the environment variables and installed the dependencies,
you can start the project by running:

    flask run
