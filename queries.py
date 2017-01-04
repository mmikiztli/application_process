from db import Database
from filters import create_filter
from filters import applicant_by_first_name
from filters import applicant_by_email
from filters import applicant_by_all
from filters import applicant_by_full_name
from filters import update_phone_number


def find_applicant_by_first_name(first_name):
    return [{'full_name': applicant.full_name}
            for applicant in Database.find_applicants(create_filter(applicant_by_first_name, first_name))]


def find_applicant_by_email(email_address):
    return [{'full_name': applicant.full_name}
            for applicant in Database.find_applicants(create_filter(applicant_by_email, email_address))]


def insert_and_find_applicant_by_all(other):
    Database.insert_applicant(other)
    new_applicant = Database.find_applicants(
        create_filter(applicant_by_all, other))
    return [elements.__dict__ for elements in new_applicant]


def update_phone_by_full_name(full_name, new_phone):
    Database.update_applicant(create_filter(
        applicant_by_full_name, full_name), create_filter(update_phone_number, new_phone))
    return [{"phone_number": applicant.phone_number} for applicant in Database.find_applicants(create_filter(applicant_by_full_name, full_name))]


def delete_applicants_by_email(email_address):
    Database.delete_applicants(create_filter(
        applicant_by_email, email_address))
    return sum([1 for applicant in Database.find_applicants(create_filter(applicant_by_email, email_address))])


def list_all_mentors():
    return [{'first_name': mentors.first_name, 'last_name': mentors.last_name} for mentors in Database.get_mentors()]


def list_all_mentors_by_city(city):
    return [{'nick_name': mentors.nick_name} for mentors in Database.get_mentors() if mentors.city == city]


def greatest_favourite_number_of_mentors():
    return max(mentors.favourite_number for mentors in Database.get_mentors() if mentors.favourite_number != None)
