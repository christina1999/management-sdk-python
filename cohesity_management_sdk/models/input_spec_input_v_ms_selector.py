# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.input_spec_file_time_filter

class InputSpecInputVMsSelector(object):

    """Implementation of the 'InputSpec_InputVMsSelector' model.

    TODO: type model description here.

    Attributes:
        file_time_filter (InputSpecFileTimeFilter): File time filter to filter
            files based on their last change time. All files whose change time
            is in the range [change_time_range_start_secs,
            change_time_range_end_secs) will be processed. Both values are
            time duration in seconds w.r.t. to current time and not absolute
            points in time.
        filename_glob (list of string): After VMDKs are selected as above, the
            files within them can be selected by using these predicates.
        job_ids (list of long|int): TODO: type description here.
        max_snapshot_timestamp (long|int): Exclusive end of snapshot_timestamp
            range. If missing, inf will be used as the timestamp range.
        min_snapshot_timestamp (long|int): Inclusive. If missing, 0 will the
            default lower end of timestamp range
        partition_ids (list of long|int): Filters are AND of ORs.
        process_latest_only (bool): Boolean flag to indicate if only latest
            snapshot of each object should be processed.
        root_dir (string): Within each volume, traversal will be rooted at
            this directory. A typical value here might be /home
        source_entity_ids (list of long|int): TODO: type description here.
        view_box_ids (list of long|int): TODO: type description here.
        view_names (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_time_filter":'fileTimeFilter',
        "filename_glob":'filenameGlob',
        "job_ids":'jobIds',
        "max_snapshot_timestamp":'maxSnapshotTimestamp',
        "min_snapshot_timestamp":'minSnapshotTimestamp',
        "partition_ids":'partitionIds',
        "process_latest_only":'processLatestOnly',
        "root_dir":'rootDir',
        "source_entity_ids":'sourceEntityIds',
        "view_box_ids":'viewBoxIds',
        "view_names":'viewNames'
    }

    def __init__(self,
                 file_time_filter=None,
                 filename_glob=None,
                 job_ids=None,
                 max_snapshot_timestamp=None,
                 min_snapshot_timestamp=None,
                 partition_ids=None,
                 process_latest_only=None,
                 root_dir=None,
                 source_entity_ids=None,
                 view_box_ids=None,
                 view_names=None):
        """Constructor for the InputSpecInputVMsSelector class"""

        # Initialize members of the class
        self.file_time_filter = file_time_filter
        self.filename_glob = filename_glob
        self.job_ids = job_ids
        self.max_snapshot_timestamp = max_snapshot_timestamp
        self.min_snapshot_timestamp = min_snapshot_timestamp
        self.partition_ids = partition_ids
        self.process_latest_only = process_latest_only
        self.root_dir = root_dir
        self.source_entity_ids = source_entity_ids
        self.view_box_ids = view_box_ids
        self.view_names = view_names


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
        file_time_filter = cohesity_management_sdk.models.input_spec_file_time_filter.InputSpecFileTimeFilter.from_dictionary(dictionary.get('fileTimeFilter')) if dictionary.get('fileTimeFilter') else None
        filename_glob = dictionary.get('filenameGlob')
        job_ids = dictionary.get('jobIds')
        max_snapshot_timestamp = dictionary.get('maxSnapshotTimestamp')
        min_snapshot_timestamp = dictionary.get('minSnapshotTimestamp')
        partition_ids = dictionary.get('partitionIds')
        process_latest_only = dictionary.get('processLatestOnly')
        root_dir = dictionary.get('rootDir')
        source_entity_ids = dictionary.get('sourceEntityIds')
        view_box_ids = dictionary.get('viewBoxIds')
        view_names = dictionary.get('viewNames')

        # Return an object of this model
        return cls(file_time_filter,
                   filename_glob,
                   job_ids,
                   max_snapshot_timestamp,
                   min_snapshot_timestamp,
                   partition_ids,
                   process_latest_only,
                   root_dir,
                   source_entity_ids,
                   view_box_ids,
                   view_names)


