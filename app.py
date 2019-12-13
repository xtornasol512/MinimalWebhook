# Let's get this party started!
import falcon
import json


class WebhookResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')


    def on_post(self, req, resp):
        """  Webhook Type POST"""
        doc = json.load(req.bounded_stream)
        resp.body = json.dumps(doc)



# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
webhook = WebhookResource()

# things will handle all requests to the '/things' URL path
app.add_route('/', webhook)
