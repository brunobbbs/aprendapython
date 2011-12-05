# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class WebsiteTest(TestCase):
    """Testes unitários dos mapeamento dos templates
    estáticos
    """

    def test_homepage_sucesso(self):
        response = self.get.client(reverse('homepage'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed('website/index.html', response)
