
def a_an(string):
    if string.beginswith('aeiou'):
        return "an"
    else:
        return "a"

def content_template(post):
     content = post["properties"].get("content")
    if not content:
        # have to continue bc it might be in the "content[html]" property...
        #I think angelo has abstracted all this already

    elif content.isinstance(str):
        #I don't obey the mandate that generic notes need to be plaintext: I'll happily stick in HTML. therefore, the Jinja "safe" filter is needed even when properties.content looks like a bare string -->
    <!--# FIXME: given this section in Micropub specification, since I want to be able to support HTML even if the post is a note, I should store all post content in the content[0].html scheme when saving a new post.
        # e.g. content : [{"html" : "the-content-is-here"}]
        # Why? because I want to be able to "return the content property as an object containing an html property"
        # if I store data as a mere string in properties.content, then if I return that to a Micropub client which supports editing, semantically that content will be understood as plain text. which is not what I want.

        # <q>HTML Content

        # If the source of the post was written as HTML content, then the endpoint MUST return the content property as an object containing an html property. Otherwise, the endpoint MUST return a string value for the content property, and the client will treat the value as plain text. This matches the behavior of the values of properties in [microformats2-parsing].</q>
        # todo need safe filter on the content? no, that should be getting filtered when it's ingested anyway........
        return content
    {% elif post.properties["content[html]"] %} %}
    {{post.properties["content[html]"|safe]}}
    {% elif post.properties.content[0].html %}
    {{post.properties.content[0].html|safe}}
    {% else %}
    {% endif %}


def name_template(name):
    return """<span class="p-name">{name}</span>"""


def render_name(post):
    """Render the microformats name property of a post."""
    if post.name:
        return post.name
    else:
        pt = post.discover_type()
        return a_an(pt) + pt


# todo is this a good idea?
# rewrite syndication_template, author_line, the "," loop in inner.html
# all in in terms of one fun "comma_list_with_fixings"


def syndication_template(syndication_url, syndication_location):
    """Return e.g. a link to a Twitter post with link text that reads 'Twitter.'"""
    return f"<a class='u-syndication' href='{syndication_url}'>{syndication_location}</a>"

def tag_template(tag):
    return f"<a class='p-category' href='/tags/{tag}'>{tag}</a>"

def author_template(author):
    return f"""<span class="p-author">{author}</span>"""

def author_line(authors):
    if len(authors) == 1:
        return authors[0]
    else:
        return ",".join(self.authors[:-1] + " and " + authors[-1]


# fuck this
# bc need to put more html onto each author them
def refer_poem(post):
    <h2>{{ post["properties"]["name"]}}</h2>
    <p><span class="h-entry"><a class="u-url" href="{{post.properties.url}}">{{ymdonly(raw_published(post))}}</a></span>{% if post.properties.updated %} (updated {{ymdonly(raw_updated(post))}}){% endif %}</p>
    {{content(post)}}

