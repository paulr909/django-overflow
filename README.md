[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.4-brightgreen.svg)](https://djangoproject.com)

# Django Overflow with Elasticsearch

## Django 3.0.4

Run your app in a Virtual Environment: http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python manage.py runserver
```

Run Elasticsearch:

```bash
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.0.0
```

Create Elasticsearch Index:

```bash
 curl -XPUT "localhost:9200/overflow?pretty"
```

Load Questions into Elasticsearch:

```bash
 python manage.py load_questions
```