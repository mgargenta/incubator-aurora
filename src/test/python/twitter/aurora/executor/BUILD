python_test_suite(name = 'all',
  dependencies = [
    pants(':executor_builds'),
    pants(':executor_detector'),
    pants(':executor_vars'),
    pants(':gc_executor'),
    pants(':thermos_executor'),
    pants(':thermos_task_runner'),
    pants('src/test/python/twitter/aurora/executor/common:all'),
  ]
)

python_tests(name = 'gc_executor',
  sources = ['test_gc_executor.py'],
  dependencies = [
    pants('src/main/python/twitter/aurora/BUILD.thirdparty:mock'),
    pants('aurora/twitterdeps/src/python/twitter/common/app'),
    pants('aurora/twitterdeps/src/python/twitter/common/concurrent'),
    pants('aurora/twitterdeps/src/python/twitter/common/quantity'),
    pants('aurora/twitterdeps/src/python/twitter/common/testing'),
    pants('src/main/python/twitter/thermos/common:path'),
    pants('src/main/python/twitter/thermos/config'),
    pants('src/main/python/twitter/thermos/core:runner'),
    pants('src/main/thrift/com/twitter/thermos:py-thrift'),
    pants('src/main/python/twitter/aurora/executor:gc_executor'),
    pants('src/main/thrift/com/twitter/aurora/gen:py-thrift'),
  ],
  coverage = 'twitter.mesos.executor.gc_executor'
)

python_tests(name = 'executor_detector',
  sources = [ 'test_executor_detector.py' ],
  dependencies = [
    pants('aurora/twitterdeps/src/python/twitter/common/contextutil'),
    pants('aurora/twitterdeps/src/python/twitter/common/dirutil'),
    pants('src/main/python/twitter/aurora/executor:executor_detector')
  ]
)

python_tests(name = 'thermos_executor',
  sources = ['test_thermos_executor.py'],
  timeout = Amount(5, Time.MINUTES),
  dependencies = [
    pants('aurora/twitterdeps/src/python/twitter/common/app'),
    pants('aurora/twitterdeps/src/python/twitter/common/exceptions'),
    pants('aurora/twitterdeps/src/python/twitter/common/quantity'),
    pants('src/main/python/twitter/thermos/common'),
    pants('src/main/python/twitter/thermos/core'),
    pants('src/main/python/twitter/thermos/monitoring:monitor'),
    pants('src/main/python/twitter/aurora/config:schema'),
    pants('src/main/python/twitter/aurora/executor/common:executor_timeout'),
    pants('src/main/python/twitter/aurora/executor/common:health_checker'),
    pants('src/main/python/twitter/aurora/executor/common:sandbox'),
    pants('src/main/python/twitter/aurora/executor/common:task_runner'),
    pants('src/main/python/twitter/aurora/executor:thermos_executor'),
    pants('src/main/python/twitter/aurora/executor:thermos_task_runner'),
    pants('src/main/thrift/com/twitter/aurora/gen:py-thrift'),
  ]
)

python_tests(name = 'thermos_task_runner',
  sources = ['test_thermos_task_runner.py'],
  dependencies = [
    pants('aurora/twitterdeps/src/python/twitter/common/contextutil'),
    pants('aurora/twitterdeps/src/python/twitter/common/dirutil'),
    pants('aurora/twitterdeps/src/python/twitter/common/log'),
    pants('aurora/twitterdeps/src/python/twitter/common/quantity'),
    pants('src/main/python/twitter/aurora/config:schema'),
    pants('src/main/python/twitter/aurora/executor/common:sandbox'),
    pants('src/main/python/twitter/aurora/executor/common:status_checker'),
    pants('src/main/python/twitter/aurora/executor:thermos_task_runner'),
  ]
)

python_tests(name = 'executor_vars',
  sources = ['test_executor_vars.py'],
  dependencies = [
    pants('aurora/twitterdeps/src/python/twitter/common/contextutil'),
    pants('src/main/python/twitter/aurora/executor:executor_vars'),
  ]
)

python_tests(name = 'executor_builds',
  sources = ['test_executor_builds.py'],
)
