# General settings
LISTEN_ADDR = "0.0.0.0"
PORT = 3000
DEBUG = True # Disable this for production
IS_PROXY = False # Turn this on if you are using it behind a proxy
CHARSET = "utf8" # In case another charset is required, also applies to database settings
TIMEZONE = "Europe/Warsaw" # If timestamps are having an offset
BASEURL = "http://localhost:3000" # Origin URL, required for generating links
EMAIL_ADDRESS = "no-reply@rly.li" # Email address used for outgoing mails
SECRET_KEY = "<paste here the output of $(</dev/urandom tr -dc A-Za-z0-9 | head -c 28)>" # Used for generating keys for users

# Database settings
DATABASE = {
    "backend": "mongodb", # You can select between redis and mongodb
    "host": "localhost",
    "port": 27015,
    "username": "", # Leave this empty if using redis
    "password": "",
    "db": "shortener"
}

# Email settings
EMAIL = {
    "hostname": "smtp.example.com",
    "auth": True,
    "username": "admin@example.com",
    "password": "p4ssw0rd",
    "secure": "tls",
    "port": 587
}

# Website settings
WEBSITE = {
    "title": "Rly.li URL Shortener", # Also used as app name
    "description": "Rly.li is lightweight service that takes long URLs and squeezes them into fewer characters \
                    to make a link that is easier to share, tweet, or email to friends.",
    "author": "David Sn",
    "copyright": "2015-2018 David Sn", # Displayed on the footer
}

# Login settings
LOGIN = {
    "allowGuests": True, # Enables guest mode
    "emailActivation": True, # Send out emails for confirmation of registration, recommended: True
    "resendActivationThreshold": 30, # Amount of time after which an user can request a new activation email
    "disableSignup": False, # Disables sign up for new users
}

# URL generator settings
URL_GENERATOR = {
    "public": {
        "type": "random",
        "length": 4 # Custom short URLs are the length of public URLs + 1 additional letter
    },
    "private": {
        "type": "phonetic", # Phonetic are easier to remember
        "length": 6
    }
}