# Name - Ojasva Singh
# Roll No - 2020318

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''

from main import *

print('=' * 50)
print('\t', '\t', '  MAIN MENU')
print('=' * 50)

print('Hello! Welcome to the records library')
print('Following are the options:')
print('-' * 50)

print("1.  Read the data from the file")
print("2.  Records with a common first name")
print("3.  Records with a common last name")
print("4.  Records with a common full name")
print("5.  Records in a specific age range")
print("6.  Check the number of males and females")
print("7.  Records with a specific address")
print("8.  Alumni of a institute")
print("9.  Topper of each institute")
print("10. Find blood donors")
print("11. Find common friends from a group")
print("12. is_related")
print("13. Delete an ID from the records")
print("14. Make 2 people friends")
print("15. Remove 2 people fromm their friends list")
print("16. Add an education record for a specific ID")
print('-' * 50)


def input_(rec):
    choice = int(input('Enter your choice :'))

    if choice == 1:
        print(f'Records :{rec}')
        input_(rec)

    elif choice == 2:
        first_name = input("Enter the first name :")
        lst = filter_by_first_name(rec, first_name)
        print(f'Records with a common first name :{lst}')
        input_(rec)


    elif choice == 3:
        last_name = input("Enter the last name :")
        lst = filter_by_last_name(rec, last_name)
        print(f'Records with a common last name :{lst}')
        input_(rec)

    elif choice == 4:
        full_name = input("Enter the full name :")
        lst = filter_by_full_name(rec, full_name)
        print(f'Records with a common first name :{lst}')
        input_(rec)


    elif choice == 5:
        min = int(input("Enter the minimum age :"))
        max = int(input("Enter the maximum age :"))
        lst = filter_by_age_range(rec, min, max)
        print(f'Records in the given range :{lst}')
        input_(rec)


    elif choice == 6:
        lst = count_by_gender(rec)
        print(f' The number of males and females are :{lst}')
        input_(rec)


    elif choice == 7:
        x = int(input("Enter the number of parameters you want to pass in address dictionary :"))
        dic = {}
        for item in range(n):
            y = input()
            if y == 'house_no' or y == 'pincode':
                z = int(input())
                dic[y] = z
            else:
                z = input()
                dic[y] = z

        lst = filter_by_address(rec, dic)
        print(f'Records with the given address :{lst}')
        input_(rec)


    elif choice == 8:
        inst = input("Enter the name of the institute")
        lst = find_alumni(rec, inst)
        print(f'Alumni of the institute {inst} : {lst}')
        input_(rec)


    elif choice == 9:
        lst = find_topper_of_each_institute(rec)
        print(f'The topper of each institute :{lst}')
        input_(rec)


    elif choice == 10:
        id = int(input("Enter the id of the receiver :"))
        lst = find_blood_donors(rec, id)
        print(f'Blood donors :{lst}')
        input_(rec)


    elif choice == 11:
        lst1 = list(map(int, input("Enter the ID's of the people whose common friends need to be found :")).split())
        lst = get_common_friends(rec, lst1)
        print(f'The list of common friends IDs is {lst}')
        input_(rec)


    elif choice == 12:
        print(f' isRelated ')
        input_(rec)


    elif choice == 13:
        delete = int(input("Enter the id whose record you want to delete:"))
        lst = delete_by_id(rec, delete)
        rec = lst
        print(f'The updated records are {rec}')
        input_(rec)


    elif choice == 14:
        per = int(input("Enter the id of the first person :"))
        fre = int(input("Enter the id of the friend :"))
        lst = add_friend(rec, per, fre)
        rec = lst
        print(f'The updated records are {rec}')
        input_(rec)


    elif choice == 15:
        per = int(input("Enter the id of the first person :"))
        fre = int(input("Enter the id of the friend :"))
        lst = remove_friend(rec, per, fre)
        rec = lst
        print(f'The updated records are {rec}')
        input_(rec)


    elif choice == 16:
        per = int(input("Enter the person id :"))
        ins = input("Enter the institute name :")
        ong = bool(input("Is the person currently studying or not"))
        if not ong:
            perc = float(input("Enter the percentage :"))
            lst = add_education(per, ins, ong, perc)
        else:
            lst = add_education(per, ins, ong, None)

        rec = lst
        print(f'The updated records are {rec}')
        input_(rec)


    elif choice == -1:
        quit()

    else:
        print(f"Invalid query code. Enter a valid code :")

        input_(rec)


rec = read_data_from_file()
input_(rec)
