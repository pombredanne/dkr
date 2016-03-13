import re


class DockerManager(object):

    def __init__(self, org, password):
        self._org = org
        self._remote = DockerHub(org, password)
        self._local = DockerLocal()

    def show_images(self, image_arg):
        [ self.show_image(arg) for arg in image_arg if re.match('.*:', arg) ] # todo: no need for re.

    def show_image(self, image_arg):
        im = DockerImage(self._org, image_arg)
        local_inspect = self._local.inspect(im.full_name_with_version())
        if local_inspect:
            local_layer = local_inspect['Id'][0:8]
        else:
            local_layer = None
        remote_tags = self._remote.tags(im.name())
        remote_layer = None
        if remote_tags:
            version = im.version()
            matching = [ m for m in remote_tags if m['name'] == version ]
            if matching:
                remote_layer = matching[0]['layer']
        print("{:36} {:10} {:10}".format(im.full_name_with_version(), local_layer, remote_layer))
