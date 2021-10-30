# Chapter 1: Hello, World!

https://www.youtube.com/playlist?list=PLhOuww6rJJNP7UvTeF6_tQ1xcubAs9hvO

Write a program to enthusiastically greet the world:

```
$ ./hello.py
Hello, World!
```

The program should also accept a name given as an optional `--name` parameter:

```
$ ./hello.py --name Universe
Hello, Universe!
```

The program should produce documentation for `-h` or `--help`:

```
$ ./hello.py -h
usage: hello.py [-h] [-n str]

Say hello

optional arguments:
  -h, --help          show this help message and exit
  -n str, --name str  The name to greet (default: World)
```

Run `pytest -xv test.py` (or `make test`) to ensure you pass all the tests:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 4 items

test.py::test_exists PASSED                                              [ 25%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_default PASSED                                             [ 75%]
test.py::test_input PASSED                                               [100%]

============================== 4 passed in 0.41s ===============================
```

BDD support (Pycharm CE setup):
1. Navigate to ```features/steps/step_impl.py```

2. Navigate to behave, choose install package

3. Execute command ```behave --no-capture -f plain```

Sample output:

```
Feature: hello

  Scenario: Program exists
    Given User enters program as "hello08_formatted.py" ... passed in 0.000s
    Then Verify program "hello08_formatted.py" exists ... passed in 0.000s

  Scenario: Program is runnable
    Given User enters program as "hello08_formatted.py" ... passed in 0.001s
    Then Verify program "hello08_formatted.py" is runnable ... passed in 0.116s

  Scenario: Program is executable
    Given User enters program as "hello08_formatted.py" ... passed in 0.001s
    Then Verify program "hello08_formatted.py" is executable ... passed in 0.087s

  Scenario: Program usage
    Given User enters program as "hello08_formatted.py" ... passed in 0.001s
    Then Verify program "hello08_formatted.py" is usable with arguments "-h,--help" ... passed in 0.183s

  Scenario: Program usage with input
    Given User enters program as "hello08_formatted.py" ... passed in 0.000s
    Then Verify program "hello08_formatted.py" is executable with arguments "-n,--name" and inputs "Universe,Multi_verse" ... passed in 0.348s

1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
10 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.737s
```

