from quart import Quart, jsonify, request
import requests
from .POTD import *

app = Quart(__name__)

@app.route('/nasa')
async def get_nasa_data():
    nasa_api_url = 'https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY'
    response = requests.get(nasa_api_url)
    data = response.json()
    return jsonify(data)

@app.route('/wikipedia/<keyword>')
async def get_wikipedia_data(keyword):
    wikipedia_api_url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{keyword}'
    response = requests.get(wikipedia_api_url)
    data = response.json()
    if 'title' not in data:
        return jsonify({'error': 'No Wikipedia page found'})
    return jsonify(data)

@app.route('/POTD')
async def get_potd():
    return jsonify(get_POTD_with_desc())
    

def main():
    app.run(host="0.0.0.0", port=5000)
    @app.route('/spacefact/<keyword>')
    async def get_space_fact(keyword):
        nasa_api_url = f'https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY&search={keyword}'
        response = requests.get(nasa_api_url)
        data = response.json()
        if 'error' in data:
            return jsonify({'error': 'No space fact found'})
        return jsonify(data)

    @app.route('/wikipedia/<keyword>')
    async def get_wikipedia_data(keyword):
        wikipedia_api_url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{keyword}'
        response = requests.get(wikipedia_api_url)
        data = response.json()
        if 'title' not in data:
            return jsonify({'error': 'No Wikipedia page found'})
        return jsonify(data)



if __name__ == '__main__':
    main()
