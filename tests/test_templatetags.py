from django.template.loader import render_to_string
from django.test import TestCase


class RenderBlockTestCase(TestCase):

    def setUp(self):
        pass

    def test_renderblock_should_work_without_context(self):
        rendered_template = render_to_string(template_name="renderblock_without_context.html")

        self.assertTrue("<p><em>A block rendered into variable</em></p>" in rendered_template)

    def test_renderblock_should_work_with_context(self):
        rendered_template = render_to_string(template_name="renderblock_with_context.html", context={"value": "1"})

        self.assertTrue("<p><em>A block rendered with value 1 into variable</em></p>" in rendered_template)

    def tearDown(self):
        pass
