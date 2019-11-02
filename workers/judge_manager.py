def judge_problem(language, code, inputs, outputs, time):
  judge = Judge(language, code, inputs, outputs)
  judge.execute(time)
  return judge.status

class CodeExecutor:
    def __init__(self, code, time):
        pass

    def test(self, _input, _output):
        return False

class Judge:
  EXECUTORS = {
    'python': CodeExecutor # To be implemented
  }

  def __init__(self, language, code, inputs, outputs):
    self.language = language
    self.code = code
    self.inputs = inputs
    self.outputs = outputs
    self.status = 'NEW'

  def execute(self, time):
    executor = self.EXECUTORS[self.language](self.code, time)
    for i in range(len(self.inputs)):
      _input = self.inputs[i]
      _output = self.outputs[i]

      if executor.test(_input, _output):
        self.status = 'YES'
      else:
        self.status = 'WAE'
        break
