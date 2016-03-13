import re

class DockerImage(object):

    def __init__(self, org, image):
        self._org = org
        im0 = re.sub('^' + org + '/', "", image)
        parts = im0.split(':')
        self._name = parts[0]
        if len(parts) == 2:
            self._version = parts[1]
        else:
            self._version = None

    def org(self):
        return self._org

    def name(self):
        return self._name

    def version(self):
        return self._version

    def full_name(self):
        return "/".join([self.org(), self.name()])

    def full_name_with_version(self):
        if self.version():
            return "{}:{}".format(self.full_name(), self.version())
        else:
            return None
