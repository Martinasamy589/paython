# from matplotlib import pyplot
# import pandas as pd
# import seaborn as sns
#
# from pandas.plotting import scatter_matrix
# # from pandas import read_csv
#
# data= pd.read_csv('Pproject_programming_section.csv')
# print(data)
# print(data.dtypes)
# print(data.describe())
# print(data.isna().sum())
# data=data.dropna()
# print(data.isna().sum())
# print(data.duplicated())
# data.drop_duplicates(inplace= True)
# print(data)
#
# # #data frame 1
# #
# data = { "name": ['martina', 'martha', 'moris','marina'],"gpa": [2.1, 2.6, 1.9,2.1],"subject":['programing','math','ob','om'] }
# mar= pd.DataFrame(data)
# print(mar)
#
# # #data frame 2
# data = [['martina',3.1],['marina',2.0],['martha',1.9],['moris',2.1]]
# mar= pd.DataFrame(data,columns=['name','gpa'])
# print(mar)
# data.plot(kind='density', subplots=True, layout=(3,2))
# data.plot("tax")
# data.hist()
# print(data.corr())
# data=sns.heatmap(data.corr())
# scatter_matrix(data)
# d = data.head(20)
# sns.pairplot( d,hue="tax")
# sns.countplot(x='tax', data=data, palette='hls')
# pyplot.show()
#
#
#
#
#













class Person :
    def __init__(self,name ,NID,phone,program,year,semester,faculty):
        self.name = name
        self.__NID =NID
        self.phone = phone
        self.program=program
        self._year = year
        self._semester = semester
        self._faculty = faculty

    def details(self):
        print('name :',self.name,'NID:',self.__NID, self.phone ,self.program,
            'faculty is :', self._faculty ,'the semester :',self._semester ,'year:',self._year)

    def get_nid(self):
        return self.__NID

    def set_NID(self, NID):
        self.__NID = NID
class Doctor(Person):
    def __init__(self ,name ,NID,phone,program,year,semester,faculty,code,course,salary,hours=0):
        self.code=code
        self.course=course
        self.salary=salary
        self.hours=hours
        Person.__init__(self,name ,NID,phone,program,year,semester,faculty)
    def details(self):
        print('name :',self.name,'NID:', self.phone ,self.program,
            'faculty is :', self._faculty ,'the semester :',self._semester ,'year:',self._year,self.code,self.course,self.salary,self.hours)

    def check(self):
        return self.course

    def change(self, course):
        self.course = course

    def check_hours(self):
        return self.hours

    def check_salary(self):
        return self.salary


    def add_hours_worked(self, hours):
       self.hours = hours + self.hours
       overtime = self.hours - 30
       overtime_amount = (overtime * (self.salary / 30))
       if self.hours > 30:
         self.salary = self.salary + overtime_amount

    def Exit(self):
        return exit('Log out ')




class Student(Person):
    def __init__(self,name ,NID,phone,program,year,semester,faculty,ID,email):
        self.ID =ID
        self.email=email
        Person.__init__(self,name ,NID,phone,program,year,semester,faculty)

    def detail(self):
        print( 'name :',self.name,'NID:',self.__NID, self.phone ,self.program,
            'faculty is :', self._faculty ,'the semester :',self._semester ,'year:',self._year,self.ID, self.email)

    def check_ID(self):
        return self.__NID

    def change_ID(self, NID):
        self.__NID = NID

    def Exit(self):
        return exit('Log out ')



while True:
    martina = input('Login as Doctor or student ?  ')



    if  martina == 'Doctor':
        name = input(' enter name: ')
        NID = int(input('Enter NID: '))
        phone = int(input('Enter phone: '))
        faculty = 'Business'
        program = input('Enter program: ')
        semester = 'second semester'
        year = 2023
        code = input('Enter Code: ')
        course = input('Enter Course: ')
        salary = float(input('Enter salary: '))

        doc=Doctor(name ,NID,phone,program,year,semester,faculty,code,course,salary,hours=0)



        while True:
            print('''
                    1 Account details
                    2 Check course
                    3 Change course
                    4 Check hours worked
                    5 Check salary
                    6 Add hours worked
                    7 Exit''')
            martina1= int(input('Enter the number of the option you want: '))

            if martina1==1:
                print(doc.details())
                l=input('do you want continue y or n ? ')
                if l == 'yes':
                    continue
                elif l == 'no':
                    print(doc.Exit())
            elif martina1==2:
                print(doc.check())
                l = input('do you want continue y or n ? ')
                if l == 'y':
                    continue
                elif l == 'n':
                    print(doc.Exit())
            elif martina1 ==3:
                m = input('change course to: ')
                doc.change(m)
                l = input('do you want continue y or n ? ')
                if l == 'y':
                    continue
                elif l == 'n':
                    print(doc.Exit())
            elif martina1 ==4:
                print(doc.check_hours())
                l = input('do you want continue y or n ? ')
                if l == 'y':
                    continue
                elif l == 'n':
                    print(doc.Exit())
            elif martina1 ==5:
                print(doc.check_salary())
                l = input('do you want continue y or n ? ')
                if l == 'y':
                    continue
                elif l == 'n':
                    print(doc.Exit())
            elif martina1 ==6:
                h = float(input('Add hours worked: '))
                doc.add_hours_worked(h)
                l = input('do you want continue y or n ?')
                if l == 'y':
                    continue
                elif l == 'n':
                    print(doc.Exit())
            elif martina1==7:
                print(doc.Exit())
                break
        break



    elif martina == 'Student':
        name = input('Name: ')
        NID = int(input('Enter NID: '))
        phone = int(input('Enter phone: '))
        faculty = 'Business'
        program = input('Enter program: ')
        semester = 'second semester'
        year = 2023
        student_ID = input('Enter  Student ID: ')
        uni_email = input('Enter University email: ')
        st=Student(name, NID, phone, faculty, program, semester,year, student_ID, uni_email)


        while True:
            print('''
            1 Account details
            2 Check National ID (NID)
            3 Change National ID (NID)
            4 Exit''')
            samy= int(input('Enter the number of the option you want: '))

            if samy ==1:
                print(st.details())
                c = input('do you want continue y or n ? ')
                if c == 'y':
                    continue
                elif c == 'n':
                    print(st.Exit())
            elif samy ==2:
                print(st.check_ID())
                c = input('do you want continue y or n ? ')
                if c == 'y':
                    continue
                elif c == 'n':
                    print(st.Exit())
            elif samy==3:
                b = int(input('Change national ID: '))
                st.change_ID(b)
                c = input('do you want continue y or n ? ')
                if c == 'y':
                    continue
                elif c == 'n':
                    print(st.Exit())
            elif samy ==4:
                print(st.Exit())
                break
        break

    else:
        print('Try again')



from math import pi
class Shape:
  def __init__(self, name):
    self.name = name
  def area(self):
    pass
  def fact(self):
    return "I am a two-dimensional shape."
  def __str__(self):
    return self.name
class Square(Shape):
  def __init__(self, length):
   super().__init__("Square")
   self.length = length
  def area(self):
   return self.length**2
  def fact(self):
   return "Squares have each angle equal to 90degrees."

class Circle(Shape):
  def __init__(self, radius):
      super().__init__("Circle")
      self.radius = radius

  def area(self):
      return pi * self.radius **2

a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

class Person:
 def person_info(self, name, age):
   print('Inside Person class')
   print('Name:', name, 'Age:', age)
# Parent class 2
class Company:
 def company_info(self, company_name, location):
   print('Inside Company class')
   print('Name:', company_name, 'location:',
location)
# Child class
class Employee(Person, Company):
 def Employee_info(self, salary, skill):
   print('Inside Employee class')
   print('Salary:', salary, 'Skill:', skill)
# Create object of Employee
emp = Employee()
# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
class Polygon:
 def __init__(self, no_of_sides):
  self.n = no_of_sides
  self.sides = [0 for i in range(no_of_sides)]
 def inputSides(self):
  self.sides = [float(input("Enter side "+str(i+1)+": ")) for i in range(self.n)]
 def dispSides(self):
  for i in range(self.n):
   print("Side",i+1,"is",self.sides[i])

class Person:
 def work(self):
  print("A person can work.")
 def food(self):
  print("A person eats food.")
class Employee(Person):
 def work(self):
  super().work()
  print("I can work.")
 def food(self):
  super().food()
  print("I can eat.")
p1 = Person()
p2 = Employee()
# p1.work()
p2.work()
p1.food()
# p2.food()
class A:
 def __init__(self,b):
  self.b=b
 def display(self):
  print(self.b)
obj=A("Hello")
del obj





















