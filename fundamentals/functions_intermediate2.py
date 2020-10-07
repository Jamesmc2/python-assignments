# x = [ [5,2,3], [10,8,9] ] 
# x[1][0]=15
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name']= 'Bryant'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0]='Andres'
# z = [ {'x': 10, 'y': 20} ]
# z[0]['y']=30
# print(z)

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(dict):
#     for x in range(len(dict)):
#         for k,v in dict[x].items():
#             print(k+' - '+v)
# iterateDictionary(students)            

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#def iterateDictionary2(key_name, some_list):
#     for x in range(len(some_list)):
#         print(some_list[x][key_name])
# iterateDictionary2('first_name',students)   

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict.keys():
        print(len(some_dict[key]),(key).upper())
        for x in range(len(some_dict[key])):
            print(some_dict[key][x])
printInfo(dojo)            