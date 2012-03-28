# encoding=utf-8
import starflyer
import functools
from werkzeug.wrappers import Request, Response
import werkzeug.exceptions

__all__ = ["BaseHandler", "logged_in"]


class AuthException(werkzeug.exceptions.Unauthorized):
    """extended version of a unauthorized exception"""

    def __init__(self, description=None, realm=""):
        Exception.__init__(self, '%d %s' % (self.code, self.name))
        if description is not None:
            self.description = description
        self.realm = realm

    def get_headers(self, environ):
        """return the headers"""
        headers = [('Content-Type', 'text/html')]
        headers.append(('WWW-Authenticate', 'Basic realm=%s' %self.realm))
        return headers
        
class logged_in(object):
    """check if a valid user is present"""

    def __call__(self, method):
        """check user"""

        that = self

        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            auth = self.request.authorization
            if not auth or not (auth.username=="admin" and auth.password==self.config.settings.admin_password):
                raise AuthException('Could not verify your access level for that URL.', realm="Pad Manager")
            return method(self, *args, **kwargs)
        return wrapper


class BaseHandler(starflyer.Handler):
    """an extended handler for the deleter"""

    def prepare_render(self, params):
        """provide more information to the render method"""
        params = super(BaseHandler, self).prepare_render(params)
        return params

