# haysApp
Contact Management REST Api.

# Installing
```
cd IQVIA_RESTapi
pip install requirements.txt
python run.py
```

# Test
```
Pytest -v
```

# Celery
* Assumes Redis is running.
```
celery beat -A hays_1.main.tasks
celery worker -A hays_1.main.tasks
```
