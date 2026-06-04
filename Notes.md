## This IS SUPPOSED TO BE DONE LATER

mysql(servermworkbench,router,examples and samples)
vs code
git
git desktop
mongodb (server, compass, command line tools, shell)
** Mongodb atlas (cloud database)


Theory ( RDBMS, sql,sub languages data types , libraries)
ORDBMS
Basic queries
*** Tricky queries(Important for placement/interviews)
*** Intricacies / hidden/important topics(groupby,joins)
pqsql(stored procedures, functions, indexes, views , cursors, triggers)
Implement a project
MongoDB as No SQL (not only sql)


1. Create a folder named “software”
2. create one folder each for every software/app you download
3. later from here , double click the installer file/.msi file/setup and install
NOTE:
	Some apps where installed like (Vs code , git etc … ) after they are automatically installd , the 	path of the apps of the software are automatically added to the environment variables . Some are 	not.

Steps to create personal access token:
1. Click on profile icon (top right corner)
2. then click on settings
3. then in a new window go to bottom and click on the developer settings
4. then click on the personal access token
5. Then on the tokens(classic)
6. Now click on the generate new token
7. Now click on the generate new token (classic)
8. Then in the Note section add the Note you want to add eg :” This PAT I created for learning “ .
9. Expiry: 30 days / no expiry
10. Then select the first score REPO
11. Then click on the generate token at the end of the page
12. Then copy the PAT
13. Then save it at a location only accessible to you like mailing to yourself
14. That’s it the PAT has been created

Git configuration:

$> git config –global user.name “git-username”
$> git config –global user.email “youremail”

$> git clone https://github.com/Kamalesh-choudhary/mtd_db_jun26.git
$> git push file1.sql
There is a situation where I need to authenticate inorder to push the changes to the repository and for it it will ask me the user-name and password to check if I am the owner and I have the ability to push into the repository. But eg if we want to push 10 times then entering username and password everytime could be very frustating hence we use the PAT token that we have created here. It will help us here in the saving of time of entering the username and password for many times

→ The command for this is 
$> git clone https://PAT_TOKEN@github.com/Kamalesh-choudhary/mtd_db_jun26.git


SQL COMMANDS:

show databases;
//this command lists all of the databases names

select database();
//this command lists the current working DB
//This command lists the DB which we are right now inside of 
NOTE: Observer that database() is a function

create database pavan_db;
// This is to create a new database pavan_db if it doesn’t exist else throws a error

create database IF NOT EXISTS pavan_db
// ignores the error if it exists and doesn’t create a new one 

use pavan_db;
// To select the pavan_db 

Lets take an entity: Flight
Attributes: Id, airline, flight_code, source, destination, fare, duaration, capacity

SUN-Microsystems: Java
byte,short, int, long

Oracle: MySQL
tinyint, smalling, int, bigint

**In SQL the table name must be plural.

ATTRIBUTE		DATATYPE		CONSTRAINTS	
id 			int		primary key, auto_increment(start,steps eg(101,2)
airline 		varchar(64) 	not null
flght_code 		varchar(7) 		not null, check(XX-YYYY)
source 		varchar(32) 	
destination 	varchar(32)
fare 			float			not null, default(1000)  
duaration		float			
capacity		int 


alter table flight:
change datatype from int to short
add not null constraints to source and destination
lets add check constraint to ariline code: check(XX-YYYY) XX is alphanumeric and YYYY is 1 to 4 digits number
drop the tables and crete again with the rules given above(alter tble flights) and also change the id SEED and INCREMENT to 101,2


CREATE TABLE flights(id int primary key auto_increment, airline varchar(64) not null, flight_code varchar(7) not null , source varchar(32), destination varchar(32), fare float not null default(1000),duaration float, capacity int);
lets insert few rows in the table

insert into flights(airline, flight_code, source, destination, fare, duaration, capacity) values('Air India', '6e-0934', 'hyderabad', 'amritsar', 5734, 2.5, 180);

insert into flights(airline, flight_code, source, destination, duaration, capacity) values('Air India', '6e-0934', 'hyderabad', 'amritsar', 2.5, 180);

I inserted two rows one with the no id insertion and second with the no fare insertion to check for the auto increment and the default value that we used while the creation of the table.

##[20,30]  //closed interval, both ends are included
##(20,30)  // open interval , 20,30 are excluded 
##(10,50]   // left open the range is 11 to 50.

#Operations done on the table:

1. Print the all of the data from the table:
	select * from flights;

2. print specific columns from the table:
	select airlines,flight_code from flights;

3. select the flights that fly from hyderabad;
  select * from flights where source = 'Hyderabad';

4. select the flights which have duration less than 2 hours ;
  select * from flights where duaration < 2;
  
5. selec the flights that have fare greater than 10000;
  select * from flights where fare > 1000;

6. select the flights of a specific airline (say Airline);
  select * from flights where airline = 'Air India';

7. select the flights that have least fare;
  select * from flights where fare = (select min(fare) from flights);
  select * from flights ORDER BY fare DESC LIMIT 1;

8.select the flight that have longest duration;
  select * from flights where duration = (select max(duration) from flights);

9. Print the flight details in the decreasing order of the duration;
  select * from flights ORDER BY duration ;

10. Print the flights details in the ascending order of the fare;
  select * from flights ORDER BY fare ASC;

11. Lists the flights where fare is not available;
  select * from flights where fare = null;
// compares the value in/of fare with the value in the variable null;

  select * from flights where fare = 'null';
// compares the value in fae with the string literal 'null';

  select * from flights where fare = NULL;
// Check if the fare is NULL (ie. its value is empty);

12. Now remove the fare of the flights with ID's 3 and 5;
  update flights set id = NULL where id = 3 or id = 5;

13. Print allthe flights whose source starts from 's';
    select * from flights where airline like 's%';

14. List flights in ascending order of duration and descending order of fare
    SELECT * FROM flights ORDER BY duration,fare DESC;

15. Print the fare of the flights as "Fare not available" where the fare is empty
    SELECT id,airline,flight_code,source,destination,NVL(FARE,'Fare not Available') as fare, duaration from flights;

16. display the Airline and its code whose duration is not updated or available 
    select airline,flight_code from flights where duration is NULL;

17. Display airline, code , source and destination. First letter of each of these values must be capitalized.
    select concat(upper(substring(airline,1,1)),lower(substring(airline,2,LENGTH(airline)))) as Airlines,upper(flight_code) as Flight_Code from flights;

18. Display only 1st 3 characters of the airline and also print its code.
    select left(airline,3)as Airline, flight_code from flights;   

19. Print all of the details of the flights in upper case.
    select id,upper(airline) as Airline,upper(flight_code) as Flight_Code,upper(source) as Source,upper(destination) as Destintaion,fare,upper(duaration) as Duration,upper(capacity) as Capacity from flights;

20. print airline, code and the osurce and destination together as route 
    select airline,flight_code, concat(source,'-',destination) as Route from flights;

21. Print the total fare of each of the airline.
    select airlines,sum(fares) as Total_fare from flights GROUP BY airline;

22. Count the Number of routes on which the airline provides the services.
    select airlines,count(*) as Routes from flights GROUP BY airline;

23. For a given route print the average price of the route of every airline.
    select airline,avg(fare) as Average_fare from flights GROUP BY airline;

24. For each of the airline print the minimum fare they got to offer to the customer.
    select airline,min(fare) as Minimum_fare from flights GROUP BY airline;

25. for each of the airline print the maximum duration of all the routes they fly.
    select airline,max(fare) as Maximum_fare from flights GROUP BY airline;

---------------------------------------------------------------------------------------------------------------------------------------


Project Name: Gaming Club

**Make sure to add the Cascading feature.**

Entity: Members
    member_id int primary key auto_increament,
    member_name  varchar(64) not null, 
    gender  bool(True:Male,False:Female) or char not null,
    age tinyint not null,
    phone_number  bigint check_constraint(len(phone_number) <=10) unique
    wallet_balance: float  minimum_balance should be 500;
    **Later added feature : Expiry of the wallet money

Entity: Recharges
    id: int primary key auto_increment,
    int member_id references members member_id;
    recharge_date: date default curdate;
    rehcarge_amount: check_constraint(minimum 500, maximum-10000)
    
Entity: Transactions:
    Transaction_id: int primary key auto_increment,
    int member_id references members(id),
    int game_id references games(id),
    transaction_date: default curdate,
    amount: check(min_player_count,maximum_player_count,player_multiple_count)

Entity: Games:
    id: int primary key auto_increment;
    name: vatchar(32) not null unique,
    amount_per_person: 
    min_player_count,
    maximum_player_count,
    player_multiple_count
    
Entity: Collections table
    id: int primary key auto_increment;
    amount: ,
    date:
    rating.(optional)


