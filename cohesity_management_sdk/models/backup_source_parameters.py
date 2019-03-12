# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.physical_backup_source_parameters
import cohesity_management_sdk.models.vmware_backup_source_parameters

class BackupSourceParameters(object):

    """Implementation of the 'Backup Source Parameters.' model.

    Message to capture any additional backup params at the source level.

    Attributes:
        app_entity_id_vec (list of long|int): If we are backing up an
            application (such as SQL), this contains the entity ids of the app
            entities (such as SQL instances and databases) that will be
            protected on the backup source.  If this vector is empty, it
            implies that we are protecting all app entities on the source.
        physical_params (PhysicalBackupSourceParameters): Message to capture
            additional backup params for a Physical type source.
        skip_indexing (bool): Set to true, if indexing is not required for
            given source.
        source_id (long|int): Source entity id. NOTE: This is expected to
            point to a leaf-level entity.
        vmware_params (VmwareBackupSourceParameters): Message to capture
            additional backup params for a VMware type source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_entity_id_vec":'appEntityIdVec',
        "physical_params":'physicalParams',
        "skip_indexing":'skipIndexing',
        "source_id":'sourceId',
        "vmware_params":'vmwareParams'
    }

    def __init__(self,
                 app_entity_id_vec=None,
                 physical_params=None,
                 skip_indexing=None,
                 source_id=None,
                 vmware_params=None):
        """Constructor for the BackupSourceParameters class"""

        # Initialize members of the class
        self.app_entity_id_vec = app_entity_id_vec
        self.physical_params = physical_params
        self.skip_indexing = skip_indexing
        self.source_id = source_id
        self.vmware_params = vmware_params


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
        app_entity_id_vec = dictionary.get('appEntityIdVec')
        physical_params = cohesity_management_sdk.models.physical_backup_source_parameters.PhysicalBackupSourceParameters.from_dictionary(dictionary.get('physicalParams')) if dictionary.get('physicalParams') else None
        skip_indexing = dictionary.get('skipIndexing')
        source_id = dictionary.get('sourceId')
        vmware_params = cohesity_management_sdk.models.vmware_backup_source_parameters.VmwareBackupSourceParameters.from_dictionary(dictionary.get('vmwareParams')) if dictionary.get('vmwareParams') else None

        # Return an object of this model
        return cls(app_entity_id_vec,
                   physical_params,
                   skip_indexing,
                   source_id,
                   vmware_params)


