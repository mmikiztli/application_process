from copy import deepcopy
from mentor import Mentor
from applicant import Applicant


class Database:

    mentors_data = [
        Mentor([1, 'Attila', 'Molnár', 'Atesz', '003670/630-0539', 'attila.molnar@codecool.com', 'Miskolc', 23]),
        Mentor([2, 'Pál', 'Monoczki', 'Pali', '003630/327-2663', 'pal.monoczki@codecool.com', 'Miskolc', None]),
        Mentor([3, 'Sándor', 'Szodoray', 'Szodi', '003620/519-9152', 'sandor.szodoray@codecool.com', 'Miskolc', 7]),
        Mentor([4, 'Dániel', 'Salamon', 'Dani', '003620/508-0706', 'daniel.salamon@codecool.com', 'Budapest', 4]),
        Mentor([5, 'Miklós', 'Beöthy', 'Miki', '003630/256-8118', 'miklos.beothy@codecool.com', 'Budapest', 42]),
        Mentor([6, 'Tamás', 'Tompa', 'Tomi', '003630/370-0748', 'tamas.tompa@codecool.com', 'Budapest', 42]),
        Mentor([7, 'Mateusz', 'Ostafil', 'Mateusz', '003648/518-664-923', 'mateusz.ostafil@codecool.com', 'Krakow', 13])
    ]

    applicants_data = [
        Applicant([1, 'Dominique', 'Williams', '003630/734-4926', 'dolor@laoreet.co.uk', 61823]),
        Applicant([2, 'Jemima', 'Foreman', '003620/834-6898', 'magna@etultrices.net', 58324]),
        Applicant([3, 'Zeph', 'Massey', '003630/216-5351', 'a.feugiat.tellus@montesnasceturridiculus.co.uk', 61349]),
        Applicant([4, 'Joseph', 'Crawford', '003670/923-2669', 'lacinia.mattis@arcu.co.uk', 12916]),
        Applicant([5, 'Ifeoma', 'Bird', '003630/465-8994', 'diam.duis.mi@orcitinciduntadipiscing.com', 65603]),
        Applicant([6, 'Arsenio', 'Matthews', '003620/804-1652', 'semper.pretium.neque@mauriseu.net', 39220]),
        Applicant([7, 'Jemima', 'Cantu', '003620/423-4261', 'et.risus.quisque@mollis.co.uk', 10384]),
        Applicant([8, 'Carol', 'Arnold', '003630/179-1827', 'dapibus.rutrum@litoratorquent.com', 70730]),
        Applicant([9, 'Jane', 'Forbes', '003670/653-5392', 'janiebaby@adipiscingenimmi.edu', 56882]),
        Applicant([10, 'Ursa', 'William', '003620/496-7064', 'malesuada@mauriseu.net', 91220])
    ]

    @classmethod
    def get_mentors(cls):
        return [deepcopy(mentor) for mentor in cls.mentors_data]

    @classmethod
    def get_applicants(cls):
        return [deepcopy(applicant) for applicant in cls.applicants_data]

    @classmethod
    def find_applicants(cls, condition):
        return [deepcopy(applicant) for applicant in cls.applicants_data if condition(applicant)]

    @classmethod
    def insert_applicant(cls, applicant):
        cls.applicants_data.append(deepcopy(applicant))

    @classmethod
    def update_applicant(cls, condition, update_operation):
        for applicant in cls.applicants_data:
            if condition(applicant):
                update_operation(applicant)

    @classmethod
    def delete_applicants(cls, condition):
        cls.applicants_data = [applicant for applicant in cls.applicants_data if not condition(applicant)]

