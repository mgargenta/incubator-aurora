python_test_suite(
  name = 'all',
  dependencies = [ pants(':job') ]
)

python_library(
  name = 'util',
  sources = [ 'util.py' ],
  dependencies = [
    pants('src/main/python/twitter/aurora/BUILD.thirdparty:mock'),
    pants('src/main/python/twitter/aurora/client/cli'),
  ]
)

python_tests(
  name = 'job',
  sources = [ 'test_create.py', 'test_kill.py' ],
  dependencies = [
    pants(':util'),
    pants('src/main/python/twitter/aurora/BUILD.thirdparty:mock'),
    pants('aurora/twitterdeps/src/python/twitter/common/contextutil'),
    pants('src/main/python/twitter/aurora/client/cli'),
    pants('src/main/python/twitter/aurora/client/cli'),
    pants('src/test/python/twitter/aurora/client/commands:util')
  ]
)
