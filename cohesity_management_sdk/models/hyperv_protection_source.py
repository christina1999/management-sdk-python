# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.agent_information
import cohesity_management_sdk.models.hyperv_datastore_object
import cohesity_management_sdk.models.hyperv_virtual_machine_object

class HypervProtectionSource(object):

    """Implementation of the 'HyperV Protection Source.' model.

    Specifies a Protection Source in HyperV environment.

    Attributes:
        agents (list of AgentInformation): Array of Agents on the Physical
            Protection Source.  Specifiles the agents running on the HyperV
            Protection Source and the status information.
        backup_type (BackupTypeEnum): Specifies the type of backup supported
            by the VM. 'kRctBackup', 'kVssBackup' Specifies the type of an
            HyperV datastore object. 'kRctBackup' indicates backup is done
            using RCT/checkpoints. 'kVssBackup' indicates backup is done using
            VSS.
        cluster_name (string): Specifies the cluster name for 'kHostCluster'
            objects.
        datastore_info (HypervDatastoreObject): Specifies information about a
            Datastore Object in HyperV environment.
        description (string): Specifies a description about the Protection
            Source.
        host_type (HostType4Enum): Specifies host OS type for
            'kVirtualMachine' objects. 'kLinux' indicates the Linux operating
            system. 'kWindows' indicates the Microsoft Windows operating
            system. 'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system.
        hyperv_uuid (string): Specifies the UUID for 'kVirtualMachine' HyperV
            objects.
        name (string): Specifies the name of the HyperV Object.
        mtype (Type7Enum): Specifies the type of an HyperV Protection Source
            Object such as 'kSCVMMServer', 'kStandaloneHost', 'kNetwork', etc.
            overrideDescription: true Specifies the type of an HyperV
            Protection Source. 'kSCVMMServer' indicates a collection of root
            folders clusters. 'kStandaloneHost' indicates a single Nutanix
            cluster. 'kStandaloneCluster' indicates a single Nutanix cluster.
            'kHostGroup' indicates a Nutanix cluster manageed by a Prism
            Central. 'kHost' indicates an HyperV host. 'kHostCluster'
            indicates a Nutanix cluster manageed by a Prism Central.
            'kVirtualMachine' indicates a Virtual Machine. 'kNetwork'
            indicates a Virtual Machine network object. 'kDatastore'
            represents a storage container object.
        uuid (string): Specifies the UUID of the Object. This is unique within
            the HyperV environment.
        vm_info (HypervVirtualMachineObject): Specifies information about a
            VirtualMachine Object in HyperV environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agents":'agents',
        "backup_type":'backupType',
        "cluster_name":'clusterName',
        "datastore_info":'datastoreInfo',
        "description":'description',
        "host_type":'hostType',
        "hyperv_uuid":'hypervUuid',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid',
        "vm_info":'vmInfo'
    }

    def __init__(self,
                 agents=None,
                 backup_type=None,
                 cluster_name=None,
                 datastore_info=None,
                 description=None,
                 host_type=None,
                 hyperv_uuid=None,
                 name=None,
                 mtype=None,
                 uuid=None,
                 vm_info=None):
        """Constructor for the HypervProtectionSource class"""

        # Initialize members of the class
        self.agents = agents
        self.backup_type = backup_type
        self.cluster_name = cluster_name
        self.datastore_info = datastore_info
        self.description = description
        self.host_type = host_type
        self.hyperv_uuid = hyperv_uuid
        self.name = name
        self.mtype = mtype
        self.uuid = uuid
        self.vm_info = vm_info


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
        agents = None
        if dictionary.get('agents') != None:
            agents = list()
            for structure in dictionary.get('agents'):
                agents.append(cohesity_management_sdk.models.agent_information.AgentInformation.from_dictionary(structure))
        backup_type = dictionary.get('backupType')
        cluster_name = dictionary.get('clusterName')
        datastore_info = cohesity_management_sdk.models.hyperv_datastore_object.HypervDatastoreObject.from_dictionary(dictionary.get('datastoreInfo')) if dictionary.get('datastoreInfo') else None
        description = dictionary.get('description')
        host_type = dictionary.get('hostType')
        hyperv_uuid = dictionary.get('hypervUuid')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        vm_info = cohesity_management_sdk.models.hyperv_virtual_machine_object.HypervVirtualMachineObject.from_dictionary(dictionary.get('vmInfo')) if dictionary.get('vmInfo') else None

        # Return an object of this model
        return cls(agents,
                   backup_type,
                   cluster_name,
                   datastore_info,
                   description,
                   host_type,
                   hyperv_uuid,
                   name,
                   mtype,
                   uuid,
                   vm_info)


