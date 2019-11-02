class BaseExecutor:
  class CompilationError(Exception):
    pass

  def __init__(self, code, time):
    self.program = self.compile(code)
    self.time = time

  def compile(self, code):
    return code

  def run_with(self, _input):
    raise NotImplementedError('Should have implemented this')

  def test(self, _input, _output):
    with open(_output) as f:
      answer = f.read().strip()

    return self.run_with(_input) == answer
