# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class SrtStatisticSend(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'bytes': 'int',
            'bytes_dropped': 'int',
            'mbit_rate': 'float',
            'packets': 'int',
            'packets_dropped': 'int',
            'packets_lost': 'int',
            'packets_retransmitted': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes': 'bytes',
            'bytes_dropped': 'bytesDropped',
            'mbit_rate': 'mbitRate',
            'packets': 'packets',
            'packets_dropped': 'packetsDropped',
            'packets_lost': 'packetsLost',
            'packets_retransmitted': 'packetsRetransmitted'
        }
        return attributes

    def __init__(self, bytes=None, bytes_dropped=None, mbit_rate=None, packets=None, packets_dropped=None, packets_lost=None, packets_retransmitted=None, *args, **kwargs):

        self._bytes = None
        self._bytes_dropped = None
        self._mbit_rate = None
        self._packets = None
        self._packets_dropped = None
        self._packets_lost = None
        self._packets_retransmitted = None
        self.discriminator = None

        if bytes is not None:
            self.bytes = bytes
        if bytes_dropped is not None:
            self.bytes_dropped = bytes_dropped
        if mbit_rate is not None:
            self.mbit_rate = mbit_rate
        if packets is not None:
            self.packets = packets
        if packets_dropped is not None:
            self.packets_dropped = packets_dropped
        if packets_lost is not None:
            self.packets_lost = packets_lost
        if packets_retransmitted is not None:
            self.packets_retransmitted = packets_retransmitted

    @property
    def bytes(self):
        """Gets the bytes of this SrtStatisticSend.


        :return: The bytes of this SrtStatisticSend.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this SrtStatisticSend.


        :param bytes: The bytes of this SrtStatisticSend.
        :type: int
        """

        if bytes is not None:
            if not isinstance(bytes, int):
                raise TypeError("Invalid type for `bytes`, type has to be `int`")

            self._bytes = bytes


    @property
    def bytes_dropped(self):
        """Gets the bytes_dropped of this SrtStatisticSend.


        :return: The bytes_dropped of this SrtStatisticSend.
        :rtype: int
        """
        return self._bytes_dropped

    @bytes_dropped.setter
    def bytes_dropped(self, bytes_dropped):
        """Sets the bytes_dropped of this SrtStatisticSend.


        :param bytes_dropped: The bytes_dropped of this SrtStatisticSend.
        :type: int
        """

        if bytes_dropped is not None:
            if not isinstance(bytes_dropped, int):
                raise TypeError("Invalid type for `bytes_dropped`, type has to be `int`")

            self._bytes_dropped = bytes_dropped


    @property
    def mbit_rate(self):
        """Gets the mbit_rate of this SrtStatisticSend.


        :return: The mbit_rate of this SrtStatisticSend.
        :rtype: float
        """
        return self._mbit_rate

    @mbit_rate.setter
    def mbit_rate(self, mbit_rate):
        """Sets the mbit_rate of this SrtStatisticSend.


        :param mbit_rate: The mbit_rate of this SrtStatisticSend.
        :type: float
        """

        if mbit_rate is not None:
            if not isinstance(mbit_rate, float):
                raise TypeError("Invalid type for `mbit_rate`, type has to be `float`")

            self._mbit_rate = mbit_rate


    @property
    def packets(self):
        """Gets the packets of this SrtStatisticSend.


        :return: The packets of this SrtStatisticSend.
        :rtype: int
        """
        return self._packets

    @packets.setter
    def packets(self, packets):
        """Sets the packets of this SrtStatisticSend.


        :param packets: The packets of this SrtStatisticSend.
        :type: int
        """

        if packets is not None:
            if not isinstance(packets, int):
                raise TypeError("Invalid type for `packets`, type has to be `int`")

            self._packets = packets


    @property
    def packets_dropped(self):
        """Gets the packets_dropped of this SrtStatisticSend.


        :return: The packets_dropped of this SrtStatisticSend.
        :rtype: int
        """
        return self._packets_dropped

    @packets_dropped.setter
    def packets_dropped(self, packets_dropped):
        """Sets the packets_dropped of this SrtStatisticSend.


        :param packets_dropped: The packets_dropped of this SrtStatisticSend.
        :type: int
        """

        if packets_dropped is not None:
            if not isinstance(packets_dropped, int):
                raise TypeError("Invalid type for `packets_dropped`, type has to be `int`")

            self._packets_dropped = packets_dropped


    @property
    def packets_lost(self):
        """Gets the packets_lost of this SrtStatisticSend.


        :return: The packets_lost of this SrtStatisticSend.
        :rtype: int
        """
        return self._packets_lost

    @packets_lost.setter
    def packets_lost(self, packets_lost):
        """Sets the packets_lost of this SrtStatisticSend.


        :param packets_lost: The packets_lost of this SrtStatisticSend.
        :type: int
        """

        if packets_lost is not None:
            if not isinstance(packets_lost, int):
                raise TypeError("Invalid type for `packets_lost`, type has to be `int`")

            self._packets_lost = packets_lost


    @property
    def packets_retransmitted(self):
        """Gets the packets_retransmitted of this SrtStatisticSend.


        :return: The packets_retransmitted of this SrtStatisticSend.
        :rtype: int
        """
        return self._packets_retransmitted

    @packets_retransmitted.setter
    def packets_retransmitted(self, packets_retransmitted):
        """Sets the packets_retransmitted of this SrtStatisticSend.


        :param packets_retransmitted: The packets_retransmitted of this SrtStatisticSend.
        :type: int
        """

        if packets_retransmitted is not None:
            if not isinstance(packets_retransmitted, int):
                raise TypeError("Invalid type for `packets_retransmitted`, type has to be `int`")

            self._packets_retransmitted = packets_retransmitted

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(SrtStatisticSend, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SrtStatisticSend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
