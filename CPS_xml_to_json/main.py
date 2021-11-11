from flask import Blueprint, json, jsonify
import xmltodict
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
    response.encoding = 'utf-8'
    response_text = response.content
    xml_feed = xmltodict.parse(response_text)

    feed = {
      'title': xml_feed['feed']['title']['#text'],
      'subtitle': xml_feed['feed']['subtitle'],
      'updated': xml_feed['feed']['updated'],
      'articles': {},
    }

    articles = xml_feed["feed"]["entry"]
    i = 0

    for article in articles:
      title = article['title']['#text']
      author = article['author']['name']
      content = article['content']['#text']
      link = article['link']['@href']
      thumbnail = article['media:thumbnail']['@url']
      summary = article['summary']['#text']
      published = article['published']
      categories = []

      for cat in article['category']:
        categories.append(cat['@term'])

      single_article = {
        'title': title,
        'perex': summary,
        'thumbnail': thumbnail,
        'content': content,
        'categories': categories,
        'link': link,
        'author': author,
        'published': published,
      }

      feed['articles'][i] = single_article
      i += 1

    return jsonify(feed)