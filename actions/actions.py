# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
import os
import random
import json
import time
import requests
import logging
#import locale
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import UserUtteranceReverted

################################################
# Devuelve un sonido para analizar
################################################


logger = logging.getLogger(__name__)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}#, 'Access-Control-Allow-Origin':'*'}

dia = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

class action_dar_sonido_info(Action):
    def name(self):
        return 'action_dar_sonido_info'

    def run(self, dispatcher, tracker, domain):
        url = 'http://138.100.100.143:3001/sonidos?policy=random'
        r = requests.get(url, headers=headers)
        decoded = json.loads(r.text)
        dispatcher.utter_message(decoded["Ruta"])
        index = decoded['_id'].find('_')
        estacion = decoded['_id'][:index]
        date = decoded['_id'][index+1:-4]
        dateTimeObj = datetime.strptime(date, '%Y-%m-%d-%H%M')
        hour = dateTimeObj.strftime("%H:%M")
        day = dateTimeObj.day
        weekday = dia[dateTimeObj.weekday()]
        month = mes[dateTimeObj.month]
        date = weekday + ' ' + str(day) + " de " + month + " a las " + str(hour)
        return [SlotSet("eco", decoded["_id"]), SlotSet("estacion", estacion.capitalize()), SlotSet("fecha",date)]


class action_post_api(Action):
    def name(self):
        return 'action_post_api'

    def run(self, dispatcher, tracker, domain):
        url = 'http://138.100.100.143:3001/clasificaciones/'

        query_Dict ={}
        
        nombre = tracker.get_slot('nombre')
        message = tracker.latest_message['text']

        respuesta1 = tracker.get_slot('respuesta1')
        respuesta2 = tracker.get_slot('respuesta2')
        respuesta3 = tracker.get_slot('respuesta3')
        eco = tracker.get_slot('eco')
        
        query_Dict['_id'] = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")  
        query_Dict['idEco'] = eco
        query_Dict['Tipo'] = "Sonido"
        query_Dict['Respuesta1'] = respuesta1
        query_Dict['Respuesta2'] = respuesta2
        query_Dict['Respuesta3'] = respuesta3
        
        r = requests.post(url, data=json.dumps(query_Dict), headers=headers)
        
        #Reseteamos los valores de los slots
        return [SlotSet("respuesta1",None),SlotSet("respuesta2",None),SlotSet("respuesta3",None),SlotSet("eco",None)]

class ActionSetDuracion(Action):
   def name(self):
      return "action_set_duracion"

   def run(self, dispatcher, tracker, domain):

      respuesta = tracker.latest_message['intent'].get('name')
      if (respuesta == 'corto'):
         return [SlotSet("duracion", "corto"), SlotSet("respuesta1", "Menos de 1 segundo")]
      elif (respuesta == 'mediano'):
         return [SlotSet("duracion", "mediano"), SlotSet("respuesta1", "Entre 1 y 5 segundos")]
      elif (respuesta == 'largo'):
         return [SlotSet("duracion", "largo"), SlotSet("respuesta1", "Mas de 9 segundos")]

class ActionSetR2(Action):
   def name(self):
      return "action_set_r2"

   def run(self, dispatcher, tracker, domain):

      respuesta = tracker.latest_message['intent'].get('name')
      if (respuesta == 'affirm'):
         return [SlotSet("respuesta2", "Sí")]
      elif (respuesta == 'deny'):
         return [SlotSet("respuesta2", "No")]

class ActionSetR3(Action):
   def name(self):
      return "action_set_r3"

   def run(self, dispatcher, tracker, domain):
      
      respuesta = tracker.latest_message['intent'].get('name')
      if (respuesta == 'affirm'):
         return [SlotSet("respuesta3", "Sí")]
      elif (respuesta == 'deny'):
         return [SlotSet("respuesta3", "No")]


