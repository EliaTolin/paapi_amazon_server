from models.exceptions.base_exception import Error


class UrlNotDefinedAmazonException(Error):
    """Url not defined """
    pass


class MissingParameterAmazonException(Error):
    """At least one of Actor, Artist, Author,
    Brand, BrowseNodeId, Keywords, SearchIndex, Title should be provided."""
    pass


class GenericErrorAmazonException(Error):
    """Generic Error in Amazon API"""
    pass


class TooManyRequestAmazonException(Error):
    """except amazon_paapi.errors.exceptions.TooManyRequests:
        https://github.com/sergioteula/python-amazon-paapi/discussions/59"""
    pass
