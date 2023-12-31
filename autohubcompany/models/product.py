# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from autohubcompany.models.base_model_ import Model
from autohubcompany import util


class Product(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, part_id: int=None, name: str=None, price: float=None, brand: str=None, compatibility: str=None, quantity: int=None, category: str=None):  # noqa: E501
        """Product - a model defined in Swagger

        :param part_id: The part_id of this Product.  # noqa: E501
        :type part_id: int
        :param name: The name of this Product.  # noqa: E501
        :type name: str
        :param price: The price of this Product.  # noqa: E501
        :type price: float
        :param brand: The brand of this Product.  # noqa: E501
        :type brand: str
        :param compatibility: The compatibility of this Product.  # noqa: E501
        :type compatibility: str
        :param quantity: The quantity of this Product.  # noqa: E501
        :type quantity: int
        :param category: The category of this Product.  # noqa: E501
        :type category: str
        """
        self.swagger_types = {
            'part_id': int,
            'name': str,
            'price': float,
            'brand': str,
            'compatibility': str,
            'quantity': int,
            'category': str
        }

        self.attribute_map = {
            'part_id': 'part_id',
            'name': 'name',
            'price': 'price',
            'brand': 'brand',
            'compatibility': 'compatibility',
            'quantity': 'quantity',
            'category': 'category'
        }
        self._part_id = part_id
        self._name = name
        self._price = price
        self._brand = brand
        self._compatibility = compatibility
        self._quantity = quantity
        self._category = category

    @classmethod
    def from_dict(cls, dikt) -> 'Product':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Product of this Product.  # noqa: E501
        :rtype: Product
        """
        return util.deserialize_model(dikt, cls)

    @property
    def part_id(self) -> int:
        """Gets the part_id of this Product.


        :return: The part_id of this Product.
        :rtype: int
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id: int):
        """Sets the part_id of this Product.


        :param part_id: The part_id of this Product.
        :type part_id: int
        """

        self._part_id = part_id

    @property
    def name(self) -> str:
        """Gets the name of this Product.


        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product.


        :param name: The name of this Product.
        :type name: str
        """

        self._name = name

    @property
    def price(self) -> float:
        """Gets the price of this Product.


        :return: The price of this Product.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float):
        """Sets the price of this Product.


        :param price: The price of this Product.
        :type price: float
        """

        self._price = price

    @property
    def brand(self) -> str:
        """Gets the brand of this Product.


        :return: The brand of this Product.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        """Sets the brand of this Product.


        :param brand: The brand of this Product.
        :type brand: str
        """

        self._brand = brand

    @property
    def compatibility(self) -> str:
        """Gets the compatibility of this Product.


        :return: The compatibility of this Product.
        :rtype: str
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility: str):
        """Sets the compatibility of this Product.


        :param compatibility: The compatibility of this Product.
        :type compatibility: str
        """

        self._compatibility = compatibility

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Product.


        :return: The quantity of this Product.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Product.


        :param quantity: The quantity of this Product.
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def category(self) -> str:
        """Gets the category of this Product.


        :return: The category of this Product.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this Product.


        :param category: The category of this Product.
        :type category: str
        """

        self._category = category
