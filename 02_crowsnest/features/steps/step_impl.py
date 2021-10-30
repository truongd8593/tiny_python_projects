import os
from subprocess import getstatusoutput, getoutput
from behave import *

template = 'Ahoy, Captain, {} {} off the larboard bow!'


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
@then('Verify program "{prg}" shows usage with arguments "{args}"')
def verify_program_is_usable_with_arguments(context, prg, args):
    """usage"""

    arr = args.split(",")

    for flag in arr:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
@then('Verify program "{prg}" is executable with consonant words "{args}"')
def test_consonant(context, prg, args):

    consonant_words = args.split(", ")

    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'python {prg} {word}')
        assert out.strip() == template.format('a', word)

    """brigantine -> a Brigantine"""

    for word in consonant_words:
        out = getoutput(f'python {prg} {word.title()}')
        assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
@then('Verify program "{prg}" is executable with vowel words "{args}"')
def test_vowel(context, prg, args):

    vowel_words = args.split(", ")

    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'python {prg} {word}')
        assert out.strip() == template.format('an', word)

    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'python {prg} {word.title()}')
        assert out.strip() == template.format('an', word.title())
