# DRF Quickstart
Yet another simple API built using the DRF quickstart docs.

## Download the Zip or Clone this repo:
```
git clone https://github.com/aprakash7/drf-quickstart.git
```

## Change directory
```
cd drf-quickstart
```

## Create a virtualenv and install the dependencies (recommended)
```
python -m venv drf
```
## Activate the venv
On Mac 
```
source drf/bin/activate
```

On Windows
```
.\drf\scripts\activate
```

## Installation
```
pip install -r requirements.txt
```

## Perform migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Create superuser
```
python manage.py createsuperuser
```
## Run the server!
```
python manage.py runserver
```

### Head over to ```http://127.0.0.1:8000/users/``` and test the api! :)
