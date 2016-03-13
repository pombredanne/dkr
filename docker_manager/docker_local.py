import json


class DockerLocal(object):

    def inspect(self, arg):
        (rc, res) = OsCommand("docker inspect {}".format(arg)).run_with_exit_code()
        if rc == 0:
            data = json.loads(res)[0]
            return data
        else:
            return None
