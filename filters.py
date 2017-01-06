from decorators import query


# A query function is a binary function that takes two arguments:
# - the first argument is the data object (applicant or mentor in this case)
# - the second argument is a value used to evaluate the data object to true or false
#
# Annotating the query function f(element, value) with @query lets the client use
# the syntax f(value) which is itself the function f(value): element -> f(element, value).
# The function f(value) can then be passed around to filter/operate on sets of data objects.

@query
def applicant_by_all(applicant, other):
    return applicant == other


@query
def applicant_by_id(applicant, id):
    return applicant.id == id


@query
def applicant_by_first_name(applicant, first_name):
    return applicant.first_name == first_name


@query
def applicant_by_email(applicant, email_address):
    return email_address in applicant.email


@query
def applicant_by_full_name(applicant, full_name):
    return applicant.full_name == full_name


@query
def update_phone_number(applicant, new_phone):
    applicant.phone_number = new_phone
    return applicant
