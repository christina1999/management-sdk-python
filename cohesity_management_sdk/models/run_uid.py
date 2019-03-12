# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.unique_global_id

class RunUID(object):

    """Implementation of the 'Run UID.' model.

    Specifies the universal id of the latest successful Protection Job Run.

    Attributes:
        job_uid (UniqueGlobalId): Specifies an id for an object that is unique
            across Cohesity Clusters. The id is composite of all the ids
            listed below.
        start_time_usecs (long|int): Specifies the start time of the
            Protection Job Run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_uid":'jobUid',
        "start_time_usecs":'startTimeUsecs'
    }

    def __init__(self,
                 job_uid=None,
                 start_time_usecs=None):
        """Constructor for the RunUID class"""

        # Initialize members of the class
        self.job_uid = job_uid
        self.start_time_usecs = start_time_usecs


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        job_uid = cohesity_management_sdk.models.unique_global_id.UniqueGlobalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        start_time_usecs = dictionary.get('startTimeUsecs')

        # Return an object of this model
        return cls(job_uid,
                   start_time_usecs)


