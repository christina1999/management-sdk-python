# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class Type13Enum(object):

    """Implementation of the 'Type13' enum.

    Specifies the type of this Vserver.
    Specifies the type of the NetApp Vserver.
    'kData' indicates the Vserver is used for data backup and restore.
    'kAdmin' indicates the Vserver is used for cluster-wide management.
    'kSystem' indicates the Vserver is used for cluster-scoped communications
    in an IPspace.
    'kNode' indicates the Vserver is used as the physical controller.
    'kUnknown' indicates the Vserver is used for an unknown purpose.

    Attributes:
        KDATA: TODO: type description here.
        KADMIN: TODO: type description here.
        KSYSTEM: TODO: type description here.
        KNODE: TODO: type description here.
        KUNKNOWN: TODO: type description here.

    """

    KDATA = 'kData'

    KADMIN = 'kAdmin'

    KSYSTEM = 'kSystem'

    KNODE = 'kNode'

    KUNKNOWN = 'kUnknown'

