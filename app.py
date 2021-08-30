"""
The www.maxwelljoslyn.com website.
https://github.com/canopy/canopy/blob/main/canopy/templates/about.html
https://github.com/canopy/canopy/blob/main/canopy/templates/home.html
https://github.com/canopy/canopy/tree/main/canopy/templates

"""

from understory import indieweb, kv, sql, web
from understory.web import tx


# XXX still need year/mo/day/slug/etc regexes?
# what about eg sithlord, poem, etc
app = indieweb.site("Maxwell Joslyn's Website",
                        static=__name__,
                        year=r"\d{4}",
                        month=r"\d{2}",
                        day=r"\d{2}",
                        slug=r"[\d\w_]+",
                        poem=r".*",
                        person=r"[\w-]+",
                        sithlord=r".+")
templates = web.templates(__name__)



# XXX where should robots.txt be placed? same dir as this py file? static folder?
@app.route("robots\.txt")
class Robots:

    def get(self):
        web.header("content-type", "text/plain")
        f = open("robots.txt", "r")
        return f.read()

@app.route("")
class Home:

    def get(self):
        return "Home"
