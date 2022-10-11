"""
A module to translate input text in English to French and vice versa
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    translate the text input in English to French and return the French text
    """
    translation = language_translator.translate(
    englishText, model_id='en-fr').get_result()
    output = json.dumps(translation, indent=2, ensure_ascii=False)
    frenchText = json.loads(output)["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    """
    translate the text input in French to English and return the English text
    """
    translation = language_translator.translate(
    frenchText, model_id='fr-en').get_result()
    output = json.dumps(translation, indent=2, ensure_ascii=False)
    englishText = json.loads(output)["translations"][0]["translation"]
    return englishText
