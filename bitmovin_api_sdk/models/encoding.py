# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.encoding_type import EncodingType
from bitmovin_api_sdk.models.infrastructure_settings import InfrastructureSettings
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class Encoding(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None,
                 started_at=None,
                 queued_at=None,
                 running_at=None,
                 finished_at=None,
                 error_at=None,
                 progress=None,
                 cloud_region=None,
                 fallback_cloud_regions=None,
                 encoder_version=None,
                 infrastructure_id=None,
                 infrastructure=None,
                 selected_encoder_version=None,
                 selected_encoding_mode=None,
                 selected_cloud_region=None,
                 status=None,
                 labels=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, EncodingType, datetime, datetime, datetime, datetime, datetime, int, CloudRegion, list[CloudRegion], string_types, string_types, InfrastructureSettings, string_types, EncodingMode, CloudRegion, Status, list[string_types]) -> None
        super(Encoding, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._type = None
        self._started_at = None
        self._queued_at = None
        self._running_at = None
        self._finished_at = None
        self._error_at = None
        self._progress = None
        self._cloud_region = None
        self._fallback_cloud_regions = list()
        self._encoder_version = None
        self._infrastructure_id = None
        self._infrastructure = None
        self._selected_encoder_version = None
        self._selected_encoding_mode = None
        self._selected_cloud_region = None
        self._status = None
        self._labels = list()
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if started_at is not None:
            self.started_at = started_at
        if queued_at is not None:
            self.queued_at = queued_at
        if running_at is not None:
            self.running_at = running_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_at is not None:
            self.error_at = error_at
        if progress is not None:
            self.progress = progress
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if fallback_cloud_regions is not None:
            self.fallback_cloud_regions = fallback_cloud_regions
        if encoder_version is not None:
            self.encoder_version = encoder_version
        if infrastructure_id is not None:
            self.infrastructure_id = infrastructure_id
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if selected_encoder_version is not None:
            self.selected_encoder_version = selected_encoder_version
        if selected_encoding_mode is not None:
            self.selected_encoding_mode = selected_encoding_mode
        if selected_cloud_region is not None:
            self.selected_cloud_region = selected_cloud_region
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Encoding, self), 'openapi_types'):
            types = getattr(super(Encoding, self), 'openapi_types')

        types.update({
            'type': 'EncodingType',
            'started_at': 'datetime',
            'queued_at': 'datetime',
            'running_at': 'datetime',
            'finished_at': 'datetime',
            'error_at': 'datetime',
            'progress': 'int',
            'cloud_region': 'CloudRegion',
            'fallback_cloud_regions': 'list[CloudRegion]',
            'encoder_version': 'string_types',
            'infrastructure_id': 'string_types',
            'infrastructure': 'InfrastructureSettings',
            'selected_encoder_version': 'string_types',
            'selected_encoding_mode': 'EncodingMode',
            'selected_cloud_region': 'CloudRegion',
            'status': 'Status',
            'labels': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Encoding, self), 'attribute_map'):
            attributes = getattr(super(Encoding, self), 'attribute_map')

        attributes.update({
            'type': 'type',
            'started_at': 'startedAt',
            'queued_at': 'queuedAt',
            'running_at': 'runningAt',
            'finished_at': 'finishedAt',
            'error_at': 'errorAt',
            'progress': 'progress',
            'cloud_region': 'cloudRegion',
            'fallback_cloud_regions': 'fallbackCloudRegions',
            'encoder_version': 'encoderVersion',
            'infrastructure_id': 'infrastructureId',
            'infrastructure': 'infrastructure',
            'selected_encoder_version': 'selectedEncoderVersion',
            'selected_encoding_mode': 'selectedEncodingMode',
            'selected_cloud_region': 'selectedCloudRegion',
            'status': 'status',
            'labels': 'labels'
        })
        return attributes

    @property
    def type(self):
        # type: () -> EncodingType
        """Gets the type of this Encoding.

        Type of the encoding

        :return: The type of this Encoding.
        :rtype: EncodingType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (EncodingType) -> None
        """Sets the type of this Encoding.

        Type of the encoding

        :param type_: The type of this Encoding.
        :type: EncodingType
        """

        if type_ is not None:
            if not isinstance(type_, EncodingType):
                raise TypeError("Invalid type for `type`, type has to be `EncodingType`")

        self._type = type_

    @property
    def started_at(self):
        # type: () -> datetime
        """Gets the started_at of this Encoding.

        Timestamp when the encoding was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The started_at of this Encoding.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        # type: (datetime) -> None
        """Sets the started_at of this Encoding.

        Timestamp when the encoding was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param started_at: The started_at of this Encoding.
        :type: datetime
        """

        if started_at is not None:
            if not isinstance(started_at, datetime):
                raise TypeError("Invalid type for `started_at`, type has to be `datetime`")

        self._started_at = started_at

    @property
    def queued_at(self):
        # type: () -> datetime
        """Gets the queued_at of this Encoding.

        Timestamp when the encoding status changed to \"QUEUED\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The queued_at of this Encoding.
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        # type: (datetime) -> None
        """Sets the queued_at of this Encoding.

        Timestamp when the encoding status changed to \"QUEUED\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param queued_at: The queued_at of this Encoding.
        :type: datetime
        """

        if queued_at is not None:
            if not isinstance(queued_at, datetime):
                raise TypeError("Invalid type for `queued_at`, type has to be `datetime`")

        self._queued_at = queued_at

    @property
    def running_at(self):
        # type: () -> datetime
        """Gets the running_at of this Encoding.

        Timestamp when the encoding status changed to to \"RUNNING\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The running_at of this Encoding.
        :rtype: datetime
        """
        return self._running_at

    @running_at.setter
    def running_at(self, running_at):
        # type: (datetime) -> None
        """Sets the running_at of this Encoding.

        Timestamp when the encoding status changed to to \"RUNNING\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param running_at: The running_at of this Encoding.
        :type: datetime
        """

        if running_at is not None:
            if not isinstance(running_at, datetime):
                raise TypeError("Invalid type for `running_at`, type has to be `datetime`")

        self._running_at = running_at

    @property
    def finished_at(self):
        # type: () -> datetime
        """Gets the finished_at of this Encoding.

        Timestamp when the encoding status changed to \"FINISHED\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The finished_at of this Encoding.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        # type: (datetime) -> None
        """Sets the finished_at of this Encoding.

        Timestamp when the encoding status changed to \"FINISHED\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param finished_at: The finished_at of this Encoding.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

        self._finished_at = finished_at

    @property
    def error_at(self):
        # type: () -> datetime
        """Gets the error_at of this Encoding.

        Timestamp when the encoding status changed to \"ERROR\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The error_at of this Encoding.
        :rtype: datetime
        """
        return self._error_at

    @error_at.setter
    def error_at(self, error_at):
        # type: (datetime) -> None
        """Sets the error_at of this Encoding.

        Timestamp when the encoding status changed to \"ERROR\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param error_at: The error_at of this Encoding.
        :type: datetime
        """

        if error_at is not None:
            if not isinstance(error_at, datetime):
                raise TypeError("Invalid type for `error_at`, type has to be `datetime`")

        self._error_at = error_at

    @property
    def progress(self):
        # type: () -> int
        """Gets the progress of this Encoding.

        Progress of the encoding in percent

        :return: The progress of this Encoding.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        # type: (int) -> None
        """Sets the progress of this Encoding.

        Progress of the encoding in percent

        :param progress: The progress of this Encoding.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

        self._progress = progress

    @property
    def cloud_region(self):
        # type: () -> CloudRegion
        """Gets the cloud_region of this Encoding.


        :return: The cloud_region of this Encoding.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (CloudRegion) -> None
        """Sets the cloud_region of this Encoding.


        :param cloud_region: The cloud_region of this Encoding.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

        self._cloud_region = cloud_region

    @property
    def fallback_cloud_regions(self):
        # type: () -> list[CloudRegion]
        """Gets the fallback_cloud_regions of this Encoding.

        Specify a list of regions which are used in case the preferred region is down. Currently there are several restrictions. - The region has to be specific or AUTO - The region has to be for the same cloud provider as the default one - You can only configure at most 3 fallback regions 

        :return: The fallback_cloud_regions of this Encoding.
        :rtype: list[CloudRegion]
        """
        return self._fallback_cloud_regions

    @fallback_cloud_regions.setter
    def fallback_cloud_regions(self, fallback_cloud_regions):
        # type: (list) -> None
        """Sets the fallback_cloud_regions of this Encoding.

        Specify a list of regions which are used in case the preferred region is down. Currently there are several restrictions. - The region has to be specific or AUTO - The region has to be for the same cloud provider as the default one - You can only configure at most 3 fallback regions 

        :param fallback_cloud_regions: The fallback_cloud_regions of this Encoding.
        :type: list[CloudRegion]
        """

        if fallback_cloud_regions is not None:
            if not isinstance(fallback_cloud_regions, list):
                raise TypeError("Invalid type for `fallback_cloud_regions`, type has to be `list[CloudRegion]`")

        self._fallback_cloud_regions = fallback_cloud_regions

    @property
    def encoder_version(self):
        # type: () -> string_types
        """Gets the encoder_version of this Encoding.

        Version of the encoder

        :return: The encoder_version of this Encoding.
        :rtype: string_types
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        # type: (string_types) -> None
        """Sets the encoder_version of this Encoding.

        Version of the encoder

        :param encoder_version: The encoder_version of this Encoding.
        :type: string_types
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, string_types):
                raise TypeError("Invalid type for `encoder_version`, type has to be `string_types`")

        self._encoder_version = encoder_version

    @property
    def infrastructure_id(self):
        # type: () -> string_types
        """Gets the infrastructure_id of this Encoding.

        Define an external infrastructure to run the encoding on. Note If you set this value, the `cloudRegion` must be 'EXTERNAL'.

        :return: The infrastructure_id of this Encoding.
        :rtype: string_types
        """
        return self._infrastructure_id

    @infrastructure_id.setter
    def infrastructure_id(self, infrastructure_id):
        # type: (string_types) -> None
        """Sets the infrastructure_id of this Encoding.

        Define an external infrastructure to run the encoding on. Note If you set this value, the `cloudRegion` must be 'EXTERNAL'.

        :param infrastructure_id: The infrastructure_id of this Encoding.
        :type: string_types
        """

        if infrastructure_id is not None:
            if not isinstance(infrastructure_id, string_types):
                raise TypeError("Invalid type for `infrastructure_id`, type has to be `string_types`")

        self._infrastructure_id = infrastructure_id

    @property
    def infrastructure(self):
        # type: () -> InfrastructureSettings
        """Gets the infrastructure of this Encoding.


        :return: The infrastructure of this Encoding.
        :rtype: InfrastructureSettings
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        # type: (InfrastructureSettings) -> None
        """Sets the infrastructure of this Encoding.


        :param infrastructure: The infrastructure of this Encoding.
        :type: InfrastructureSettings
        """

        if infrastructure is not None:
            if not isinstance(infrastructure, InfrastructureSettings):
                raise TypeError("Invalid type for `infrastructure`, type has to be `InfrastructureSettings`")

        self._infrastructure = infrastructure

    @property
    def selected_encoder_version(self):
        # type: () -> string_types
        """Gets the selected_encoder_version of this Encoding.

        Will be set to the encoder version that was actually used for the encoding. This is especially useful when starting an encoding with a version tag like STABLE or BETA.

        :return: The selected_encoder_version of this Encoding.
        :rtype: string_types
        """
        return self._selected_encoder_version

    @selected_encoder_version.setter
    def selected_encoder_version(self, selected_encoder_version):
        # type: (string_types) -> None
        """Sets the selected_encoder_version of this Encoding.

        Will be set to the encoder version that was actually used for the encoding. This is especially useful when starting an encoding with a version tag like STABLE or BETA.

        :param selected_encoder_version: The selected_encoder_version of this Encoding.
        :type: string_types
        """

        if selected_encoder_version is not None:
            if not isinstance(selected_encoder_version, string_types):
                raise TypeError("Invalid type for `selected_encoder_version`, type has to be `string_types`")

        self._selected_encoder_version = selected_encoder_version

    @property
    def selected_encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the selected_encoding_mode of this Encoding.

        Will be set to the encoding mode that was actually used for the encoding. This is especially useful when starting an encoding with encoding mode STANDARD.

        :return: The selected_encoding_mode of this Encoding.
        :rtype: EncodingMode
        """
        return self._selected_encoding_mode

    @selected_encoding_mode.setter
    def selected_encoding_mode(self, selected_encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the selected_encoding_mode of this Encoding.

        Will be set to the encoding mode that was actually used for the encoding. This is especially useful when starting an encoding with encoding mode STANDARD.

        :param selected_encoding_mode: The selected_encoding_mode of this Encoding.
        :type: EncodingMode
        """

        if selected_encoding_mode is not None:
            if not isinstance(selected_encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `selected_encoding_mode`, type has to be `EncodingMode`")

        self._selected_encoding_mode = selected_encoding_mode

    @property
    def selected_cloud_region(self):
        # type: () -> CloudRegion
        """Gets the selected_cloud_region of this Encoding.

        Contains the region which was selected when cloudregion:AUTO was specified

        :return: The selected_cloud_region of this Encoding.
        :rtype: CloudRegion
        """
        return self._selected_cloud_region

    @selected_cloud_region.setter
    def selected_cloud_region(self, selected_cloud_region):
        # type: (CloudRegion) -> None
        """Sets the selected_cloud_region of this Encoding.

        Contains the region which was selected when cloudregion:AUTO was specified

        :param selected_cloud_region: The selected_cloud_region of this Encoding.
        :type: CloudRegion
        """

        if selected_cloud_region is not None:
            if not isinstance(selected_cloud_region, CloudRegion):
                raise TypeError("Invalid type for `selected_cloud_region`, type has to be `CloudRegion`")

        self._selected_cloud_region = selected_cloud_region

    @property
    def status(self):
        # type: () -> Status
        """Gets the status of this Encoding.

        The current status of the encoding.

        :return: The status of this Encoding.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Status) -> None
        """Sets the status of this Encoding.

        The current status of the encoding.

        :param status: The status of this Encoding.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

        self._status = status

    @property
    def labels(self):
        # type: () -> list[string_types]
        """Gets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :return: The labels of this Encoding.
        :rtype: list[string_types]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        # type: (list) -> None
        """Sets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :param labels: The labels of this Encoding.
        :type: list[string_types]
        """

        if labels is not None:
            if not isinstance(labels, list):
                raise TypeError("Invalid type for `labels`, type has to be `list[string_types]`")

        self._labels = labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Encoding, self), "to_dict"):
            result = super(Encoding, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Encoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
