# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class SQLEnvironmentJobParameters(object):

    """Implementation of the 'SQL Environment Job Parameters.' model.

    Specifies job parameters applicable for all 'kSQL' Environment type
    Protection Sources in a Protection Job.

    Attributes:
        aag_preference (AagPreferenceEnum): Specifies the preference for
            backing up databases that are part of an AAG. Only applicable if
            'aagPreferenceFromSqlServer' is set to false or not given.
            kPrimaryReplicaOnly implies backups should always occur on the
            primary replica. kSecondaryReplicaOnly implies backups should
            always occur on the secondary replica. kPreferSecondaryReplica
            implies secondary replica is preferred for backups. kAnyReplica
            implies no preference of about whether backups are performed on
            the primary replica or on a secondary replica. If no secondary
            replica is available, then performing backups on the primary
            replica is acceptable.
        aag_preference_from_sql_server (bool): If true, AAG preferences are
            taken from the SQL server host. If this is set to false or not
            given, preferences can be overridden by aagBackupPreference.
        backup_system_databases (bool): If true, system databases are backed
            up. If this is set to false, system databases are not backed up.
            If this field is not specified, default value is true.
        backup_type (BackupType1Enum): Specifies the type of the 'kFull'
            backup job. Specifies whether it is Volume level backup or
            individual files level backup. kSqlVSSVolume implies volume based
            VSS full backup. kSqlVSSFile implies file based VSS full backup.
        backup_volumes_only (bool): If set to true, only the volumes
            associated with databases should be backed up. The user cannot
            select additional volumes at host level for backup.  If set to
            false, all the volumes on the host machine will be backed up. In
            this case, the user can further select the exact set of volumes
            using host level params.  Note that the volumes associated with
            selected databases will always be included in the backup.
        is_copy_only_full (bool): If true, the backup is a full backup with
            the copy-only option specified.
        user_database_preference (UserDatabasePreferenceEnum): Specifies the
            preference for backing up user databases on the host.
            kBackupAllDatabases implies to backup all databases.
            kBackupAllExceptAAGDatabases implies not to backup AAG databases.
            kBackupOnlyAAGDatabases implies to backup only AAG databases.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aag_preference":'aagPreference',
        "aag_preference_from_sql_server":'aagPreferenceFromSqlServer',
        "backup_system_databases":'backupSystemDatabases',
        "backup_type":'backupType',
        "backup_volumes_only":'backupVolumesOnly',
        "is_copy_only_full":'isCopyOnlyFull',
        "user_database_preference":'userDatabasePreference'
    }

    def __init__(self,
                 aag_preference=None,
                 aag_preference_from_sql_server=None,
                 backup_system_databases=None,
                 backup_type=None,
                 backup_volumes_only=None,
                 is_copy_only_full=None,
                 user_database_preference=None):
        """Constructor for the SQLEnvironmentJobParameters class"""

        # Initialize members of the class
        self.aag_preference = aag_preference
        self.aag_preference_from_sql_server = aag_preference_from_sql_server
        self.backup_system_databases = backup_system_databases
        self.backup_type = backup_type
        self.backup_volumes_only = backup_volumes_only
        self.is_copy_only_full = is_copy_only_full
        self.user_database_preference = user_database_preference


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
        aag_preference = dictionary.get('aagPreference')
        aag_preference_from_sql_server = dictionary.get('aagPreferenceFromSqlServer')
        backup_system_databases = dictionary.get('backupSystemDatabases')
        backup_type = dictionary.get('backupType')
        backup_volumes_only = dictionary.get('backupVolumesOnly')
        is_copy_only_full = dictionary.get('isCopyOnlyFull')
        user_database_preference = dictionary.get('userDatabasePreference')

        # Return an object of this model
        return cls(aag_preference,
                   aag_preference_from_sql_server,
                   backup_system_databases,
                   backup_type,
                   backup_volumes_only,
                   is_copy_only_full,
                   user_database_preference)


