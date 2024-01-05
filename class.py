class Employee:
    company='TESLA'
    CEO    ='ELON MUSK'
    def insert_member(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid 
ravi = Employee()
gayi = Employee()
virat = Employee()
Employee.insert_member(ravi,'ravi',22,50000,'test01')
Employee.insert_member(gayi,'gayi',21,45000,'test02')
virat.insert_member('virat',45,20000,'test03')
