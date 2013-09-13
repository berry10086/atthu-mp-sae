import sae
from atthupy import wsgi

application = sae.create_wsgi_app(wsgi.application)