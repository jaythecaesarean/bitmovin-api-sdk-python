# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class AnalyticsLicenseDomain(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 url=None):
        # type: (string_types, string_types) -> None
        super(AnalyticsLicenseDomain, self).__init__(id_=id_)

        self._url = None
        self.discriminator = None

        if url is not None:
            self.url = url

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsLicenseDomain, self), 'openapi_types'):
            types = getattr(super(AnalyticsLicenseDomain, self), 'openapi_types')

        types.update({
            'url': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsLicenseDomain, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsLicenseDomain, self), 'attribute_map')

        attributes.update({
            'url': 'url'
        })
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this AnalyticsLicenseDomain.


        :return: The url of this AnalyticsLicenseDomain.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this AnalyticsLicenseDomain.


        :param url: The url of this AnalyticsLicenseDomain.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsLicenseDomain, self), "to_dict"):
            result = super(AnalyticsLicenseDomain, self).to_dict()
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
        if not isinstance(other, AnalyticsLicenseDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
