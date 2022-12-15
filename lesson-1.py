"""
    Keywords
        Predefined words used any programming languages are called keywords
        For example: if, for, else  

    Variables
        Custom words created by the programmer
        Example: 
            name = "Jewel" 
            age = 27
            experience_in_years = 7.2

    Data types
        int -> 
            An int variable saves a whole number 1, 2, -3 - Not 1.5
        str -> string 
            String is a series of characters
        float -> Floating point values
            Numbers with decimal point. Eg: 1.5, -2.4984
        list -> List of anything
            List can contain any data types. Eg: [1, 2, 4] or ["honey", "joseph"] or [1, "honey", 2.5]
        dict -> Dictionary
            Dictionary contains key value pairs. 
            Eg:
            {
                "name": "Honey", 
                "age": 28 , 
                "skills": ["Communication"]
                "experiences": [
                    {
                        "company": "BK College",
                        "start_date": "2019-07-01",
                        "end_date": "2020-07-01",
                        "designation": "Asst. Professor",
                        "location": "Kottayam, Kerala"
                    },
                    {
                        "company": "Adooh",
                        "start_date": "2022-07-01",
                        "end_date": "Present",
                        "designation": "Asst. Professor",
                        "location": "Kottayam, Kerala"
                    }
                ] 
            }       
"""

name = "Jewel" 
age = 27
experience_in_years = 7.2
numbers = [1, 5, 4]
skills = ["honey", "joseph"]
user = {
    "name": "Honey", 
    "age": 28 , 
    "skills": ["Communication", "Leadership"],
    "experience_in_years": 3.1,
    "experiences": [
        {
            "company": "BK College",
            "start_date": "2019-07-01",
            "end_date": "2020-07-01",
            "designation": "Asst. Professor",
            "location": "Kottayam, Kerala"
        },
        {
            "company": "Adooh",
            "start_date": "2022-07-01",
            "end_date": "Present",
            "designation": "Asst. Professor",
            "location": "Kottayam, Kerala"
        }
    ] 
}

# print(name) # prints "Jewel"
# print(user["name"]) # prints "Honey"
# print(numbers[0]) # prints 1

# numbers = "Honey"

# try:
#     print(numbers[0])
# except IndexError as e:
#     print("Uh oh IndexError: ", e)
# except Exception as e:
#     print("Uh oh General Error: ", e)

# print("Hi")




# names = ["Money", "Honey", "Johney", "Roney", "Horny"]
# name = names[0]
# print(name, "-->", name[0]=="H")

# name = names[1]
# print(name, "-->", name[0]=="H")

# name = names[2]
# print(name, "-->", name[0]=="H")

# print(len(names)) # prints 5
# length_of_name = len(names)
# print(length_of_name)

# # Print the names start with H
# names = ["Money", "Honey", "Johney", "Roney", "Horny"]
# for name in names: # this is a for loop
#     first_letter = name[0] # taking the 0th index 
#     if first_letter=="H":
#         print(name)

def filter_names(names, required_character, index):
    """
        takes 3 arguments/params/parameters
        names: list of names
        required_character: filtering character
        index: position of the character in the name
    """
    for name in names: # this is a for loop
        try:
            nth_letter = name[index] 
            if nth_letter==required_character:
                print(name)
        except IndexError:
            pass

        

# names = ["Money", "Honey", "Johney", "Roney", "Horny"]
# print("Here are the names available: ", names)
names = []
counter = 1
print("=========Name filtering application===========")
print("Hi User, Please enter the names to filter from. Enter 0 to complete names input.")
name = "dummy"
while name!="0":
    name = input("Enter name " + str(counter) + ": ")
    if name!="0":
        names.append(name)
        print("names: ", names)
        counter+=1 # same as counter = counter + 1

character = input("Enter the character to search: ")
index = int(input("Enter the position to search: "))
index = index - 1
filter_names(names, character, index)


