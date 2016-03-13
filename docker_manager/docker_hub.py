import json
import requests
from requests.auth import HTTPBasicAuth


class DockerHub(object):

    def __init__(self, org, password):
        self._org = org
        self._password = password

    def tags(self, image):
        url = self._url('/{}/tags'.format(image))
        res = self._get(url)
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            return None

    def _url(self, path):
        return 'https://registry.hub.docker.com/v1/repositories/{}{}'.format(self._org, path)

    def _get(self, url):
        return requests.get(url=url, auth=self._auth())

    def _auth(self):
        return HTTPBasicAuth(self._org, self._password)
