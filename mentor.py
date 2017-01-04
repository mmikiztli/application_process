class Mentor():

    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.nick_name = raw_data[3]
        self.phone_number = raw_data[4]
        self.email = raw_data[5]
        self.city = raw_data[6]
        self.favourite_number = raw_data[7]

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
