class Applicant():

    def __init__(self, id, first_name, last_name, phone_number, email, application_code):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.application_code = application_code

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    # Return the full name, as a full_name property of all the applicants, whose name is Carol
    # returns: list of dictionaries
    # example: [{
    #    full_name: 'Carol James'
    # }, ...]
    @classmethod
    def _4_specific_applicant_by_first_name(cls):
        from queries import find_applicant_by_first_name
        return find_applicant_by_first_name('Carol')

    # Return the full name, as a full_name property of all the applicants, whose email ends with '@adipiscingenimmi.edu'
    # returns: list of dictionaries
    # example: [{
    #    full_name: 'Ipis Blud'
    # }, ...]
    @classmethod
    def _5_specific_applicant_by_email_domain(cls):
        from queries import find_applicant_by_email
        return find_applicant_by_email('@adipiscingenimmi.edu')

    # Insert a the Applicant into Database.applicants_data,
    # and return a filtered list, where we only add the data of Markus.
    # The data of the new applicant:
    #   id: 11
    #   first_name: 'Markus'
    #   last_name: 'Schaffarzyk'
    #   phone_number: '003620/725-2666'
    #   email: 'djnovus@groovecoverage.com'
    #   application_code: 54823
    # returns: list of dictionaries (one dictionary, as the list should be filtered)
    # example return value: [{
    #    id: 500
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson',
    #    phone_number: '003670/123-4567'
    #    email: 'bill@wilkins.on'
    #    application_code: 54823
    # }]
    @classmethod
    def _6_inserting_a_new_applicant(cls):
        from queries import insert_and_find_applicant_by_all
        return insert_and_find_applicant_by_all(Applicant(11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823))

    # Update an Applicant in the applicants_data, and returns a filtered dictionary list for checking.
    # Story: Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
    # example return value: [{
    #    phone_number: '003670/223-7459'
    # }]
    @classmethod
    def _7_updating_data(cls):
        from queries import update_phone_by_full_name
        return update_phone_by_full_name("Jemima Foreman", '003670/223-7459')

    # Delete lines from the applicants_data, based on a filter condition
    # Story: Arsenio, an applicant called us, that he and his friend applied to Codecool.
    # They both want to cancel the process, because they got an investor for the site they run: mauriseu.net
    # Logic: remove all the applicants, who applied with emails for this domain.
    #       (e-mail address has this domain after the @ sign)
    # returns: integer (number of occurences of the @mauriseu.net e-mail domains)
    # example: 2
    @classmethod
    def _8_deleting_applicants(cls):
        from queries import delete_applicants_by_email
        return delete_applicants_by_email("@mauriseu.net")
