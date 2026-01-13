from canadata_clean.clean_date import clean_date

def test_whitespace():
    out = clean_date(" 1991-10-20")
    expected_out = "1991-10-20"
    assert  out == expected_out, f"Expected {expected_out} but got {out}"
