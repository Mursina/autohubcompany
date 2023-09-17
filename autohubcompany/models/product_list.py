# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from autohubcompany.models.base_model_ import Model
from autohubcompany.models.product import Product  # noqa: F401,E501
from autohubcompany import util


class ProductList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """ProductList - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ProductList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProductList of this ProductList.  # noqa: E501
        :rtype: ProductList
        """
        return util.deserialize_model(dikt, cls)