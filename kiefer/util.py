# Expected status should be an integer, but since Jawbone messes up
# status codes (e.g. create workout return 200 instead of 201) we need
# a way to check for multiple status codes -.-
def validate_response(req, expected_status, exception_cls=Exception):
    """
    Validate that request was successful, otherwise raise an exception.

    :param req: requests.Response
    :param expected_status: :class:`int` or :class:`list`
    :param exception_cls: (Custom) exception class
    """
    def raise_error():
        error_type = req.json()['meta']['error_type']
        error_detail = req.json()['meta']['error_detail']
        raise exception_cls('{}: {}'.format(error_type, error_detail))

    if isinstance(expected_status, int):
        if req.status_code != expected_status:
            raise_error()
    else:
        if req.status_code not in expected_status:
            raise_error()
    return True
