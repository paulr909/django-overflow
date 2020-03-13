[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.4-brightgreen.svg)](https://djangoproject.com)

# Django Overflow with Elasticsearch

## Django 3.0.4

Run your app in a Virtual Environment: http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html

Install the requirements:

```
pip install -r requirements.txt
```

Run the development server:

```
python manage.py runserver
```

Run Elasticsearch:

```
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --name overflow_es docker.elastic.co/elasticsearch/elasticsearch:6.0.0
```

Check Elasticsearch is running:

```
curl -XGET http://localhost:9200
```

Create Elasticsearch Index:

```
curl -XPUT "localhost:9200/overflow?pretty"
```

Load Questions into Elasticsearch:

```
python manage.py load_questions
```

Run tests with coverage:

```
python manage.py test
```

Use elasticsearch==6.0.0 as v7 breaks (multiple id's created)
