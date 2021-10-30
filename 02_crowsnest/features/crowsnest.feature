Feature: crowsnest

  Scenario: Program exists
    Given User enters program as "solution.py"
    Then Verify program "solution.py" exists

  Scenario: Program usage
    Given User enters program as "solution.py"
    Then Verify program "solution.py" shows usage with arguments "-h,--help"

  Scenario: Consonant words
    Given User enters program as "solution.py"
    Then Verify program "solution.py" is executable with consonant words "brigantine, clipper, dreadnought, frigate, galleon, haddock, junk, ketch, longboat, mullet, narwhal, porpoise, quay, regatta, submarine, tanker, vessel, whale, xebec, yatch, zebrafish"

  Scenario: Vowel words
    Given User enters program as "solution.py"
    Then Verify program "solution.py" is executable with vowel words "aviso, eel, iceberg, octopus, upbound"