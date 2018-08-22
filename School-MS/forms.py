from wtforms import Form, BooleanField, StringField, validators, DateTimeField


class Registration(Form):
    name = StringField('Last Name', [validators.Length(min=4, max=25)])
    surname = StringField('First Name', [validators.Length(min=4, max=25)])
    dob = DateTimeField('Date of Birth', format='%m/%d/%y')
    sex = StringField('Sex')
    level = StringField('Class')
    guardian = StringField('Parent or Guardian Name')
    address = StringField('Telephone or Guardian Address')
    pwd = StringField('Online Account Password')
    photoUrl = StringField('Photo')


class Search(Form):
    name = StringField('Last Name', [validators.Length(min=4, max=25)])
    surname = StringField('First Name', [validators.Length(min=4, max=25)])
    level = StringField('Class')
    guardian = StringField('Parent or Guardian Name')


class Classlist(Form):
    level = StringField('Class')


class Finance(Form):
        receiptNumber = StringField('Receipt Number')
        name = StringField('Last Name', [validators.Length(min=4, max=25)])
        surname = StringField('First Name', [validators.Length(min=4, max=25)])
        level = StringField('Class')
        paid = StringField('Amount Paid')
        owing = StringField('Amount Owing')


class Contact(Form):
    name = StringField('Last Name', [validators.Length(min=4, max=25)])
    surname = StringField('First Name', [validators.Length(min=4, max=25)])
    level = StringField('Class')
    message = StringField('Message')
    address = StringField('Telephone or Address')
