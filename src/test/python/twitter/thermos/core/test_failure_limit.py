from twitter.thermos.config.schema import (
  Task,
  Resources,
  Process)
from twitter.thermos.testing.runner import RunnerTestBase
from gen.twitter.thermos.ttypes import (
  TaskState,
  ProcessState
)

class TestFailureLimit(RunnerTestBase):
  @classmethod
  def task(cls):
    task = Task(
      name = "failing_task",
      resources = Resources(cpu = 1.0, ram = 16*1024*1024, disk = 16*1024),
      max_failures = 2,
      processes = [
        Process(name = "a", max_failures=1, min_duration=1, cmdline="echo hello world"),
        Process(name = "b", max_failures=1, min_duration=1, cmdline="exit 1"),
        Process(name = "c", max_failures=1, min_duration=1, cmdline="echo hello world")
      ],
      constraints = [{'order': ['a', 'b', 'c']}]
    )
    return task.interpolate()[0]

  def test_runner_state_failure(self):
    assert self.state.statuses[-1].state == TaskState.FAILED

  def test_runner_process_in_expected_states(self):
    processes = self.state.processes
    assert len(processes['a']) == 1
    assert processes['a'][0].state == ProcessState.SUCCESS
    assert len(processes['b']) == 1
    assert processes['b'][0].state == ProcessState.FAILED
    assert 'c' not in processes


class TestTaskSucceedsIfMaxFailures0(RunnerTestBase):
  @classmethod
  def task(cls):
    base = Process(max_failures=2, min_duration=1)
    ex = base(cmdline="exit 1")
    hw = base(cmdline="echo hello world")
    task = Task(
      name = "failing_task",
      resources = Resources(cpu = 1.0, ram = 16*1024*1024, disk = 16*1024),
      max_failures = 0,
      processes = [ex(name='f1'), ex(name='f2'), ex(name='f3'),
                   hw(name='s1'), hw(name='s2'), hw(name='s3')])
    return task.interpolate()[0]

  def test_runner_state_failure(self):
    assert self.state.statuses[-1].state == TaskState.SUCCESS

  def test_runner_process_in_expected_states(self):
    for process in self.state.processes:
      for run in range(len(self.state.processes[process])):
        if process.startswith('f'):
          assert self.state.processes[process][run].state == ProcessState.FAILED
        elif process.startswith('s'):
          assert self.state.processes[process][run].state == ProcessState.SUCCESS
        else:
          assert False, "Unknown process!"
