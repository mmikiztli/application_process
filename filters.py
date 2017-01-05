
def closure(function, value):
    return lambda element: function(element, value)


def applicant_by_all(applicant, other):
    return applicant == other


def applicant_by_id(applicant, id):
    return applicant.id == id


def applicant_by_first_name(applicant, first_name):
    return applicant.first_name == first_name


def applicant_by_email(applicant, email_address):
    return email_address in applicant.email


def applicant_by_full_name(applicant, full_name):
    return applicant.full_name == full_name


def update_phone_number(applicant, new_phone):
    applicant.phone_number = new_phone
    return applicant
