import re

from django import template
from django.template import Node
from django.template.defaulttags import register


class RenderBlockNode(Node):
    def __init__(self, nodelist, varname):
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        context[self.varname] = self.nodelist.render(context)
        return ""


@register.tag
def renderblock(parser, token):
    nodelist = parser.parse(('endrenderblock',))
    parser.delete_first_token()

    try:
        args = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % args[0])

    if len(args) != 3:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % args[0])

    as_tag = args[1]
    if as_tag != "as":
        raise template.TemplateSyntaxError("%r tag's argument should have 'as' parameter for set variable" % args[0])

    varname = args[2]
    if varname[0] == varname[-1] and varname[0] in ('"', "'"):
        raise template.TemplateSyntaxError("%r tag's argument should not be in quotes" % varname)

    return RenderBlockNode(nodelist, varname)
