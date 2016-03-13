import unittest
from docker_manager import DockerImage


class TestDockerImage(unittest.TestCase):

    def test1(self):
        im = DockerImage("org", "org/name:vsn")
        self.assertEquals("org/name:vsn", im.full_name_with_version())
        self.assertEquals("org/name", im.full_name())
        self.assertEquals("name", im.name())
        self.assertEquals("vsn", im.version())

    def test2(self):
        im = DockerImage("foo", "bar/name:vsn")
        self.assertEquals("foo/bar/name:vsn", im.full_name_with_version())
        self.assertEquals("bar/name", im.name())
        self.assertEquals("foo/bar/name", im.full_name())
        self.assertEquals("vsn", im.version())
