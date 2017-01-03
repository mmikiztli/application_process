
def matcher(match_function, match_data):
    return lambda value: match_function(value, match_data)

def applicant_by_all(applicant, other):
    return applicant == other

def applicant_by_id(applicant, id):
    return (applicant.id == id)

def applicant_by_first_name(applicant, first_name):
    return (applicant.first_name == first_name)

def applicant_by_email(applicant, email_address):
    return (email_address in applicant.email)

