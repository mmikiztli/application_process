class Mentor():

    def __init__(self, id, first_name, last_name, nick_name, phone_number, email, city, favourite_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.phone_number = phone_number
        self.email = email
        self.city = city
        self.favourite_number = favourite_number

    # Return the 2 name property of all the mentors
    # returns: list of dictionaries
    # example: [{
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson'
    # }, ...]
    @classmethod
    def _1_list_mentors(cls):
        from queries import list_all_mentors
        return list_all_mentors()

    # Return the nick_name property of all the mentors located in Miskolc
    # returns: list of dictionaries
    # example: [{
    #    nick_name: 'Billy'
    # }, ...]
    @classmethod
    def _2_list_mentors_from_miskolc(cls):
        from queries import list_all_mentors_by_city
        return list_all_mentors_by_city("Miskolc")

    # Return the highest favourite number of all mentors
    # returns: integer
    # example: 927
    @classmethod
    def _3_greatest_favourite_number(cls):
        from queries import greatest_favourite_number_of_mentors
        return greatest_favourite_number_of_mentors()
