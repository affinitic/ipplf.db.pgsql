# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta
from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy import desc, and_, or_
from sqlalchemy.orm import backref, mapper, relationship
from ipplf.db.pgsql.baseTypes import (DemandeIntervention)
from ipplf.db.pgsql.tables import (getDemandeIntervention)


class ipplfModel(object):
    """
    A model providers provides information about the tables to be used
    and the mapper classes.
    """
    implements(IModelProvider)

    def getModel(self, metadata=None):
        """
        ipplf database model
        """
        model = Model()
        model.metadata = metadata

## table demande intervention ##
        demandeInterventionTable = getDemandeIntervention(metadata)
        demandeInterventionTable.create(checkfirst=True)
        mapper(DemandeIntervention, demandeInterventionTable)



        return model
