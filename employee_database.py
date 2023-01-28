#! python3

import inflect
 
ie = inflect.engine()
 
name = ["Bob", "Sally", "Susan", "Gertrude"]
position = ["marketing", "manager", "HR", "accounting"]
tenure = ("3 years", "10 years", "11 years", "1 years")
salary = [ ]
 
def earnings(y):
    x = float(32300 * 0.05)
    increase = float(x * y)
    final = int(32300 + increase)
    return str("$") + str(final)
 
for num in tenure:
    year = int(num[0:2])
    salary.append(earnings(year))
 
data = list(zip( name, position, tenure, salary))
 
 
index_one = ' : ' . join(data[0])
index_two = ' : ' . join(data[1])
index_three = ' : ' . join(data[2])
index_four = ' : ' . join(data[3])

#n = '\u0332'
 
print("----------EMPLOYEE DATABASE---------")
 
for employee in name:
    print(employee)
    
def index_retrieval():
    status = True
    while status == True:
        query = input('''   
        Please select an index
       
        if you need help type ' search ' 
        
        to exit type 'quit' 
       
               ''')
        if (query) == "search":
            lookup = input('''
            Enter a NAME. 
            ''')
            x = name.index(lookup.capitalize())
            print(f"\n-----index {ie.number_to_words(x + 1)}-----")
        elif (query) == ("index one"):
            print(index_one.center(20))
        elif (query) == ("index two"):
            print(index_two)
        elif (query) == ("index three"):
            print(index_three)
        elif (query) == ("index four"):
            print(index_four)
        elif (query) == ("quit"):
            status = False
            print("CLOSING")
            return(query)
 
index_retrieval()
        
    