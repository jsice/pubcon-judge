from concurrent.futures import ThreadPoolExecutor
from workers.judge_manager import judge_problem

if __name__ == '__main__':
  executor = ThreadPoolExecutor(max_workers=5)
  print('waiting for submission...')
  # example
  # executor.submit(judge_problem, 'python', 'files/test.py', ['files/testcase/1.in'], ['files/testcase/1.ans'], 1)
