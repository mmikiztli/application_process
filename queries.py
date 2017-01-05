from db import Database
from filters import closure
from filters import applicant_by_first_name
from filters import applicant_by_email
from filters import applicant_by_all
from filters import applicant_by_full_name
from filters import update_phone_number


def find_applicant_by_first_name(first_name):
    return [{'full_name': applicant.full_name}
            for applicant in Database.find_applicants(closure(applicant_by_first_name, first_name))]


def find_applicant_by_email(email_address):
    return [{'full_name': applicant.full_name}
            for applicant in Database.find_applicants(closure(applicant_by_email, email_address))]


def insert_and_find_applicant_by_all(other):
    Database.insert_applicant(other)
    new_applicants = Database.find_applicants(closure(applicant_by_all, other))
    return [a.__dict__ for a in new_applicants]


def update_phone_by_full_name(full_name, new_phone):
    Database.update_applicant(closure(applicant_by_full_name, full_name),
                              closure(update_phone_number, new_phone))
    updated_applicants = Database.find_applicants(closure(applicant_by_full_name, full_name))
    return [{"phone_number": a.phone_number} for a in updated_applicants]


def delete_applicants_by_email(email_address):
    Database.delete_applicants(closure(applicant_by_email, email_address))
    delete_check = Database.find_applicants(closure(applicant_by_email, email_address))
    return len(delete_check)


def list_all_mentors():
    return [{'first_name': mentors.first_name, 'last_name': mentors.last_name} for mentors in Database.get_mentors()]


def list_all_mentors_by_city(city):
    return [{'nick_name': mentors.nick_name} for mentors in Database.get_mentors() if mentors.city == city]


def greatest_favourite_number_of_mentors():
    return max(mentors.favourite_number for mentors in Database.get_mentors() if mentors.favourite_number != None)
