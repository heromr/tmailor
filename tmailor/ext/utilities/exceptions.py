import json

class EmailNotFound(Exception):
    """
    API Code: 101
    """

class InternalServerError(Exception):
    """
    API Code: 500
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnknownError(Exception):
    """
    API Code: Unknown
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


def CheckException(data):

    if isinstance(data, dict):
        data = json.dumps(data)
        
    data = json.loads(data)
    api_code = data.get("code")

    if api_code == 500:
        raise InternalServerError(data)
    elif api_code == 101:
        raise EmailNotFound(data)
    elif api_code == 400:
        raise EmailNotFound(data)
    else:
        raise UnknownError(data)
