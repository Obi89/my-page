#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class About(BaseHandler):
    def get(self):
        return self.render_template("aboutme.html")

class Projects(BaseHandler):
    def get(self):
        return self.render_template("projects.html")

class Blog(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class Contact(BaseHandler):
    def get(self):
        return self.render_template("contact.html")

class Request(BaseHandler):
    def get(self):
        return self.render_template("request.html")

class Blog2(BaseHandler):
    def get(self):
        return self.render_template("blog2.html")



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/aboutme', About),
    webapp2.Route('/projects', Projects),
    webapp2.Route('/blog', Blog),
    webapp2.Route('/contact', Contact),
    webapp2.Route('/request', Request),
    webapp2.Route('/blog2', Blog2),
], debug=True)
