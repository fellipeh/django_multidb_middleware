# -*- coding: utf-8 -*-
__author__ = 'Fellipe Henrique < fellipeh@gmail.com >'
__copyright__ = '2013 (tm) Point Informatica '
__version__ = '0.1'

#                ( O O )
# +===========oOO==(_)==OOo==============+

# Created : 23/07/13
# Changed :

from threading import local
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from web_core.models import UserProfile


my_local_global = local()


class CustomerMiddleware(object):
    def process_request(self, request):
        my_local_global.database_name = get_database_name(request)


def get_database_name(request):
    session_key = request.session.session_key
    try:
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)

        profile = UserProfile.objects.get(user_id=uid)

        if profile:
            return profile.dbname
        else:
            return None
    except:
        return None
