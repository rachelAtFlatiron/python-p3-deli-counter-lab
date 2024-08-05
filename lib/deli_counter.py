import ipdb 
test = ['a', 'b', 'c', 'd', 'e']
def line(deli_line):
    if(len(deli_line) == 0):
        print ("The line is currently empty.")
    #The line is currently: 1. Logan 2. Avi 3. Spencer\n
    else: 
        ret_str = "The line is currently:"
        for i in range(0, len(deli_line)):
            print(ret_str)
            # ret_str += f' {i + 1}. {deli_line[i]}'
            person_position = i + 1
            current_person = deli_line[i]
            ret_str = ret_str + f' {person_position}. {current_person}'
        print(ret_str)

def take_a_number(deli_line, person):
    #add person to end of deli_line
    deli_line.append(person)
    #print person's name and their position
    print(f'Welcome, {person}. You are number {len(deli_line)} in line.')

def now_serving(deli_line):
    if(len(deli_line) == 0):
        print('There is nobody waiting to be served!')
    else: 
        #get/remove the first person
        #print that information
        #Currently serving Logan.
        print(f'Currently serving {deli_line.pop(0)}.')

ipdb.set_trace()