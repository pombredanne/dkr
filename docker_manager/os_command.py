import subprocess


class OsCommand(object):

    def __init__(self, cmd):
        self.cmd = cmd

    def run_with_exit_code(self):
        p = subprocess.Popen(
              self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout_data, stderr_data = p.communicate()
        out = stdout_data.rstrip()
        return (p.returncode, out)
