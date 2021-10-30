import os
from subprocess import getstatusoutput, getoutput
from behave import *


# --------------------------------------------------
@given('User enters program as "{prg}"')
def user_enters_program_as(context, prg):
    pass


# --------------------------------------------------
@then('Verify program "{prg}" exists')
def verify_program_exists(context, prg):
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
@then('Verify program "{prg}" is runnable')
def verify_program_is_runnable(context, prg):
    """Runs using python3"""

    out = getoutput(f'python {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
@then('Verify program "{prg}" is executable')
def verify_program_is_executable(context, prg):
    """Says 'Hello, World!' by default"""

    out = getoutput(f'python {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
@then('Verify program "{prg}" is usable with arguments "{args}"')
def verify_program_is_usable_with_arguments(context, prg, args):
    """usage"""

    arr = args.split(",")

    for flag in arr:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
@then('Verify program "{prg}" is executable with arguments "{args}" and inputs "{inputs}"')
def verify_program_is_executable_with_arguments_and_inputs(context, prg, args, inputs):
    """test for input"""

    arr_args = args.split(",")
    arr_inputs = inputs.split(",")

    for val in arr_inputs:
        for option in arr_args:
            rv, out = getstatusoutput(f'python {prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
