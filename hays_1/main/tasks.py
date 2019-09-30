from faker import Faker
from hays_1 import create_celery_app
from faker import Faker
from hays_1.models import Contact
from hays_1 import db

celery = create_celery_app()
fake_data = Faker()


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Runs celery periodic tasks .
    add_contact runs every 15 seconds.
    delete_contact runs every minute
    """
    sender.add_periodic_task(15.0, add_contact.s())
    sender.add_periodic_task(60.0, delete_contact.s())


@celery.task
def add_contact():
    """
    Adds a random contact to the app using Faker
    """
    contact = Contact(
        username=fake_data.first_name(),
        firstname=fake_data.last_name(),
        lastname=fake_data.first_name(),
        primary_email=fake_data.email(),
    )
    db.session.add(contact)
    db.session.commit()

    return None


@celery.task
def delete_contact():
    """
    removes a contact from  the app database
    """
    contact = Contact.query.first()
    db.session.delete(contact)
    db.session.commit()

    return None

