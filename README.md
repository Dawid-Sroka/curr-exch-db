## Currency exchange database

The `currapp` django application allows to view currencies and currency exchange rates stored in the local database.

To get started, execute the following commands:

```
git clone git@github.com:Dawid-Sroka/curr-exch-db.git
cd curr-exch-db
python -m venv .venv
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then simply visit `http://127.0.0.1:8000/currency/fetch` to load the data from https://github.com/ranaroussi/yfinance API.
