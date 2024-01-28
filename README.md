# gjango_moex_api
Simple service for requesting USD to RUB rate from MOEX Informational &amp; Statistical Server. Python 3.12 + Django

## Requirements
- Python 3.12
- Poetry

## Installation
- clone repository
- install dependencies
- run server
```
git clone https://github.com/firepanda70/django_moex_api
cd django_moex_api
poetry install
poetry run python django_moex_api/manage.py runserver
```

## Usage
- Endpoint ```/http://127.0.0.1:8000/get-current-usd/``` will be avaliable after startup. Data returns with 10 seconds caching. ```history``` saves up to 10 last responses, clears after restart. Response example:
```
{
    "last": {
        "rate": 89.7375,
        "request_datetime": "2024-01-29T00:40:24.259"
    },
    "history": [
        {
            "rate": 89.7375,
            "request_datetime": "2024-01-29T00:39:57.918"
        },
        {
            "rate": 89.7375,
            "request_datetime": "2024-01-29T00:40:10.602"
        },
        {
            "rate": 89.7375,
            "request_datetime": "2024-01-29T00:40:24.259"
        }
    ]
}
```

## Technologies
- Python 3.12
- Poetry
- Django
