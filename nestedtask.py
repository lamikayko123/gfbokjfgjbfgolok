names= [
    ['Alice','Bob','Charlie'], 
    ['David','Eve','Frank'],
    ['Grace','Heidi','Ivan'],
    ['judy','Ken','Laura']
]
# Check if "Alice" exist and remove her

Alice_found = False

for list in names:
    if "Alice" in list:
        list.remove("Alice")
    Alice_found = True


if Alice_found:
    new_name = input("Alice not found. Enter a new to add: ")
    names[0].append(new_name)

    print(names)

    for list in names:
        for name in list:
            print(name)
    





        
