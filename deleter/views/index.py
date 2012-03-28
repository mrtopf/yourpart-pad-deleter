#encoding=utf8
import uuid
import werkzeug

from starflyer import ashtml
from deleter import BaseHandler, logged_in
from py_etherpad import EtherpadLiteClient


class IndexView(BaseHandler):
    """an index handler"""
    
    template = "index.html"

    @ashtml()
    @logged_in()
    def get(self):
        """show the main screen for deleting pads"""
        return self.render()

    post = get

class Delete(BaseHandler):
    """delete a pad"""

    template = "success.html"

    @ashtml()
    @logged_in()
    def post(self):
        padname = self.request.form['name'].strip()
        padMgr = EtherpadLiteClient(self.config.settings.pad_api_key, self.config.settings.pad_api_url)
        if padname!="":
            try:
                padMgr.deletePad(padname)
            except ValueError, e:
                self.flash(u"Fehler: %s" %e, css_class="error")
            else:
                self.flash(u"Das Pad '%s' wurde erfolgreich gelöscht!" %padname, css_class="success")
        raise self.redirect(self.url_for("index"))
