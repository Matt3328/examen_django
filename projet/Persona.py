data = [{
"first_name":"Ilyès",
"last_name":"Fleury",
"address_street":"Rue Paul Bert",
"address_number":73,
"city":"Dunkerque",
"postcode":12681
},{
"first_name":"Lia",
"last_name":"Dumont",
"address_street":"Rue Louis-Blanqui",
"address_number":30,
"city":"Lille",
"postcode":63996
},{
"first_name":"Eléonore",
"last_name":"Caron",
"address_street":"Avenue du Château",
"address_number":87,
"city":"Rennes",
"postcode":78482
},{
"first_name":"Eva",
"last_name":"Girard",
"address_street":"Rue du Bon-Pasteur",
"address_number":9,
"city":"Rueil-Malmaison",
"postcode":23879
}]


class Persona:
    def __init__(self,first_name = 'Emilien', last_name = 'Duval'):
        self._first_name = first_name
        self._last_name = last_name
 
    def __str__(self):
        return "Hi ! I'm " + self._first_name + " " + self._last_name + "."

    def set_adress(self, address_street, address_number, city, postcode):
    	self.address_street = address_street
    	self.address_number = address_number
    	self.city = city
    	self.postcode = postcode   

    def show_address(self):
    	return f"My full address is : {self.address_number}  {self.address_street} , {self.city} ({self.postcode})"
 
test = Persona()
test.set_adress("chemin", "24", "Avensan", "33480")
print(test.show_address())

for i in data:
	test = Persona(i["first_name"],i["last_name"])
	print(test)
	test.set_adress(i["address_street"], i["address_number"], i["city"], i["postcode"])
	print(test.show_address())
	print("--")