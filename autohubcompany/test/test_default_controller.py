# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from autohubcompany.models.cart_body import CartBody  # noqa: E501
from autohubcompany.models.order_body import OrderBody  # noqa: E501
from autohubcompany.models.order_body_updated_cart import OrderBodyUpdatedCart  # noqa: E501
from autohubcompany.models.product import Product  # noqa: E501
from autohubcompany.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_cart_delete(self):
        """Test case for cart_delete

        Remove an entry from the shopping cart.
        """
        query_string = [('cart_id', 56)]
        response = self.client.open(
            '/cart',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cart_get(self):
        """Test case for cart_get

        Get the items in the shopping cart.
        """
        query_string = [('user_id', 56)]
        response = self.client.open(
            '/cart',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cart_patch(self):
        """Test case for cart_patch

        Update the quantity of a product in the cart.
        """
        body = [OrderBodyUpdatedCart()]
        response = self.client.open(
            '/cart',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cart_post(self):
        """Test case for cart_post

        Add a product to the shopping cart.
        """
        body = CartBody()
        response = self.client.open(
            '/cart',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_post(self):
        """Test case for order_post

        Place an order for the products in the shopping cart.
        """
        body = OrderBody()
        response = self.client.open(
            '/order',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_get(self):
        """Test case for products_get

        Get an overview of all available products.
        """
        response = self.client.open(
            '/products',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_post(self):
        """Test case for products_post

        Add one or more products to the database.
        """
        body = [Product()]
        response = self.client.open(
            '/products',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_get(self):
        """Test case for products_product_id_get

        Get details of a specific product.
        """
        response = self.client.open(
            '/products/{product_id}'.format(product_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
