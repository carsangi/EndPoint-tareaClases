import json
import random
import falcon
from falcon import API

class HolaMundo():

    def on_get(self, req, resp, uuid):
        mensajes = ['Hola Mindo','Hola Que hace', 'Adio', 'Ciao','2+2=4']
        resp.body = json.dumps(mensajes)
        resp.status =falcon.HTTP_OK


def iniciar() ->  API:
#run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/hola-mundo",HolaMundo())

    return api

app=iniciar()