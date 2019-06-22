#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from checkbutton import checkButton

class myAssistant(Gtk.Assistant):
    def __init__(self):
        Gtk.Assistant.__init__(self, title="The Bazaar")
        self.set_default_size(800,600)

        self.software = set()

        intro = self.init_intro()
        nd = self.init_nd()
        utils = self.init_utils()
        summary = self.init_summary()

        for p in [intro, nd, utils, summary]:
            self.append_page(p)

        self.set_page_title(intro, "The Bazaar")
        self.set_page_title(nd, "Notre Dame Specific Software")
        self.set_page_title(utils, "Utility Software")
        self.set_page_title(summary, "Finished")

        self.set_page_type(intro, Gtk.AssistantPageType.INTRO)
        self.set_page_type(nd, Gtk.AssistantPageType.CONTENT)
        self.set_page_type(utils, Gtk.AssistantPageType.CONTENT)
        self.set_page_type(summary, Gtk.AssistantPageType.SUMMARY)

        self.set_page_complete(intro, True)
        self.set_page_complete(nd, True)
        self.set_page_complete(utils, True)

        self.connect("cancel", self.close)
        self.connect("close", self.close)
        self.connect("destroy", self.close)

    def init_intro(self):
        label = Gtk.Label()
        label.set_markup('''
                <big>Welcome to <b>The Bazaar!</b></big>

                <b>The Bazaar</b> is a software setup tool created
                by the Notre Dame Linux Users Group. This tool will
                help a Notre Dame student who is new to Linux get
                started with their favorite apps. If you are not a
                member of LUG (yet), consider joining!

                Check out our <a href='http://ndlug.org'>website</a> and the <a href='https://www.github.com/NDLUG/bazaar'>source code</a> for this project!
                ''')

        label.set_line_wrap(True)
        intro = Gtk.Frame()
        intro.add(label)

        return intro

    def init_nd(self):
        label = Gtk.Label()
        label.set_markup('''
                <big>Select the <b><i>Notre Dame specific</i></b> software you would like to install:</big>
                ''')
        nd = Gtk.Box(spacing = 6)
        nd.set_orientation(Gtk.Orientation.VERTICAL)
        nd.add(label)

        print_driver = checkButton('ND Print Driver', 'ndprint')
        eduroam_driver = checkButton('Eduroam Driver', 'eduroam')

        self.add_to_widget(nd, [print_driver, eduroam_driver])

        return nd

    def init_utils(self):
        label = Gtk.Label()
        label.set_markup('''
                <big>Select the <b><i>Utility</i></b> software you would like to install:</big>
                ''')
        utils = Gtk.Box(spacing = 6)
        utils.set_orientation(Gtk.Orientation.VERTICAL)
        utils.add(label)

        # Coding
        coding   = Gtk.Label('Text Editors')
        vscodium = checkButton('VSCodium', 'vscodium')
        vscode   = checkButton('Visual Studio Code', 'vscode')
        atom     = checkButton('Atom', 'atom')
        sublime  = checkButton('Sublime Text', 'sublime-text')

        self.add_to_widget(utils, [coding, vscodium, vscode, sublime])

        # Web Browsers
        browsers = Gtk.Label('Web Broswers')
        chromium = checkButton('Chromium', 'chromium')
        chrome   = checkButton('Chrome', 'chrome')
        firefox  = checkButton('Firefox', 'firefox')

        self.add_to_widget(utils, [browsers, chromium, chrome, firefox])

        # Gaming
        gaming  = Gtk.Label('Gaming')
        steam   = checkButton('Steam', 'steam')
        lutris  = checkButton('Lutris', 'eduroam')
        discord = checkButton('Discord', 'discord')

        self.add_to_widget(utils,[gaming,steam,lutris,discord])

        # Chat
        chat     = Gtk.Label('Chat Applications')
        slack    = checkButton('Slack', 'slack')
        whatsapp = checkButton('WhatsApp', 'whatsapp')
        telegram = checkButton('Telegram', 'telegram')
        signal   = checkButton('Signal', 'signal')

        self.add_to_widget(utils,[chat, slack, whatsapp, telegram, signal])

        spotify  = checkButton('Spotify', 'spotify')

        return utils

    def init_summary(self):
        label = Gtk.Label()
        label.set_markup('''
                <big>Summary</big>
                ''')
        summary = Gtk.Box(spacing = 6)
        summary.set_orientation(Gtk.Orientation.VERTICAL)
        summary.add(label)
        self.install(summary)

        return summary

    def add_to_widget(self, widget, widges):
        for w in widges:
            self.software.add(w)
            widget.add(w)

    def install(self, widget):
        for i in self.software:
            if isinstance(widget, Gtk.CheckButton) and widget.get_active():
                label = Gtk.Label('Installing {}...'.format(i))
                self.add(label)
                print('Installing {}...'.format(i))

    def close(self, widget):
        Gtk.main_quit()

a = myAssistant()
a.show_all()
Gtk.main()
