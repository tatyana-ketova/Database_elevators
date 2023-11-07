import mysql.connector
#connect to server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="31101987"
)

#create a database if exists
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

database_exists = False
for db in mycursor:
    if db[0] == "Elevator_db":
        database_exists = True
        break
if not database_exists:
    mycursor.execute("CREATE DATABASE Elevator_db")
    print(f"Database Elevator_db created.")
else:
    print(f"Database Elevator_db already exists.")

#create sql queries for creating tabels
create_table_employeestatus_sql = "CREATE TABLE IF NOT EXISTS Elevator_db.EmployeeStatus(EmployeeStatusId INT AUTO_INCREMENT PRIMARY KEY, StatusDescription CHAR)"
create_table_servicestatus_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.ServiceStatus (ServiceStatusId INT  AUTO_INCREMENT PRIMARY KEY,StatusDescription CHAR)"
create_table_elevatortype_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.ElevatorType (ElevatorTypeId INT  AUTO_INCREMENT PRIMARY KEY, TypeName CHAR)"
create_table_elevatormodel_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.ElevatorModel (ElevatorModelId INT AUTO_INCREMENT PRIMARY KEY,ModelName INT,Speed INT,MaxWeight INT,PeopleLimit INT,ElevatorTypeId INT,FOREIGN KEY (ElevatorTypeId) REFERENCES ElevatorService.ElevatorType(ElevatorTypeId))"
create_table_city_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.City(CityId INT AUTO_INCREMENT PRIMARY KEY, CityName CHAR)"
create_table_building_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.Buildning ( BuildningId INT AUTO_INCREMENT PRIMARY KEY, CityId INT, FOREIGN KEY (CityId) REFERENCES ElevatorService.City(CityId), Floors INT)"
create_table_technican_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.Technican (EmployeeId INT AUTO_INCREMENT PRIMARY KEY,FirstName CHAR,LastName CHAR,EmailAddress CHAR,AnnualSalary INT,SpecialSkill CHAR,EmployeeStatusId INT,FOREIGN KEY (EmployeeStatusId) REFERENCES ElevatorService.EmployeeStatus(EmployeeStatusId))"
create_table_elevator_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.Elevator (ElevatorId INT  AUTO_INCREMENT PRIMARY KEY,ElevatorModelId INT,FOREIGN KEY (ElevatorModelId) REFERENCES ElevatorService.ElevatorModel(ElevatorModelId),BuildningId INT,FOREIGN KEY (BuildningId) REFERENCES ElevatorService.Buildning(BuildningId),InstallationDate Date)"
create_table_serviceactivity_sql ="CREATE TABLE IF NOT EXISTS Elevator_db.ServiceActivity (ServiceActivityId INT  AUTO_INCREMENT PRIMARY KEY,EmployeeId INT,FOREIGN KEY (EmployeeId) REFERENCES ElevatorService.Technican(EmployeeId),ElevatorId INT,FOREIGN KEY (ElevatorId) REFERENCES ElevatorService.Elevator(ElevatorId),ServiceDateTime DATE,ServiceDescription CHAR,ServiceStatusId INT,FOREIGN KEY (ServiceStatusId) REFERENCES ElevatorService.ServiceStatus(ServiceStatusId))"

#create list queries for executing
mysql_list = [create_table_employeestatus_sql,
              create_table_servicestatus_sql,
              create_table_elevatortype_sql,
              create_table_elevatormodel_sql,
              create_table_city_sql,
              create_table_building_sql,
              create_table_technican_sql,
              create_table_elevator_sql,
              create_table_serviceactivity_sql
              ]


#execute queries
for query in mysql_list:
    mycursor.fetchall()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    print('Execute '+query)



mycursor.close()
mydb.close()