def create_record(name, telephone, address):
    """Creates record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record


user1 = create_record('Vasya','+79865432187','Russia')
user2 = create_record('Peter','+63219864837', 'America')

print(user1)
print(user2)


def give_award(medal, *persons):
    """Gives medals to persons"""
    for person in persons:
        print('Tovarishc ' + str(person.title) + ' nagrajdaetsya medaliyu' + str(medal))


give_award("za berlin", "vasya", "andrew", "ephim")
give_award("za otvagu", "arsen", "lubomir")