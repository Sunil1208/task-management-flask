import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname((__file__)))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

"""Info:
    The WTF_CSRF_ENABLED config setting is used for cross-site request forgery
    prevention, which makes your app more secure. This setting is used by the Flask-
    WTF extension.

    The SECRET_KEY config setting is used in conjunction with the
    WTF_CSRF_ENABLED setting in order to create a cryptographic token that is used to validate a form. It's
    also used for the same reason in conjunction with sessions. Make sure the secret
    key is nearly impossible to guess. Use a random key generator.
"""

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
