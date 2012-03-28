import pkg_resources
import os
import starflyer


from jinja2 import Environment, PackageLoader, PrefixLoader
import views

def setup(**kw):
    """setup the application. 

    :param kw: optional keyword arguments to override certain values of the 
        settings section of the configuration

    :return: a configuration object to be passed into the application
    """

    config = starflyer.Configuration()
    config.register_sections('logs')
    config.register_snippet_names('header', 'footer')
    config.register_template_chains("main")

    ## various constants
    config.update_settings({
        #'log_name' : "participate",
        'virtual_host' : "http://localhost:8222",
        'virtual_path' : "/",
        'title' : "YouthPart Pad Delete Tool",
        'description' : "tool for deleting Pads",
        'debug' : False,
        'cookie_secret' : "89c7sc9ds87cs9c7s09c87cs9cd8888d88d88d88!8d88",
        'pad_secret' : "s",
        'message_cookie_name' : "m",
        'pad_api_key' : "YwZ95eln1OWBTgWw5ukIIEp28f9IpDzj",
        'pad_api_url' : "http://localhost:9001/api",
        'admin_password' : "test123",
    })
    config.update_settings(kw) # update with data from ini file

    config.routes.extend([
        ('/', 'index', views.index.IndexView),
        ('/delete', 'delete', views.index.Delete),
    ])

    ## templates
    config.templates.main.append(PackageLoader("deleter","templates"))

    ## static resources like JS, CSS, images
    static_file_path = pkg_resources.resource_filename(__name__, 'static')
    config.register_static_path("/css", os.path.join(static_file_path, 'css'))
    config.register_static_path("/js", os.path.join(static_file_path, 'js'))
    config.register_static_path("/img", os.path.join(static_file_path, 'img'))

    return config

