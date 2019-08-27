# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.hls_version import HlsVersion
from bitmovin_api_sdk.models.manifest import Manifest
from bitmovin_api_sdk.models.manifest_type import ManifestType
import pprint
import six


class HlsManifest(Manifest):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 type_=None,
                 outputs=None,
                 manifest_name=None,
                 hls_media_playlist_version=None,
                 hls_master_playlist_version=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, ManifestType, list[EncodingOutput], string_types, HlsVersion, HlsVersion) -> None
        super(HlsManifest, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, type_=type_, outputs=outputs)

        self._manifest_name = None
        self._hls_media_playlist_version = None
        self._hls_master_playlist_version = None
        self.discriminator = None

        if manifest_name is not None:
            self.manifest_name = manifest_name
        if hls_media_playlist_version is not None:
            self.hls_media_playlist_version = hls_media_playlist_version
        if hls_master_playlist_version is not None:
            self.hls_master_playlist_version = hls_master_playlist_version

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(HlsManifest, self), 'openapi_types'):
            types = getattr(super(HlsManifest, self), 'openapi_types')

        types.update({
            'manifest_name': 'string_types',
            'hls_media_playlist_version': 'HlsVersion',
            'hls_master_playlist_version': 'HlsVersion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(HlsManifest, self), 'attribute_map'):
            attributes = getattr(super(HlsManifest, self), 'attribute_map')

        attributes.update({
            'manifest_name': 'manifestName',
            'hls_media_playlist_version': 'hlsMediaPlaylistVersion',
            'hls_master_playlist_version': 'hlsMasterPlaylistVersion'
        })
        return attributes

    @property
    def manifest_name(self):
        # type: () -> string_types
        """Gets the manifest_name of this HlsManifest.

        The filename of your manifest (required)

        :return: The manifest_name of this HlsManifest.
        :rtype: string_types
        """
        return self._manifest_name

    @manifest_name.setter
    def manifest_name(self, manifest_name):
        # type: (string_types) -> None
        """Sets the manifest_name of this HlsManifest.

        The filename of your manifest (required)

        :param manifest_name: The manifest_name of this HlsManifest.
        :type: string_types
        """

        if manifest_name is not None:
            if not isinstance(manifest_name, string_types):
                raise TypeError("Invalid type for `manifest_name`, type has to be `string_types`")

        self._manifest_name = manifest_name

    @property
    def hls_media_playlist_version(self):
        # type: () -> HlsVersion
        """Gets the hls_media_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tags of the Media Playlists are set to the provided version

        :return: The hls_media_playlist_version of this HlsManifest.
        :rtype: HlsVersion
        """
        return self._hls_media_playlist_version

    @hls_media_playlist_version.setter
    def hls_media_playlist_version(self, hls_media_playlist_version):
        # type: (HlsVersion) -> None
        """Sets the hls_media_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tags of the Media Playlists are set to the provided version

        :param hls_media_playlist_version: The hls_media_playlist_version of this HlsManifest.
        :type: HlsVersion
        """

        if hls_media_playlist_version is not None:
            if not isinstance(hls_media_playlist_version, HlsVersion):
                raise TypeError("Invalid type for `hls_media_playlist_version`, type has to be `HlsVersion`")

        self._hls_media_playlist_version = hls_media_playlist_version

    @property
    def hls_master_playlist_version(self):
        # type: () -> HlsVersion
        """Gets the hls_master_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tag of the Master Playlist is set to the provided version

        :return: The hls_master_playlist_version of this HlsManifest.
        :rtype: HlsVersion
        """
        return self._hls_master_playlist_version

    @hls_master_playlist_version.setter
    def hls_master_playlist_version(self, hls_master_playlist_version):
        # type: (HlsVersion) -> None
        """Sets the hls_master_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tag of the Master Playlist is set to the provided version

        :param hls_master_playlist_version: The hls_master_playlist_version of this HlsManifest.
        :type: HlsVersion
        """

        if hls_master_playlist_version is not None:
            if not isinstance(hls_master_playlist_version, HlsVersion):
                raise TypeError("Invalid type for `hls_master_playlist_version`, type has to be `HlsVersion`")

        self._hls_master_playlist_version = hls_master_playlist_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(HlsManifest, self), "to_dict"):
            result = super(HlsManifest, self).to_dict()
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
        if not isinstance(other, HlsManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
