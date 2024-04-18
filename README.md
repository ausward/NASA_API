# Team_2Project
Our project will utilize at least different APIs to create software to show neat space related information.

# Build Instructions
To build and run our project, you'll need to get an NASA_API_KEY, then, building + running the Dockerfile can be done with:
You can get an API_KEY from Nasa's website from: https://api.nasa.gov/ , then, paste the API_KEY in place of the `NASA_API_KEY_GOES_HERE_WITHOUT_QUOTES` in the below commands
```
docker build -t space - < Dockerfile --no-cache

docker run -it -p 5000:5000 -e NASA_API_KEY=NASA_API_KEY_GOES_HERE_WITHOUT_QUOTES space
```
Future running of this should be easily done with:

```
docker run -it space
```

# Running our App
Once you've got the Docker container up, running and connected to, you should be in a shell, from there you *should* be able to just run:
```
poetry run space
```
That should in theory launch our app.
