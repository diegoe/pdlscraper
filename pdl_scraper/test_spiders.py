#!-*- encoding: utf-8 -*-
import unittest

from pdl_scraper.spiders.proyecto_spider import ProyectoSpider
from _test_utils import fake_response_from_file


class TestProyectoSpider(unittest.TestCase):
    def setUp(self):
        self.spider = ProyectoSpider()

    def test_parse_pdfurl(self):
        results = self.spider.parse_item(fake_response_from_file('02764.html'))
        print(results.meta['item'])
        item = results.meta['item']
        self.assertEqual(item['numero_proyecto'], u'02764/2013-CR')
        self.assertEqual(item['codigo'], u'02764')
        self.assertEqual(item['congresistas'][0:10], u'Elias Aval')
        self.assertEqual(item['short_url'], u'4zhube')
        self.assertEqual(item['fecha_presentacion'], u'10/10/2013')
        self.assertEqual(item['titulo'], u'Propone Ley Universitaria')
        self.assertEqual(item['expediente'], u'http://www2.congreso.gob.pe/sicr/tradocestproc/Expvirt_2011.nsf/visbusqptramdoc/02764?opendocument')
        self.assertEqual(item['seguimiento_page'],
                         u'http://www.example.com')
        self.assertEqual(item['proponente'], u'Congreso')
        self.assertEqual(item['grupo_parlamentario'],
                         u'Grupo Parlamentario Fuerza Popular')
        self.assertEqual(item['iniciativas_agrupadas'][0:5], u'00154')
        self.assertEqual(item['nombre_comision'],
                         u'Comisión de Educación  Juventud y Deporte')
        self.assertEqual(item['titulo_de_ley'], u'LEY UNIVERSITARIA')
        self.assertEqual(item['numero_de_ley'], u'Ley Nº: 30220')
