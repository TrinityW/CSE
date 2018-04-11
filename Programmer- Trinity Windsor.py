class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def position(self):
        print("%s works at %d" % self.name, self.job)


class Programmer(Employee):
    def __init__(self, name, age, job, computer_type):
        super(Programmer, self).__init__(name, age, job,)
        self.computer_type = computer_type

    def start(self):
        print("%s starts to program on their computer" % self.name)


steve = Employee("Steve", 35, 'work')
