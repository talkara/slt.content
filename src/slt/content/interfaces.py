from collective.behavior.discount.interfaces import IDiscount
from collective.cart.shopping.interfaces import IArticle as IBaseArticle
from collective.cart.shopping.interfaces import IOrder as IBaseOrder
from slt.content.schema import ArticleSchema
from slt.content.schema import DiscountBehaviorSchema
from slt.content.schema import MemberAreaSchema
from zope.interface import Attribute
from zope.interface import Interface


# Marker

class IFeedToShopTop(Interface):
    """A marker interface for feed to shop top page."""


# Content type

class IMemberArea(MemberAreaSchema):
    """Interface for content type: slt.content.MemeberArea"""


class IArticle(ArticleSchema, IBaseArticle):
    """Interface for content type: collective.cart.core.Article"""


class IOrder(IBaseOrder):
    """Interface for content type: collective.cart.core.Order"""

    registration_number = Attribute('Registration number for the purchaser')
    birth_date = Attribute('Birth date of the purchaser')
    use_verkkolasku = Attribute('True if use Verkkolasku else False')
    verkkolasku_operator = Attribute('Verkkomaksu operator')
    verkkolasku_account = Attribute('Account of intermediator')


# Deprecated

ICart = IOrder


# Adapter

class IMember(Interface):
    """Adapter interface for member related"""

    def area():
        """Returns content type: slt.content.MemberArea

        :rtype: slt.content.MemberArea
        """

    def default_billing_info():
        """Returns brain of default billing info

        :rtype: brain
        """

    def default_shipping_info():
        """Returns brain of default shipping info

        :rtype: brain
        """

    def infos():
        """Returns brains of all the address infos

        :rtype: brains
        """

    def rest_of_infos(uuid):  # pragma: no cover
        """Returns brains of all the address infos except for the info with the uuid

        :rtype: brains
        """


# Behavior

class IDiscountBehavior(DiscountBehaviorSchema, IDiscount):
    """Behavior interface for DiscountBehavior"""
