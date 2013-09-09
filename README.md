django_multidb_middleware
=========================

Middleware for Django, to work with multi database connection using User model.

Usage:
- Put all files in your project folder.
- Edit your settings.py with these:
    * Change your middleware
        MIDDLEWARE_CLASSES = (
            'middleware.CustomerMiddleware',
        )
    * Add this:
    DATABASE_ROUTERS = ['authrouter.AuthRouter',
                        'authrouter.PadraoRouter']

Don't forget to create one field in your user profile mode, put the name: db_name = models.CharField(...)

Know Problems
=============
Can't use syncdb.
