import connexion
import six

from autohubcompany.models.cart_body import CartBody  # noqa: E501
from autohubcompany.models.order_body import OrderBody  # noqa: E501
from autohubcompany.models.order_body_updated_cart import OrderBodyUpdatedCart  # noqa: E501
from autohubcompany.models.product import Product  # noqa: E501
from autohubcompany import util
from autohubcompany.business_logic import BusinessLogic

bl = BusinessLogic()

def create_users(body):
    return bl.add_users(body)

def cart_delete(cart_id):  # noqa: E501
    """Remove an entry from the shopping cart.

     # noqa: E501

    :param cart_id: 
    :type cart_id: int

    :rtype: None
    """
    return bl.remove_user_cart(cart_id)


def cart_get(user_id):  # noqa: E501
    """Get the items in the shopping cart.

     # noqa: E501

    :param user_id: 
    :type user_id: int

    :rtype: None
    """
    return bl.get_products_from_cart(user_id)


def cart_patch(body):  # noqa: E501
    """Update the quantity of a product in the cart.

    This endpoint allows you to update the quantity of a product in the user&#x27;s cart. # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [OrderBodyUpdatedCart.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        return bl.update_product_quantity_to_cart(body)


def cart_post(body):  # noqa: E501
    """Add a product to the shopping cart.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CartBody.from_dict(connexion.request.get_json())  # noqa: E501
        return bl.add_product_to_cart(body)


def order_post(body):  # noqa: E501
    """Place an order for the products in the shopping cart.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = OrderBody.from_dict(connexion.request.get_json())  # noqa: E501
        return bl.place_an_order(body)


def products_get():  # noqa: E501
    """Get an overview of all available products.

     # noqa: E501


    :rtype: None
    """
    return bl.get_products_from_store()


def products_post(body):  # noqa: E501
    """Add one or more products to the database.

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Product.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        return bl.add_products_to_store(body)


def products_product_id_get(product_id):  # noqa: E501
    """Get details of a specific product.

     # noqa: E501

    :param product_id: 
    :type product_id: int

    :rtype: None
    """
    return bl.get_product_from_store(product_id)
