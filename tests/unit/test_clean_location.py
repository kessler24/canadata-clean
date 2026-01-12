"""
A test module for the location cleaning functions.
"""
import pytest
import pandas as pd
from canadata_clean.clean_location import clean_location

# create pt_tests file with column for long-forms and column for two letter code.
@pytest.fixture
def pt_tests():
    file_path = "tests/pt_tests.csv"
    # with open(file_path, 'r') as file:
    #     lines = file.readlines()
    data = pd.read_csv(file_path)
    return data

# create mun_tests file with column for uncleaned and column for cleaned municipality names.
@pytest.fixture
def mun_tests():
    file_path = "tests/mun_tests.csv"
    data = pd.read_csv(file_path)
    return data

def test_clean_location():
    """
    Test that clean_location works as expected.
    """
    out = clean_location("N Van British Columbia")
    expected_out = "North Vancouver, BC"
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_capitalization():
    # test that things get correctly title cased
    return

def test_spaces():
    # test that the number and location of spaces makes sense
    return

def test_format():
    # test that the output format is "municipality, two-letter-province/territory-code" using regex
    return

def test_output_type():
    # test that the function outputs a string
    return

def test_wrong_input_type():
    # test that an incorrect input type throws a typeerror
    return

def test_unidentified_province_territory():
    # check that an unidentified province/territory input throws an error
    return

def test_unidentified_municipality():
    # check that an unidentified municipality raises a warning and still returns the cleaned string
    return

def test_province_territory(pt_tests):
    # loop through each row of pt_tests
    # create sample line with long form
    # run sample line through clean_location and check short form matches
    return

def test_municipality(mun_tests):
    # loop through each row of mun_tests
    # create sample line with uncleaned city + province code
    # run sample line through clean_location and check city matches expected cleaned city
    return