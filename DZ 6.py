from marshmallow import Schema, fields, validate, post_load, ValidationError
import json
import os




save = r"C:\Users\nekit\Desktop\Telebot\Settings"

# ---------------------------------
class User(object):
    def __init__(self, name, year, aname):
        self.name = name
        self.year = year
        self.aname = aname

    def __repr__(self):
        return f'Книга называется {self.name}, и была написана в {self.year} году автором по имени {self.aname}'

class UserSchema(Schema):
    name = fields.String(missing='Unknown', default='Unknown', valdiate=validate.Length(min=1)) # Дает дефолт значения
    year = fields.Integer(required=True, error_messages={'required': 'enter year '}, validate=validate.Range(min=0, max=None)) #  обязательно заполнить
    aname = fields.String(required=False, valdiate=validate.Length(min=1))


    @post_load
    def make(self, data, **kwargs):
        return User(**data)

# ---------------------------------
try:
    data = json.load(open("Te.json", "r"))
    users = UserSchema().load(data)
except ValidationError as e:
    print(f'\nError Msg: {e.messages}')
    print(f'Valid Data: {e.valid_data}')

try:
    data = json.load(open(save, "r"))
    users = UserSchema().load(data)
    print("\n" + str(users) + " - сохраненно\n")
except ValidationError as e:
    print(f'Error Msg: {e.messages}')
    print(f'Valid Data: {e.valid_data}\n')

# ---------------------------------

class JSONAble(object):
    def __init__(self):
        '''
        Constructor
        '''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getValue(self, v):
        if (hasattr(v, "asJSON")):
            return v.asJSON()
        elif type(v) is dict:
            return self.reprDict(v)
        elif type(v) is list:
            vlist = []
            for vitem in v:
                vlist.append(self.getValue(vitem))
            return vlist
        else:
            return v

    def reprDict(self, srcDict):

        d = dict()
        for a, v in srcDict.items():
            d[a] = self.getValue(v)
        return d

    def asJSON(self):

        return self.reprDict(self.__dict__)

data = JSONAble()
try:
    data.name = input("Название книги\n")
    data.year = int(input("год написания\n"))
    data.aname = input("Автор:")
except ValueError:
    print("ошибка")

user = data.asJSON()

# ---------------------------------

try:
    users = UserSchema().load(user)
except ValidationError as e:
    print(f'Error Msg: {e.messages}')
    print(f'Valid Data: {e.valid_data}')
finally:
    print(users)

# ---------------------------------


with open(save, 'w') as outfile:
    json.dump(user, outfile)

# ---------------------------------

with open(save) as json_file:
    users = json.load(json_file)
    print(users)








