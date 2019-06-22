#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class checkButton(Gtk.CheckButton):
    def __init__(self, label, value):
        Gtk.CheckButton.__init__(self, label=label)
        self.value = value
