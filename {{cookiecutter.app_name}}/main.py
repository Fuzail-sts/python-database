import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.myDb = connector.connect(host='localhost', port='3306',
                                      user='root', password='root', database='company')

        query = 'create table if not exists employee(employeeId int primary key,employeeName varchar(200),employeeDepartment varchar(50))'
        myCursor = self.myDb.cursor()
        myCursor.execute(query)
        print('created')

        query = 'create table if not exists department(departmentId int primary key,employeeName varchar(200),salary varchar(50))'
        myCursor = self.myDb.cursor()
        myCursor.execute(query)
        print('created department')

    def insert_employee(self, employeeId, employeeName, employeeDepartment):
        query = "insert into employee(employeeId, employeeName, employeeDepartment)   values({}, '{}', '{}')" .format(
            employeeId, employeeName, employeeDepartment)
        print(query)
        myCursor = self.myDb.cursor()
        myCursor.execute(query)
        self.myDb.commit()
        print('employee saved to db')

    def insert_department(self, departmentId, employeeName, salary):
        query = "insert into department(departmentId, employeeName, salary)   values({}, '{}', '{}')" .format(
            departmentId, employeeName, salary)
        print(query)
        myCursor = self.myDb.cursor()
        myCursor.execute(query)
        self.myDb.commit()
        print('department saved to db')

    def fetch_all(self):
        query = 'select * from employee'
        myCursor = self.myDb.cursor()
        myCursor.execute(query)
        for row in myCursor:
            print('employee id:', row[0])
            print('employee Name:', row[1])
            print('employee Department:', row[2])

    def delete_employee(self, employeeId):
        query = 'delete from employee where employeeId={}'.format(employeeId)
        print(query)
        myCursor = self.myDb.cursor()
        myCursor.execute(query)
        self.myDb.commit()
        print('deleted employeeId')


helper = DBHelper()
helper.insert_employee(1, 'Dia', 'Testing')
helper.insert_employee(2, 'Mirza', 'Security')
helper.insert_employee(3, 'Ram', 'Developer')
helper.insert_employee(4, 'Tina', 'Architecture')


helper.insert_department(1, 'Dia', '25000')
helper.insert_department(2, 'Mirza', '30000')
helper.insert_department(3, 'Ram', '35000')
helper.insert_department(4, 'Tina', '40000')
helper.fetch_all()
helper.delete_employee(1)
helper.fetch_all()

