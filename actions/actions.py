# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .weatherdata import Weather
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

message=''
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello Iam your weather bot how can i help you..")
#
#         return []


class ActionPlace(Action):

    def name(self) -> Text:
        return "action_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities =tracker.latest_message['entities']
        print(entities)
        place=tracker.get_slot("place")
        print(f'place={place}')
        weather=Weather()
        print(weather.weather_detail(place))
        dispatcher.utter_message(text=weather.weather_detail(place)+'\n Hope it helped :)')


        return []

# need to run:
# https://forum.rasa.com/t/how-to-get-the-last-message-uttered-by-bot/9105
#https://rasa.com/docs/rasa/fallback-handoff/#fallbacks