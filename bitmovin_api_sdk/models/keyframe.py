# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class Keyframe(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 time=None,
                 segment_cut=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, float, bool) -> None
        super(Keyframe, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._time = None
        self._segment_cut = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if segment_cut is not None:
            self.segment_cut = segment_cut

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Keyframe, self), 'openapi_types'):
            types = getattr(super(Keyframe, self), 'openapi_types')

        types.update({
            'time': 'float',
            'segment_cut': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Keyframe, self), 'attribute_map'):
            attributes = getattr(super(Keyframe, self), 'attribute_map')

        attributes.update({
            'time': 'time',
            'segment_cut': 'segmentCut'
        })
        return attributes

    @property
    def time(self):
        # type: () -> float
        """Gets the time of this Keyframe.

        Time in seconds where the keyframe should be inserted (required)

        :return: The time of this Keyframe.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (float) -> None
        """Sets the time of this Keyframe.

        Time in seconds where the keyframe should be inserted (required)

        :param time: The time of this Keyframe.
        :type: float
        """

        if time is not None:
            if not isinstance(time, (float, int)):
                raise TypeError("Invalid type for `time`, type has to be `float`")

        self._time = time

    @property
    def segment_cut(self):
        # type: () -> bool
        """Gets the segment_cut of this Keyframe.

        Instructs the encoder to cut the segment at this position

        :return: The segment_cut of this Keyframe.
        :rtype: bool
        """
        return self._segment_cut

    @segment_cut.setter
    def segment_cut(self, segment_cut):
        # type: (bool) -> None
        """Sets the segment_cut of this Keyframe.

        Instructs the encoder to cut the segment at this position

        :param segment_cut: The segment_cut of this Keyframe.
        :type: bool
        """

        if segment_cut is not None:
            if not isinstance(segment_cut, bool):
                raise TypeError("Invalid type for `segment_cut`, type has to be `bool`")

        self._segment_cut = segment_cut

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Keyframe, self), "to_dict"):
            result = super(Keyframe, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
        if not isinstance(other, Keyframe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
