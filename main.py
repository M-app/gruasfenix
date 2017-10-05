# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        template = JINJA_ENVIRONMENT.get_template('/templates/index.html')
        self.response.write(template.render())

class TodaLaCapital(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("/templates/servicios.html")
        self.response.write(template.render())

class AvisoLegal(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/avisolegal.html")
        self.response.write(template.render())

class PreguntasFrecuentes(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/preguntasfrecuentes.html")
        self.response.write(template.render())

class VillaNueva(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/villanueva.html")
        self.response.write(template.render())    

class TodasLasZonas(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/todaslaszonas.html")
        self.response.write(template.render())

class ServicioDeGruas(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/serviciodegruas.html")
        self.response.write(template.render())

class Emergencias(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/emergencias.html")
        self.response.write(template.render())

class Experiencia(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/experiencia.html")
        self.response.write(template.render())

class Remolcadoras(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/remolcadoras.html")
        self.response.write(template.render())

class Automotores(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/automotores.html")
        self.response.write(template.render())

class Mixco(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/mixco.html")
        self.response.write(template.render())

class SanLucas(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/sanlucas.html")
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/todalacapital',TodaLaCapital),
    ('/avisolegal',AvisoLegal),
    ('/preguntasfrecuentes',PreguntasFrecuentes),
    ('/villanueva',VillaNueva),
    ('/todaslaszonas',TodasLasZonas),
    ('/serviciodegruas',ServicioDeGruas),
    ('/gruasemergencia',Emergencias),
    ('/gruasexperiencia',Experiencia),
    ('/gruasremolcadoras',Remolcadoras),
    ('/gruasautomotores',Automotores),
    ('/mixco',Mixco),
    ('/sanlucas',SanLucas)
], debug=False)
