Feature: hello

  Scenario: Program exists
    Given User enters program as "hello08_formatted.py"
    Then Verify program "hello08_formatted.py" exists

  Scenario: Program is runnable
    Given User enters program as "hello08_formatted.py"
    Then Verify program "hello08_formatted.py" is runnable

  Scenario: Program is executable
    Given User enters program as "hello08_formatted.py"
    Then Verify program "hello08_formatted.py" is executable

  Scenario: Program usage
    Given User enters program as "hello08_formatted.py"
    Then Verify program "hello08_formatted.py" is usable with arguments "-h,--help"

  Scenario: Program usage with input
    Given User enters program as "hello08_formatted.py"
    Then Verify program "hello08_formatted.py" is executable with arguments "-n,--name" and inputs "Universe,Multi_verse"