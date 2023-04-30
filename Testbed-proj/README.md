# Deployment of MEC app
### 1. Build a Docker container with MEC app
cd to Testbed-proj/
'''docker build -t tstbed-app .'''
You can check that the tstbed-app image was created:
'''docker image ls | grep tstbed-app

### 2. Deploy the containerized MEC app to 
```shelldocker run -d -p 5000:5000 --network demo-oai-public-net tstbed-app
```
You can check that the app is running properly in your web browser: [http://tstbed-app.org:5000/hello]

### 3. Register your MEC app as a MEC service
* Note: this is only necessary if you want other MEC applications to be able to consume your app's services or if you want to have it routable under the oai-mep.org domain.
Access to swagger UI of the `Mp1` interface on the Platform: [http://192.168.70.5/v1/ui/#/default/get_services]
Now you need to register your app properly under '/register' using a 'POST' request.
**WARNING:** Simply editing the example `.json` won't work, under `sid` you need to add a `uid` to avoid confusing the database. (You can choose any `uid`).
A successful request body might look like this:
```shell
{
  "description": "testing registry with sample flask",
  "endpoints": [
    {
      "description": "hello",
      "method": "GET",
      "name": "hello",
      "path": "/v1/hello"
    }
  ],
  "host": "tstbed-app.org",
  "name": "tstbed-app",
  "path": "/v1/flask-app",
  "port": 5000,
  "sid": "sid",
  "uid": "tstbedUID",
  "type": "ML"
}
```

Now you can access your MEC app under the oai-mep domain: [http://oai-mep.org/tstbed-app/]