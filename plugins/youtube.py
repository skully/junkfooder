import random
import urllib2
from lxml import html
from urllib import urlencode

import plugin


def youtube(irc, user, target, msg):
    videos = YouTube().search(msg)
    title, url = _random_from_dict(videos)
    irc.msg(target, url + " - " + title)


def _random_from_dict(videos):
    index = random.randint(0, len(videos) - 1)
    url = list(videos.keys())[index]
    title = videos[url]
    return title, url


class YouTube(object):
    def __init__(self, **kwargs):
        self.urllib = kwargs.get("urllib", urllib2)
        self.base_url = "https://www.youtube.com"

    def search(self, query):
        """
        :type query: str
        :rtype: dict[str, str]
        """
        search_query = urlencode({
            "search_query": query
        })
        response = self.urllib.urlopen(
            self.base_url + "/results?" + search_query,
        )
        return self._parse_video_links_from_string(response.read())

    def _parse_video_links_from_string(self, response):
        xpath_query = '//div[@class="yt-lockup-content"]/h3/a[starts-with(@href, "/watch?v=")]'

        tree = html.fromstring(response)
        elements = tree.xpath(xpath_query)

        return self._process_links_from_elements(elements)

    def _process_links_from_elements(self, elements):
        links = {}

        for link in elements:
            url = self.base_url + link.get('href')
            links[url] = link.get('title')

        return links


plugin.add_plugin('^!yt ', youtube)
