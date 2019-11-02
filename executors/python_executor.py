from subprocess import check_output, STDOUT
from sys import executable

class PythonExecutor(BaseExecutor):
  def run_with(self, _input):
    cmd = [executable, self.program]

    with open(_input) as _input_stream:
      out = check_output(cmd, stdin=_input_stream, timeout=self.time, stderr=STDOUT)

    return out.decode("utf-8").strip()