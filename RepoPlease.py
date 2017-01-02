# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import json
import os.path

class RepoPleaseCommand(sublime_plugin.WindowCommand):

    def run(self):

        items = sublime.find_resources('package-metadata.json')
        items.sort()
        self.items = []
        for item in items:
            # with open(os.path.join(os.path.dirname(sublime.packages_path()),
            #                                        item)) as fp:
            self.items.append([item.split('/')[1], json.loads(sublime.load_resource(item))['url']])
        self.window.show_quick_panel(self.items, self.open_repo)

    def open_repo(self, index):
        if index == -1:
            return

        sublime.run_command('open_url', {
            'url': self.items[index][1]
        })
