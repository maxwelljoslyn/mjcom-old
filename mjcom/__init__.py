"""
The www.maxwelljoslyn.com website.
"""

from understory import indieweb, web
from understory.web import tx


app = indieweb.personal_site(
    __name__,
    db=True,
    args={
        "poem": r".*",
        "person": r"[\w-]+",
        "sithlord": r".+"
    }
)

def wrap():
    yield
    # todo wrap html requests in 
    # if tx.headers.....
    # body = wrap(app.view.outer, body)
    pass


# todo redirect /index
@app.control("")
class Home:

    def get(self):
        return app.view.home()


@app.control("robots\.txt")
class Robots:

    def get(self):
        return app.view.robots()

@app.control("tags/{tag}")
class Tag:
    
    descriptions = {"poetry" : "Looking for poetry? Don't forget to read My Poems, or Others' Poems."}
    # posts, count = tx.db.posts_tagged(self.tag)

    def get(self):
        return templates.tag(
                f"Posts Tagged '{tag}'",
                self.tag,
                description.get(self.tag)
                # posts,
                # count)
                )


@app.control("tags")
class Tags:

    def get(self):
        return templates.tags("All Tags")

# wont work out of the box
#@app.control("alltags")
#@app.control("all-tags")
#@app.control("all_tags")
#@app.control("tag") -> tags
#@app.control("tag/X") -> tags/X
#class Redirect_Tags:
#
#    if tx.request.uri.path != the_canonical_one:
#        raise redirect
#
#    def get(self):
#        raise web.SeeOther("tags")

@app.control("poems")
class Poems:
    # todo rearrange in old order: poems_after_hooked, hooked_and_before
    # todo write 'get all from poems channel where author is me'
    # todo write template
    pass

@app.control("sithlordchallenge")
class SithLordChallenge:
    # posts = tx.get_channel('sithlordchallenge')
    return app.view.sithlordchallenge(posts)
    pass




@app.control("blog")
class Blog:

    def get(self):
        entries = tx.pub.recent_entries()
        return app.view.blog(entries)


# todo borrow this from indieweb.personal_site @app.control(r"{year}/{month}/{day}/{seconds}(/{slug})?")
class Entry:
    """An individual entry."""

    def get(self):
        resource = tx.pub.read(tx.request.uri.path)["resource"]
        # todo should this be resource["visibility"][0] bc value at "visibility"  is a list?
        if resource["visibility"] != "public" and not tx.user.session:
            raise web.SeeOther(f"/sign-in?return_to={tx.request.uri.path}")
        return app.view.entry(resource)


@app.control(r"/fedoradventure/play")
class FedorAdventure:

    def get(self):
        web.header("X-Accel-Redirect", "/static/fedoradventure/play.html")


@app.control(r"/fedoradventure/download")
class FedorAdventureDownload:

    def get(self):
        web.header("X-Accel-Redirect", "/static/fedoradventure/Fedoradventure.gblorb")


@app.control(r"/ryanquest/play")
class RyanQuest:

    def get(self):
        web.header("X-Accel-Redirect", "/static/ryanquest/play.html")


@app.control(r"/ryanquest/download")
class RyanQuestDownload:

    def get(self):
        web.header("X-Accel-Redirect", "/static/ryanquest/RYAN QUEST.gblorb")


#@app.control("sithlordchallenge/{sithlord}")
#def SithLord:
#
#    #    def get(self):
#    #        lord = tx.pub.read(tx.request.uri.path)["resource"]
#    #        return app.view.sithlord(lord)
#
#    pass

