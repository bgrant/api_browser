"""
Fetch JSON data from the web and explore it with TraitsUI.
"""

import requests
import json

from traits.api import HasTraits, Str, Button, Any, File
from traitsui.api import View, VGroup, HGroup, Item, ValueEditor, FileEditor


class ApiData(HasTraits):

    data = Any
    url = Str("http://www.khanacademy.org/api/v1/badges")
    fetch = Button('Fetch')
    filename = File(auto_set=True)
    save = Button('Save')

    def fetch_data(self, url):
        return requests.get(url)

    def _fetch_fired(self):
        self.data = self.fetch_data(self.url).json()

    def _save_fired(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)


view = View(
        VGroup(
            HGroup(
                Item('fetch', show_label=False),
                Item('url', show_label=False, springy=True),
                show_border=True,
            ),
            Item('data',
                 editor=ValueEditor(),
                 show_label=False,
                 ),
            HGroup(
                Item('save', show_label=False),
                Item('filename',
                     editor=FileEditor(),
                     show_label=False,
                     springy=True),
                show_border=True,
            ),
            show_border=False
            ),
        title='API Browser',
        width=400,
        height=400,
        resizable=True
        )


if __name__ == '__main__':
    b = ApiData()
    b.configure_traits(view=view)
