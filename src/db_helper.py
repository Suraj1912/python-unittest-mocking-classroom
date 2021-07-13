import mysql.connector

class DbHelper:

    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', password='', database='emp')
        self.cur = self.con.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.cur.execute('SELECT MAX(salary) FROM dummy')
        return self.cur.fetchone()[0]  ## 99997 is max salary

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.cur.execute('SELECT MIN(salary) FROM dummy')
        return self.cur.fetchone()[0]  ## 10001 is min salary

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)