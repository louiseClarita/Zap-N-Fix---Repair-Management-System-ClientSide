# based on: http://www.djangosnippets.org/snippets/779/
from django.template import Library, Node, TemplateSyntaxError

register = Library()


class RangeNode(Node):
    def __init__(self, range_args, context_name):
        self.range_args = range_args
        self.context_name = context_name

    def render(self, context):
        context[self.context_name] = range(*self.range_args)
        return ""


@register.simple_tag
def mkrange(value):
    return range(1, value + 1)