import os
import io
import json
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests
from PIL import Image, ImageDraw, ImageFont

credential = json.load(open('credentials.json'))
API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']

cv_client = ComputerVisionClient(ENDPOINT,CognitiveServicesCredentials(API_KEY))

image_url = 'https://i.redd.it/jgbqyq56uinb1.jpg'

response = cv_client.read(url = image_url, language='en',raw = True)
operationLocation = response.headers['Operation-Location']
operation_id = operationLocation.split('/')[-1]
result = cv_client.get_read_result(operation_id)

print(result)