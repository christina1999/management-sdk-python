# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.group_information
import cohesity_management_sdk.models.tenant_information
import cohesity_management_sdk.models.user_information

class EntityPermissionInformation(object):

    """Implementation of the 'Entity Permission Information.' model.

    Specifies the permission information of entities.

    Attributes:
        entity_id (long|int): Specifies the entity id.
        groups (list of GroupInformation): Specifies groups that have access
            to entity in case of restricted user.
        tenant (TenantInformation): Specifies struct with basic tenant
            details.
        users (list of UserInformation): Specifies users that have access to
            entity in case of restricted user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "groups":'groups',
        "tenant":'tenant',
        "users":'users'
    }

    def __init__(self,
                 entity_id=None,
                 groups=None,
                 tenant=None,
                 users=None):
        """Constructor for the EntityPermissionInformation class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.groups = groups
        self.tenant = tenant
        self.users = users


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
        entity_id = dictionary.get('entityId')
        groups = None
        if dictionary.get('groups') != None:
            groups = list()
            for structure in dictionary.get('groups'):
                groups.append(cohesity_management_sdk.models.group_information.GroupInformation.from_dictionary(structure))
        tenant = cohesity_management_sdk.models.tenant_information.TenantInformation.from_dictionary(dictionary.get('tenant')) if dictionary.get('tenant') else None
        users = None
        if dictionary.get('users') != None:
            users = list()
            for structure in dictionary.get('users'):
                users.append(cohesity_management_sdk.models.user_information.UserInformation.from_dictionary(structure))

        # Return an object of this model
        return cls(entity_id,
                   groups,
                   tenant,
                   users)


