from django.template import Node
from django.template.defaulttags import register


class RenderBlockNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return self.nodelist.render(context)


@register.tag
def renderblock(parser, token):
    nodelist = parser.parse(('endrenderblock',))
    parser.delete_first_token()
    return RenderBlockNode(nodelist)
