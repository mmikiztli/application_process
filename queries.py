from db import Database
from filters import applicant_by_first_name
from filters import applicant_by_email
from filters import applicant_by_all
from filters import applicant_by_full_name
from filters import update_phone_number


# utilities for the silly output that's required

def full_names(applicants):
    return [{'full_name': a.full_name} for a in applicants]


def phone_numbers(applicants):
    return [{'phone_number': a.phone_number} for a in applicants]


def first_last_names(mentors):
    return [{'first_name': m.first_name, 'last_name': m.last_name} for m in mentors]


def nicknames(mentors):
    return [{'nick_name': m.nick_name} for m in mentors]


# queries

def find_applicant_by_first_name(first_name):
    return full_names(Database.find_applicants(applicant_by_first_name(first_name)))


def find_applicant_by_email(email_address):
    return full_names(Database.find_applicants(applicant_by_email(email_address)))


def insert_and_find_applicant_by_all(other):
    Database.insert_applicant(other)
    new_applicants = Database.find_applicants(applicant_by_all(other))
    return [a.__dict__ for a in new_applicants]


def update_phone_by_full_name(full_name, new_phone):
    Database.update_applicants(applicant_by_full_name(full_name),
                               update_phone_number(new_phone))
    return phone_numbers(Database.find_applicants(applicant_by_full_name(full_name)))


def delete_applicants_by_email(email_address):
    Database.delete_applicants(applicant_by_email(email_address))
    return len(Database.find_applicants(applicant_by_email(email_address)))


def list_all_mentors():
    return first_last_names(Database.get_mentors())


def list_all_mentors_by_city(city):
    return nicknames([m for m in Database.get_mentors() if m.city == city])


def greatest_favourite_number_of_mentors():
    return max(m.favourite_number for m in Database.get_mentors() if m.favourite_number is not None)

