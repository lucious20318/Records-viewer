# Assignment - 2
# Name - Ojasva Singh
# Roll No - 2020318

import json
from typing import Dict

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
    '''
    **** DO NOT modify this function ****
    Description: Reads the data.json file, and converts it into a dictionary.

    Parameters:
    - file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

    Returns:
    - A dictionary containing the data read from the file
    '''

    with open(file_path, 'r') as data:
        records = json.load(data)

    return records


def filter_by_first_name(records, first_name):
    '''
    Description: Searches the records to find all persons with the given first name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - first_name (STRING): The first name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given first name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    fname_lst = []

    for item in records:
        if item["first_name"].lower() == first_name.lower():
            fname_lst.append(item["id"])
        else:
            pass

    return fname_lst


# IF NO RECORD IS FOUND THEN id_lst IS EMPTY AND IS RETURNED OTHERWISE THE LIST WILL CONTAIN THE ID'S AND IS RETURNED


def filter_by_last_name(records, last_name):
    '''
    Description: Searches the records to find all persons with the given last name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - last_name (STRING): The last name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given last name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    lname_lst = []

    for item in records:
        if item["last_name"].lower() == last_name.lower():
            lname_lst.append(item["id"])
        else:
            pass

    return lname_lst


def filter_by_full_name(records, full_name):
    '''
    Description: Searches the records to find all persons with the given full name (case-insensitive)
.
    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    full_name_lst = []

    for item in records:
        if (item["first_name"].lower() + " " + item["last_name"]).lower() == full_name.lower():
            full_name_lst.append(item["id"])
        else:
            pass

    return full_name_lst


def filter_by_age_range(records, min_age, max_age):
    '''
    Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - min_age (INTEGER): The minimum age (inclusive)
    - max_age (INTEGER): The maximum age (inclusive)

    Note: 0 < min_age <= max_age

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    age_name = []

    for item in records:
        if item["age"] in range(min_age, max_age + 1):
            age_name.append(item["id"])
        else:
            pass
    return age_name


def count_by_gender(records):
    '''
    Description: Counts the number of males and females

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A dictionary with the following two key-value pairs:
        KEY        VALUE
        "male"     No of males (INTEGER)
        "female"   No of females (INTEGER)
    '''

    males = 0
    females = 0

    for item in records:
        if item["gender"] == "male":
            males += 1
        else:
            females += 1

    dict = {'male': males, 'female': females}

    return dict


def filter_by_address(records, address):
    '''
    Description: Filters the person records whose address matches the given address.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
        Some examples are:
            Case 1: {}
                => All records match this case

            Case 2: { "block": "AD", "city": "Delhi" }
                => All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)

            Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

    Returns:
    - A LIST of DICTIONARIES with the following two key-value pairs:
        KEY            VALUE
        "first_name"   first name (STRING)
        "last_name"    last name (STRING)
    '''

    lst = []
    lst0 = []

    for item in records:
        for ele in address:
            if ele == "house_no" or ele == "pincode":
                if item["address"][ele] == address[ele]:
                    dict = {"first_name": item["first_name"], "last_name": item["last_name"]}
                    lst.append(dict)
                else:
                    pass
            else:
                if item["address"][ele].lower() == address[ele].lower():
                    dict = {"first_name": item["first_name"], "last_name": item["last_name"]}
                    lst.append(dict)
                else:
                    pass

    if not address:
        for item in records:
            dic = {"first name": item["first_name"], "last name": item["last_name"]}
            lst0.append(dic)

    x = len(address)
    list = []
    f_lst = []
    for item in lst:
        if item not in list:
            list.append(item)

    for item in list:
        if lst.count(item) == x:
            f_lst.append(item)

    if not address:
        return lst0
    else:
        return f_lst


def find_alumni(records, institute_name):
    '''
    Description: Find all the alumni of the given institute name (case-insensitive).

    Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - institute_name (STRING): Name of the institute (case-insensitive)

    Returns:
    - A LIST of DICTIONARIES with the following three key-value pairs:
        KEY            VALUE
        "first_name"   first name (STRING)
        "last_name"    last name (STRING)
        "percentage"   percentage (FLOAT)
    '''
    lst = []
    for item in records:
        for ele in item["education"]:
            if ele["institute"] == institute_name:
                if not ele["ongoing"]:
                    dic = {"first_name": item["first_name"], "last_name": item["last_name"],
                           "percentage": ele["percentage"]}
                    lst.append(dic)
            else:
                pass

    return lst


def find_topper_of_each_institute(records, false=None):
    '''
    Description: Find topper of each institute

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

    Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
    '''

    dic = {}

    def topper(dic):
        for item in records:
            for ele in item["education"]:
                institute = ele["institute"]
                if institute not in dic.keys():
                    dic[institute] = [0, 0]
                if ele["ongoing"] == False:
                    per = ele["percentage"]
                    if per > dic[institute][1]:
                        dic[institute] = [item["id"], ele["percentage"]]

        return dic

    dicc = topper(dic)
    for x in dicc:
        del (dicc[x][1])
    for y in dicc:
        for b in dicc[y]:
            dicc[y] = b

    return dicc


def find_blood_donors(records, receiver_person_id):
    '''
    Description: Find all donors who can donate blood to the person with the given receiver ID.

        Note:
        - Possible blood groups are "A", "B", "AB" and "O".

        Rules:
        BLOOD GROUP      CAN DONATE TO
        A                A, AB
        B                B, AB
        AB               AB
        O                A, B, AB, O

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - receiver_person_id (INTEGER): The ID of the donee
        Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

    Returns:
    - A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''

    x = ''
    for item in records:
        if item["id"] == receiver_person_id:
            x = item["blood_group"]
            break

    dic = {}
    if x == 'A':
        for item in records:
            if item["blood_group"] == 'A' or item["blood_group"] == 'O':
                dic[item["id"]] = item["contacts"]
            else:
                pass

    elif x == 'B':
        for item in records:
            if item["blood_group"] == 'B' or item["blood_group"] == 'O':
                dic[item["id"]] = item["contacts"]

    elif x == 'AB':
        for item in records:
            if item["blood_group"] == 'AB':
                dic[item["id"]] = item["contacts"]

    else:
        for item in records:
            if item["blood_group"] == 'O':
                dic[item["id"]] = item["contacts"]

    dic.pop(receiver_person_id, None)
    return dic


def get_common_friends(records, list_of_ids):
    '''
    Description: Find the common friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''

    def check(x, y, list, rec):
        count = 0
        for ele in rec:
            for item in list:
                if item == ele["id"]:
                    if y in ele["friend_ids"]:
                        count += 1
                    else:
                        pass
                else:
                    pass

        if count == x:
            return True
        else:
            return False

    lst = []
    x = len(list_of_ids)
    for ele in records:
        for item in list_of_ids:
            if item == ele["id"]:
                for i in ele["friend_ids"]:
                    y = i
                    z = check(x, y, list_of_ids, records)
                    if z:
                        lst.append(y)
                    else:
                        pass

    f_lst = []

    for item in lst:
        if item not in f_lst:
            f_lst.append(item)

    return f_lst


def is_related(records, person_id_1, person_id_2):
    '''
    **** BONUS QUESTION ****
    Description: Check if 2 persons are friends

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id_1 (INTEGER): first person ID
    - person_id_2 (INTEGER): second person ID

    Returns:
    - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''
    pass



def delete_by_id(records, person_id):
    '''
    Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    flag = 0
    old_records = records
    z = []

    for item in records:
        if item["id"] == person_id:
            records = records.remove(item)
            flag = 1
        else:
            z.append(item)

    for x in z:
        for ele in x["friend_ids"]:
            if ele == person_id:
                x["friend_ids"].remove(ele)
                break
            else:
                pass

    if flag == 0:
        return old_records
    else:
        return z


def add_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    flag = 0
    x = []
    y = []
    old_records = records
    for item in records:
        if item["id"] == person_id:
            item["friend_ids"].append(friend_id)
            flag = flag + 1
            for ele in item["friend_ids"]:
                if ele not in x:
                    x.append(ele)
            item["friend_ids"] = x
        elif item["id"] == friend_id:
            item["friend_ids"].append(person_id)
            flag = flag + 1
            for ele in item["friend_ids"]:
                if ele not in y:
                    y.append(ele)
            item["friend_ids"] = y
        else:
            pass

    if flag == 2:
        return records
    else:
        return old_records


def remove_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    y = []
    old_records = records

    for item in records:
        if item["id"] == person_id:
            if friend_id in item["friend_ids"]:
                item["friend_ids"].remove(friend_id)
            else:
                return old_records

        elif item["id"] == friend_id:
            if person_id in item["friend_ids"]:
                item["friend_ids"].remove(person_id)
            else:
                return old_records
        else:
            pass

    return records


def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
    Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - institute_name (STRING): The institute name (case-insensitive)
    - ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
    - percentage (FLOAT): The person's score in percentage

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    flag = 0
    old_records = records
    for item in records:
        if item["id"] == person_id:
            if ongoing:
                dic = {"institute": institute_name, "ongoing": ongoing}
                item["education"].append(dic)
                flag = 1
                break
            else:
                dic = {"institute": institute_name, "ongoing": ongoing, "percentage": percentage}
                item["education"].append(dic)
                flag = 1
                break
        else:
            pass

    if flag == 0:
        return old_records
    else:
        return records
