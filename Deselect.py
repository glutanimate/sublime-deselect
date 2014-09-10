# Sublime Deselect plugin
# 
# based on a forum post by C0D312:
# https://www.sublimetext.com/forum/viewtopic.php?f=2&t=4716#p21219

import sublime, sublime_plugin

class DeselectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        end = self.view.sel()[0].b
        pt = sublime.Region(end, end)
        self.view.sel().clear()
        self.view.sel().add(pt)