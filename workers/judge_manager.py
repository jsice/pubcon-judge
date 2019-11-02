from executors.base_executor import BaseExecutor

def judge_problem(language, code, inputs, outputs, time):
  judge = Judge(language, code, inputs, outputs)
  judge.execute(time)
  return judge.status

class Judge:
  EXECUTORS = {
    'python': BaseExecutor
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

      try:
        if executor.test(_input, _output):
          self.status = 'YES'
        else:
          self.status = 'WAE'
          break
      except BaseExecutor.CompilationError as error:
        print(error)
        self.status = 'CPE'
        break
