import pytest
from team2_proj.POTD import *
import json



@pytest.mark.parametrize("date, expected", [("2021-10-01", True), ("11-23-1999", False)])
def test_validate_date(date, expected):
    assert validate_date(date) == expected


def test_get_past_potd():
    date = "2023-11-29"
    expected = "A Landspout Tornado over Kansas"
    got = get_potd(date)
    print(got.get_title)
    assert got.title == expected


