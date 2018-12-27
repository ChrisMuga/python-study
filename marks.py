#students
students    =       []

#subjects
maths       =       []
english     =       []
science     =       []

#total + average
total       =       []
average     =       []

def assignment():
    teacher              =   input('Enter teacher name: ')
    number_of_students   =   int(input('Enter the class population: '))
    data_entry(teacher,number_of_students)


def data_entry(teacher,number_of_students):
   
        counter     =       0
        while(counter < number_of_students):

                student_name    =   input(f'Enter Student Name {counter+1}/{number_of_students}: ')
                #append name to student's list
                students.append(student_name)

                #load subjects
                e               =   float(input(f'Enter English Marks for {students[counter]} '))
                m               =   float(input(f'Enter Maths Marks for {students[counter]} '))
                s               =   float(input(f'Enter English Marks for {students[counter]} '))

                #append subjects to list
                english.append(e)
                maths.append(m)
                science.append(s)

                #increment counter
                counter +=  1


        compute(number_of_students)


def compute(number_of_students):
        counter         =       0
        while(counter < number_of_students):
                t                       =       english[counter] + maths[counter] +  science[counter]
                #append
                total.append(t)
                a                       =       total[counter]/3  
                #append avg  
                average.append(round(a,4))
                #a/i
                counter                 +=      1
        display(number_of_students)


def display(number_of_students):
        print(f'# \t Name \t Mat \t Eng \t Sci \t Total \t Avg')
        counter =       0
        while(counter < number_of_students):
                print(f'{counter+1} \t {students[counter]} \t {maths[counter]} \t {english[counter]} \t {science[counter]} \t {total[counter]} \t {average[counter]}')
                counter+=1









    
assignment()
