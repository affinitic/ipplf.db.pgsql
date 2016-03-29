# -*- coding: utf-8 -*-
import os
import logging
from z3c.sqlalchemy import createSAWrapper, getSAWrapper
from zope.component import getUtility
from affinitic.pwmanager.interfaces import IPasswordManager

LOGGER = 'ipplf.db.pgsql'
logging.getLogger(LOGGER).info('ipplf.db.pgsql - Installing Product')

def host():
    return os.environ.get('PG_PORT_5432_TCP_ADDR', 'localhost')


def session():
    wrapper = getSAWrapper('ipplf')
    return wrapper.session


def initialize(context):
    pwManager = getUtility(IPasswordManager, 'pg')
    connString = 'postgresql://%s@%s/ipplf' % (pwManager.getLoginPassWithSeparator(':'), host())
    wr = createSAWrapper(connString,
                        forZope=True,
                        echo=False,
                        engine_options={'convert_unicode': True},
                        name='ipplf',
                        model='ipplfMappings')
    return wr
