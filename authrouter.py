# -*- coding: utf-8 -*-
__author__ = 'Fellipe Henrique < fellipeh@gmail.com >'
__copyright__ = '2013 (tm) Point Informatica '
__version__ = '0.1'

#                ( O O )
# +===========oOO==(_)==OOo==============+

# Created : 19/07/13
# Changed :

# -*- coding: utf 8 -*-

class PadraoRouter(object):
    def db_for_read(self, model, **hints):
        # if model._meta.app_label == 'auth':
        #     return 'auth_db'
        from pointlib.middleware import my_local_global

        return my_local_global.database_name

    def db_for_write(self, model, **hints):
        # if model._meta.app_label == 'auth':
        #     return 'auth_db'
        from pointlib.middleware import my_local_global

        return my_local_global.database_name

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
#        db_list = ('OFICIAL')
#        if obj1.state.db in db_list and obj2.state.db in db_list:
#            return True
        return None

    def allow_syncdb(self, db, model):
        """
        All non-auth models end up in this pool.
        """
        return True


class AuthRouter(object):
    """
    Foi criado um router para definir para onde vai a autenticacao no inicio do projeto.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to default.
        """
        if model._meta.app_label == 'auth':
            return 'auth_db'
        if model._meta.app_label == 'sessions':
            return 'auth_db'
        if model._meta.app_label == 'web_core':
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to default.
        """
        if model._meta.app_label == 'auth':
            return 'auth_db'
        if model._meta.app_label == 'sessions':
            return 'auth_db'
        if model._meta.app_label == 'web_core':
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'auth' or\
           obj2._meta.app_label == 'auth':
            return True
        if obj1._meta.app_label == 'sessions' or\
           obj2._meta.app_label == 'sessions':
            return True
        if obj1._meta.app_label == 'web_core' or\
           obj2._meta.app_label == 'web_core':
            return True
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the auth app only appears in the 'default'
        database.
        """
        if db == 'auth_db':
            return model._meta.app_label == 'auth'
        elif model._meta.app_label == 'auth':
            return False
        return None