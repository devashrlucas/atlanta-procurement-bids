# Atlanta Procurement Bids (Services) Viewer

This project can be used as a quicker way to view all of the services solicitations available on the Department of Procurement’s website for the City of Atlanta. One solicitation is shown per page. Refreshing the page will show the next solicitation from the “Choose a solicitation” dropdown menu.

As of right now, there is no way to go back and view previously seen solications. If you see a solication that you would like to look at later, please be sure to save the url for that solication found above the title of the solicitation. Any required bid documents will need to be downloaded from the original url as well.


## Getting Started

Download the ZIP file from the repository and unzip the files. In a command-line shell, change into the directory containing the project files by doing the following:

```
$ cd /path/to/atlanta-procurement-bids-master
```

### Requirements

* Python 2.7
* [ChromeDriver] (https://sites.google.com/a/chromium.org/chromedriver/) for Selenium

### How To Use

Install required dependencies:

```
$ pip install -r requirements.txt
```

This project is meant to be run inside of a virtual environment. To run the included virtual environment, use the following commands:

```
$ cd myvenv
$ source ./bin/activate
```

Change into the directory containing the application files:

```
$ cd services
```

To run the Flask application, use the following commands:

```
$ export FLASK_APP=/path/to/services_app.py
$ export FLASK_DEBUG=0
$ flask run
```

Once the app is running on your local server (check command-line shell), please visit [http://localhost:5000/] (http://localhost:5000/) in the browser of your choice. Please leave the app running on your local server while you view the solicitations.

To quit running the app on your local server, press CTRL+C in the command-line shell.



