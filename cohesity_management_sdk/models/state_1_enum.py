# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class State1Enum(object):

    """Implementation of the 'State1' enum.

    Specifies the current state of the app instance.
    Specifies operational status of an app instance.
    kInitializing - The app instance has been launched or resumed, but is not
    fully running yet.
    kRunning - The app instance is running. Check health_status for the actual
    health.
    kPausing - The app instance is being paused.
    kPaused - The app instance has been paused.
    kTerminating - The app instance is being terminated.
    kTerminated -  The app instance has been terminated.
    kFailed - The app instance has failed due to an unrecoverable error.

    Attributes:
        KINITIALIZING: TODO: type description here.
        KRUNNING: TODO: type description here.
        KPAUSING: TODO: type description here.
        KPAUSED: TODO: type description here.
        KTERMINATING: TODO: type description here.
        KTERMINATED: TODO: type description here.
        KFAILED: TODO: type description here.

    """

    KINITIALIZING = 'kInitializing'

    KRUNNING = 'kRunning'

    KPAUSING = 'kPausing'

    KPAUSED = 'kPaused'

    KTERMINATING = 'kTerminating'

    KTERMINATED = 'kTerminated'

    KFAILED = 'kFailed'

