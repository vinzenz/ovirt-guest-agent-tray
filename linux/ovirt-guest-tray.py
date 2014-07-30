#!/usr/bin/env python

import gtk

class TrayIcon:
    def __init__(self, *args, **kwargs):
        self.icon = gtk.StatusIcon()
        self.icon.set_from_file('ovirt-icon-48.svg')
        self.icon.connect('popup-menu', self.on_popup_menu)

    def on_about(self, *args, **kwargs):
        dlg = gtk.Dialog("About the oVirt Guest Agent",
                         None,
                         gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                         (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        label1 = gtk.Label("oVirt Guest Agent for Linux")
        label1.show()
        label2 = gtk.Label("Version 3.6.0")
        label2.show()
        label3 = gtk.Label("oVirt Guest Agent is running.")
        label3.show()
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        textview = gtk.TextView()
        textview.set_editable(False)
        textview.set_cursor_visible(False)
        textview.set_sensitive(False)
        sw.add(textview)
        buffer = textview.get_buffer()
        lic = '<Copyright information here>'
        try:
            f = open('/usr/share/ovirt-guest-agent/COPYING', 'r')
            lic = f.read()
            f.close()
        except (OSError,IOError):
            pass
        buffer.insert(buffer.get_end_iter(), lic)
        textview.show()
        sw.show()
        dlg.vbox.set_homogeneous(False)
        dlg.vbox.pack_start(label1, fill=False, expand=False, padding=4)
        dlg.vbox.pack_start(label2, fill=False, expand=False, padding=4)
        dlg.vbox.pack_start(sw, fill=True, expand=True, padding=4)
        dlg.vbox.pack_start(label3, fill=False, expand=False, padding=4)
        dlg.set_default_size(640, 480)
        dlg.run()
        dlg.destroy()

    def on_popup_menu(self, icon, event_button, event_time):
        menu = gtk.Menu()
        about = gtk.MenuItem('About')
        about.show()
        about.connect('activate', self.on_about)
        menu.append(about)
        sep = gtk.SeparatorMenuItem()
        sep.show()
        menu.append(sep)
        quit = gtk.MenuItem('Quit')
        quit.show()
        menu.append(quit)
        quit.connect('activate', gtk.main_quit)
        menu.popup(None, None, gtk.status_icon_position_menu, event_button, event_time, self.icon)

if __name__ == '__main__':
    icon = TrayIcon()
    gtk.main()
