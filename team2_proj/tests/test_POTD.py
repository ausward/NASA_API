import pytest
from team2_proj.team2_proj.POTD import *
import json



@pytest.mark.parametrize("date, expected", [("2021-10-01", True), ("11-23-1999", False)])
def test_validate_date(date, expected):
    assert validate_date(date) == expected




@pytest.mark.parametrize("query, expected", 
                    [("python",  WikiData(
                    title="Python",
                    description="Topics referred to by the same term",
                    url="https://en.wikipedia.org/wiki/Python",
                    thumbnail="None"
                )), 
                ("blue shift", WikiData(
                    title="Redshift",
                    description="Change of wavelength in photons during travel",
                    url="https://en.wikipedia.org/wiki/Redshift",
                    thumbnail="http://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Redshift.svg/60px-Redshift.svg.png"
                )), ("walmart", WikiData(
                    title="Walmart",
                    description="American multinational retail corporation",
                    url="https://en.wikipedia.org/wiki/Walmart",
                    thumbnail="http://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Walmart_7.jpg/60px-Walmart_7.jpg"

                ))])
def test_get_wiki_data(query: str, expected: WikiData):
    '''The banana test should fail'''
    # Test case 1: Search query provided
    search_query = query
    got = get_wiki_data(search_query)

    is_ = False
    for i in got:
        if i.__dict__ == expected.__dict__:
            is_ = True

    if expected == "banana" and is_ == False:
        is_ = True
    assert is_


@pytest.mark.parametrize("date, expected", 
                        [("2023-11-29", 'https://apod.nasa.gov/apod/image/2311/LowerLandspout_Hannon_960.jpg'),
                        ("2022-11-29", 'https://apod.nasa.gov/apod/image/2211/Gum_Lima_960.jpg'),
                        ("2021-11-29", 'https://apod.nasa.gov/apod/image/2111/LLPegasi_HubbleLodge_960.jpg')])
def test_get_potd(date, expected):
    got = get_potd(date)
    assert got.url == expected



@pytest.mark.parametrize("date, expected_result", [
    ("2024-04-22", True),
    ("2024-04-32", True),  
    ("2024-04-0", False),   
    ("2024-13-22", True),  
    ("2024/13/42", False),  
    ("2024/04/22", False),  
    ("2024.04.22", False),  
])
def test_validate_date(date, expected_result):
    assert validate_date(date) == expected_result



def test_get_potd_valid_date():
    # Assuming the function returns a POTD object
    potd = get_potd("2024-04-22")
    assert potd is not None
    assert isinstance(potd, POTD)

def test_get_wiki_data():
    # Assuming the function returns a list of WikiData objects
    wiki_data_list = get_wiki_data("blue_shift")
    assert isinstance(wiki_data_list, list)
    assert all(isinstance(data, WikiData) for data in wiki_data_list)

def test_get_POTD_with_desc():
    # Assuming the function returns a dictionary with the POTD and Wikipedia data
    data = get_POTD_with_desc()
    assert isinstance(data, dict)
    assert "POTD" in data
    assert "Query" in data
    assert "WIKI_DATA" in data

def test_get_past_POTD_with_desc():
    # Assuming the function returns a dictionary with the POTD and Wikipedia data
    data = get_past_POTD_with_desc("2024-04-22")
    assert isinstance(data, dict)
    assert "POTD" in data
    assert "Query" in data
    assert "WIKI_DATA" in data

