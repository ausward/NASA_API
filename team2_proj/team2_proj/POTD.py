
import json
import requests
import os
import jsonify


# for the NASA API to work you need to get an API key from the NASA website and set it as an environment variable
#  get key here ->      https://api.nasa.gov/
# in poetry shell run -> export NASA_API_KEY="your_key_"


# AW 2/29/24
# POTD -> photo of the day

class POTD:
    url:str
    title:str
    desc:str

    def __init__(self, url:str, title:str, desc:str = None):
        self.url = url
        self.title = title
        self.desc = desc
    
    def get_title(self) -> str:
        return self.title
    
    def no_desc(self):
        return {
            "url": self.url,
            "title": self.title
        }

    
class WikiData:
    title:str
    description:str
    url:str
    thumbnail:str

    def __init__(self, title:str = None, description:str = None, url:str = None, thumbnail:str = None):
        self.title = title
        self.description = description
        self.url = url
        self.thumbnail = thumbnail

    def __str__(self) -> str:
        return f"Title: {self.title}, Description: {self.description}, URL: {self.url}, Thumbnail: {self.thumbnail}"


def get_potd() -> POTD:
    baseURL = "https://api.nasa.gov/planetary/apod"
    apiKey = os.getenv("NASA_API_KEY")
    params = {
        "api_key": apiKey,
        
    }
    response = requests.get(baseURL, params=params)
    json_data = response.json()
    try:
        POTD_obj = POTD(json_data["url"], json_data["title"], json_data['explanation'] )
        data = json.dumps(POTD_obj.__dict__)
    except:
        print(json_data)
    
    return POTD_obj



def get_wiki_data(search_query:str = "blue_shift")-> list[WikiData]:
    language_code = "en"
    
    number_of_results = 5
    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url,  params=parameters)
    list_of_wiki_data = []
    for result in response.json()["pages"]:
        # print(result)
        try:
            title = result["title"]
            description = result["description"]
            url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            if result['thumbnail'] == None:
                thumbnail = 'None' 
            else:
                thumbnail ="http://"+ result["thumbnail"]["url"][2:]
            wiki_data = WikiData(title, description, url, thumbnail)
            list_of_wiki_data.append(wiki_data)
        except:
            print(result)
        
    return list_of_wiki_data




def get_POTD_with_desc():
    NASA_data:POTD = get_potd()
    WIKI_DATA:list[WikiData] = get_wiki_data(NASA_data.get_title())
    return_data =  {
        "POTD": NASA_data.__dict__,
        "info": "Get More context from Wikipedia.",
        "WIKI_DATA": [data.__dict__ for data in WIKI_DATA]
    }
    return return_data
    # return json.dumps(return_data)


def get_POTD_without_desc():
    NASA_data:POTD = get_potd()
    WIKI_DATA:list[WikiData] = get_wiki_data(NASA_data.get_title())
    return_data =  {
        "POTD": NASA_data.no_desc(),
        "info": "Get More context from Wikipedia.",
        "WIKI_DATA": [data.__dict__ for data in WIKI_DATA]
    }
    return return_data
    

if __name__ == "__main__":
    print(get_POTD_with_desc())