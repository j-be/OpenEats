import html5lib
from html5lib import treebuilders, treewalkers, serializer
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@stringfilter
@register.filter(name='sanitize_html')
def sanitize_html(value):
    """A custom filter that sanitzes html output to make sure there is no bad stuff in it"""
    p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
    dom_tree = p.parseFragment(value)

    walker = treewalkers.getTreeWalker("dom")

    stream = walker(dom_tree)

    s = serializer.HTMLSerializer(sanitize=True, omit_optional_tags=False)
    return "".join(s.serialize(stream))
