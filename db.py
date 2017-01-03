from mentor import Mentor
from applicant import Applicant

class Database():
    mentors_data = [
        [1, 'Attila', 'Molnár', 'Atesz', '003670/630-0539', 'attila.molnar@codecool.com', 'Miskolc', 23],
        [2, 'Pál', 'Monoczki', 'Pali', '003630/327-2663', 'pal.monoczki@codecool.com', 'Miskolc', None],
        [3, 'Sándor', 'Szodoray', 'Szodi', '003620/519-9152', 'sandor.szodoray@codecool.com', 'Miskolc', 7],
        [4, 'Dániel', 'Salamon', 'Dani', '003620/508-0706', 'daniel.salamon@codecool.com', 'Budapest', 4],
        [5, 'Miklós', 'Beöthy', 'Miki', '003630/256-8118', 'miklos.beothy@codecool.com', 'Budapest', 42],
        [6, 'Tamás', 'Tompa', 'Tomi', '003630/370-0748', 'tamas.tompa@codecool.com', 'Budapest', 42],
        [7, 'Mateusz', 'Ostafil', 'Mateusz', '003648/518-664-923', 'mateusz.ostafil@codecool.com', 'Krakow', 13]
    ]

    applicants_data = [
        [1, 'Dominique', 'Williams', '003630/734-4926', 'dolor@laoreet.co.uk', 61823],
        [2, 'Jemima', 'Foreman', '003620/834-6898', 'magna@etultrices.net', 58324],
        [3, 'Zeph', 'Massey', '003630/216-5351', 'a.feugiat.tellus@montesnasceturridiculus.co.uk', 61349],
        [4, 'Joseph', 'Crawford', '003670/923-2669', 'lacinia.mattis@arcu.co.uk', 12916],
        [5, 'Ifeoma', 'Bird', '003630/465-8994', 'diam.duis.mi@orcitinciduntadipiscing.com', 65603],
        [6, 'Arsenio', 'Matthews', '003620/804-1652', 'semper.pretium.neque@mauriseu.net', 39220],
        [7, 'Jemima', 'Cantu', '003620/423-4261', 'et.risus.quisque@mollis.co.uk', 10384],
        [8, 'Carol', 'Arnold', '003630/179-1827', 'dapibus.rutrum@litoratorquent.com', 70730],
        [9, 'Jane', 'Forbes', '003670/653-5392', 'janiebaby@adipiscingenimmi.edu', 56882],
        [10, 'Ursa', 'William', '003620/496-7064', 'malesuada@mauriseu.net', 91220]
    ]

    @classmethod
    def get_mentors(cls):
        return [Mentor(raw_mentor) for raw_mentor in cls.mentors_data]

    @classmethod
    def get_applicants(cls):
        return [Applicant(raw_applicant) for raw_applicant in cls.applicants_data]

    @classmethod
    def find_matching_applicants(cls, matcher):
        return [Applicant(raw_applicant) for raw_applicant in cls.applicants_data if matcher(Applicant(raw_applicant))]

    @classmethod
    def find_matching_mentors(cls, matcher):
        return [Mentor(raw_mentor) for raw_mentor in cls.mentors_data if matcher(Applicant(raw_mentor))]

    @classmethod
    def insert_applicant(cls, applicant):
        cls.applicants_data.append(cls._raw_applicant(applicant))

    @classmethod
    def insert_mentor(cls, mentor):
        cls.mentors_data.append(cls._raw_mentor(mentor))

    @classmethod
    def delete_applicants(cls, matcher):
        cls.applicants_data = [raw_applicant for raw_applicant in cls.applicants_data if matcher(Applicant(raw_applicant))]

    @classmethod
    def delete_mentors(cls, matcher):
        cls.mentors_data = [raw_mentor for raw_mentor in cls.mentors_data if matcher(Applicant(raw_mentor))]

    @classmethod
    def _raw_applicant(cls, applicant):
        return [applicant.id,
                applicant.first_name,
                applicant.last_name,
                applicant.phone_number,
                applicant.email,
                applicant.application_code]

    @classmethod
    def _raw_mentor(cls, mentor):
        return [mentor.id,
                mentor.first_name,
                mentor.last_name,
                mentor.nick_name ,
                mentor.phone_number,
                mentor.email,
                mentor.city,
                mentor.favourite_number]
