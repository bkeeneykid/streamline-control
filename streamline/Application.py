import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from streamline.ConfigWindow import ConfigWindow


class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.theorangealliance.streamline", **kwargs)
        self.main_window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

    def do_activate(self):

        self.main_window = ConfigWindow(application=self)
        self.main_window.present()

    def on_quit(self):
        self.quit()