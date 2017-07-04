import itertools

instances = []

class Patient(object):
    """
    A Patient at TacolimClass Clinic.

    Attributes:
        id_number: Computer generated integer
        given_name: String of full given (first) name
        middle_initial: String of initial only of middle name
        family_name: String of family(last) name
        aliases: List of strings of any other known names
        dob: Date of birth
        street_address: String of street address
        street_address_2: String of street address
        city: String of city
        state_abbrev: String of state (2 letter abbreviation)
        zipcode: String of zip code
        phone_number: String of phone number
        phone_number_alt: String of alternative phone number
        insur: String of insurance name
        insur_id_number: String of insurance ID number
        insur_group_number: String of insurance Group number
        insur_phone_number: String of insurance phone number
        insur_address: String of insurance address
        emergency_contact_name: String of full name of emergency contact
        emergency_contact_phone: String of emergency contact phone number
        emergency_contact_relation: String of emergency contact relationship
        allergies: List of strings of known allergies
        dos: List of dates of service
    """

    newid = itertools.count().next

    def __init__(self, given_name, family_name, aliases,
                dob, street_address, city, state_abbrev, zipcode,
                phone_number, insur, insur_id_number, insur_group_number,
                insur_phone_number, insur_address, emergency_contact_name, emergency_contact_phone,
                emergency_contact_relation):
        self.id_number = Patient.newid()
        self.given_name = given_name
        self.middle_initial = None
        self.family_name = family_name
        self.aliases = aliases
        self.dob = dob
        self.street_address = street_address
        self.street_address_2 = None
        self.city = city
        self.state_abbrev = state_abbrev
        self.zipcode = zipcode
        self.phone_number = phone_number
        self.phone_number_alt = None
        self.insur = insur
        self.insur_id_number = insur_id_number
        self.insur_group_number = insur_group_number
        self.insur_phone_number = insur_phone_number
        self.insur_address = insur_address
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.emergency_contact_relation = emergency_contact_relation
        self.allergies = None
        self.dos = None

        instances.append(self)

charles = Patient('Charles', 'Brown', 'N/A', '01/01/1950',
                '1234 Main Place Ave', 'Harrytowne', 'VA', '22190',
                '555-123-1111', 'CAH Insurance Co', '999888CAB',
                'Group2', '555-888-9988', 'PO Box 9999 Mieville AZ 99999-9999',
                'Sally Brown', '555-123-1113', 'sister')

charles.middle_initial = 'A'

charles.street_address_2 = 'Apt B12'

charles.phone_number_alt = '555-123-1112'

charles.allergies = ['peanuts', 'pet dander',
'dust']

charles.dos = ['01/01/1950', '05/01/1959', '11/12/1971']

sally = Patient('Sally', 'Brown', 'N/A', '01/01/1953',
                '9875 Park Place Ave',  'Jonesville', 'VA', '22190',
                '555-123-1113', 'CAH Insurance Co', '999888CAB',
                'Group2', '555-888-9988', 'PO Box 9999 Mieville AZ 99999-9999',
                'Charlie Brown', '555-123-1111', 'brother')

sally.dos = ['01/01/1953', '08/31/1969', '11/12/1971']

donna = Patient('Donna', 'Brown', 'N/A', '01/01/1953',
                '1234 Main Place Ave', 'Harrytowne', 'VA', '22190',
                '555-123-1113', 'CAH Insurance Co', '999888CAB',
                'Group2', '555-888-9988', 'PO Box 9999 Mieville AZ 99999-9999',
                'Charlie Brown', '555-123-1111', 'brother')

jenna = Patient('Jenna', 'Brown', 'N/A', '01/01/1953',
                '1234 Main Place Ave', 'Harrytowne', 'VA', '22190',
                '555-123-1113', 'CAH Insurance Co', '999888CAB',
                'Group2', '555-888-9988', 'PO Box 9999 Mieville AZ 99999-9999',
                'Charlie Brown', '555-123-1111', 'brother')



for instance in Patient.instances:
    print "ID: ", id_number
    print "Name: ", given_name, middle_initial, family_name
    print "Allergies: ", allergies
    print "Phone Number: ", phone_number
