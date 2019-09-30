from flask import Flask, redirect, url_for, request, Blueprint, jsonify
from werkzeug.urls import url_parse

from hays_1.models import Contact, OtherEmail

from hays_1 import db

contact = Blueprint("contact", __name__)


@contact.route("/new_contact", methods=("GET", "POST"))
def new_contact():
    """
        Create new contact
    """
    payload = request.get_json()

    contact = Contact(
        username=payload["username"],
        firstname=payload["firstname"],
        lastname=payload["lastname"],
        primary_email=payload["primary_email"],
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify({"message": "new contact created"})


@contact.route("/contacts", methods=["GET", "POST"])
def contacts():
    """
    Show alls contacts
    """
    contacts = Contact.query.all()
    output = []

    for contact in contacts:
        contact_data = {}
        contact_data["username"] = contact.username
        contact_data["firstname"] = contact.firstname
        contact_data["lastname"] = contact.lastname
        contact_data["primary_email"] = contact.primary_email
        output.append(contact_data)

    return jsonify({"contacts": output})


@contact.route("/contact/<username>", methods=["GET", "POST"])
def find_contact(username):
    """
    find a  contact
    :param username: username from contact
    """
    contact = Contact.query.filter_by(username=str(username)).first()

    if not contact:
        return jsonify({"message": "no user found !"})

    contact_data = {}
    contact_data["username"] = contact.username
    contact_data["firstname"] = contact.firstname
    contact_data["lastname"] = contact.lastname
    contact_data["primary_email"] = contact.primary_email

    return jsonify({"contact": contact_data})


@contact.route("/contacts/<username>/", methods=["DELETE"])
def contacts_delete(username):
    """
    Delete contact
    """

    try:
        contact = Contact.query.filter_by(username=str(username)).first()
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "deleted contact"})
    except:
        db.session.rollback()
        return jsonify({"message": "error. contact not deleted"})


@contact.route("/edit_contact/<username>/", methods=["PUT"])
def edit_contact(id):
    """
    Edit contact
    :param id: Id from contact
    """
    data = request.get_json()
    try:
        contact = Contact(
            username=payload["username"],
            firstname=payload["firstname"],
            lastname=payload["lastname"],
            primary_email=payload["primary_email"],
        )
        return jsonify({"message": "updated"})
    except:
        db.session.rollback()
        return jsonify({"message": "error. contact not updated"})


@contact.route("/contacts/add_email", methods=["PUT"])
def add_email():
    """
     add email
    :param id: Id from contact
    """

    payload = request.get_json()
    username = payload["username"]

    contact = Contact.query.filter_by(username=str(username)).first()

    try:

        email = OtherEmail(address=data["address"], contact_id=contact.id)
        db.session.add(email)
        db.session.commit()
        # User info
        return jsonify({"message": "New emaill added"})
    except:
        db.session.rollback()
        return jsonify({"message": "error . not added"})
