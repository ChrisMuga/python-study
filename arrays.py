people = {
   
   'Chris': {
            'id'        :   123456,
            'age'       :   23,
            'location'  :   'Buruburu'

            },
    'Tom': {
            'id'        :   9876543,
            'age'       :   24,
            'location'  :   'Lights'
            
            }
}
print(people)
print(people['Chris'])
#print(people['name'])

new_person = {
    'Tiffany': {
            'id'        :   98746543,
            'age'       :   18,
            'location'  :   'City Lights'
            
            }
}

people.update(new_person)
print(people)