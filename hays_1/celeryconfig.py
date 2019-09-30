from celery.schedules import crontab


# CELERY_IMPORTS = ('hays_1.main.tasks')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = "Europe/London"

CELERY_ACCEPT_CONTENT = ["json", "msgpack", "yaml"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

"""
CELERYBEAT_SCHEDULE = {
    "add-contacts": {
        "task": "hays_1.main.tasks.add_contact",
        # Every minute
        "schedule": 30.0,
    },
    "delete-contacts": {
        "task": "hays_1.main.tasks.delete_contact",
        # Every minute
        "schedule": 60.0,
    }
}
"""
