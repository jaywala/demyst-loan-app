# demyst-loan-app

## Pre-requisites: 
The app is built and tested using python 3.10.7
(Use this same version for best results)

## Run using docker
1. Clone the repository

2. Navigate to the repository directory in your terminal and then build the docker image
```bash
docker build --tag loan_app .
```

3. Run the docker image
```bash
docker run --publish 5000:5000 loan_app
```
(if you would like to run it on a different port, you can do so by replacing <port> with your preferred port)
```bash
docker run --publish <port>:5000 loan_app
```

4. In your preferred browser open `http://127.0.0.1:5000/` or `http://127.0.0.1:<port>/` (if you opted for a different port in the previous step)

5. Follow instructions on the webpage running through the loan application. For ease of use Myob mock data provides positive income and Xero mock data provides negative income (to test both situations in preassessment calculation)

## Run from python
1. Install python dependencies from requirements.txt file
(If you work with other python projects I recommend creating a virtualenv first)
```bash
pip3 install -r requirements.txt
```

2. Run web application
```bash
flask --app loan_app --debug run 
```

3. In your preferred browser open `http://127.0.0.1:5000/`

4. Follow instructions on the webpage running through the loan application. For ease of use Myob mock data provides positive income and Xero mock data provides negative income (to test both situations in preassessment calculation)


## Testing
1. Install python dependencies from requirements.txt file
(If you work with other python projects I recommend creating a virtualenv first)
```bash
pip3 install -r requirements.txt
```

2. Run unit tests
```bash
python3 -m pytest loan_app/tests/
```

# Design
* The backend of this app is built on Python using Flask framework
* The frontend is rendered using templating. This requires server side processing as the html is rendered on server side

* This is an MVP, to productionise this app a few key things are required:
  * Recommended to switch app to "https" protocol to encrypt data in transit
  * Switch to using a DBMS. Currently the user data is stored using flask-sessions in filesystem for simplicity
  * Built using templating as only a basic frontend was required and I'm not as familiar with frontend frameworks. A frontend framework as well as client side rendering should be considered especially if scaling to a large number of users
    * Caveats of server side rendering is that it requires more processing on the server and as a result the server will not scale as well to larger number of users. However advantages are the website is more inclusive as it doesn't rely as much on the client's device and it's processing power to be responsive
  * Consider improving the frontend with styling and ensuring it works across differnet devices well
  * Deploy to a cloud/dedicated server
