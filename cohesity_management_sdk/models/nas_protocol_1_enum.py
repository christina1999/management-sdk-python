# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class NasProtocol1Enum(object):

    """Implementation of the 'NasProtocol1' enum.

    Specifies the preferred protocol to use for backup. This does not
    apply to generic NAS and will be ignored.
    Specifies the protocol used by a NAS server.
    'kNfs3' indicates NFS v3 protocol.
    'kCifs1' indicates CIFS v1.0 protocol.

    Attributes:
        KNFS3: TODO: type description here.
        KCIFS1: TODO: type description here.

    """

    KNFS3 = 'kNfs3'

    KCIFS1 = 'kCifs1'

