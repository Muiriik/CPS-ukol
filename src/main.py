from flask import Flask, request, Blueprint
import xmltodict
import json
import requests


convert_blueprint = Blueprint('convert', __name__)


@convert_blueprint.route("/")
def hp():
  return ":)"

@convert_blueprint.route("/feed.json", methods=['GET'])
def convert():
  url = "https://www.pirati.cz/feed.xml"
  response = requests.get(url)

  response.raise_for_status()
  if response.status_code == 200:

    # response.encoding = response.apparent_encoding
    response.encoding = 'utf-8'
    response_text = response.content

    xml_feed = xmltodict.parse(response_text)

    print(xml_feed)

    return xml_feed