#ex 16.8 Use the sqlalchemy module to connect to the sqlite3 
#  database books.db that you just made in exercise 16.4.
#  As in 16.6, select and print the title column from the
#  book table in alphabetical order
#creat short hand for ease of coding
#
import sqlalchemy as sa
conn = sa.create_engine('sqlite:///books.db')

select * from booktable order by al