
import dash
from pages.deals.layout import deals_layout
from pages.home.layout import home_layout


class Controller:
    def configure(self):
        dash.register_page(
            "home",
            path='/',
            title='Home',
            name='Home',
            layout=home_layout
        )

        dash.register_page(
            "deals",
            path='/deals',
            title='Deals',
            name='Deals',
            layout=deals_layout
        )