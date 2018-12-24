def assignment():
    teacher             =   input('Enter teacher name: ')
    number_of_students  =   int(input('Enter the class population: '))
    data_entry(teacher,number_of_students)


def data_entry(teacher,number_of_students):
    counter     =   0
    students    =   []
    while(counter < number_of_students):

        student_name    =   input(f'Enter Student Name {counter+1}/{number_of_students}: ')

        #append name to student's list
        students.insert(student_name)

        #increment counter
        counter +=  1

    print(students)

    
assignment()