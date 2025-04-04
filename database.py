# Import necessary modules and functions
import random
import string
import mysql.connector
from datetime import datetime, timedelta
from fastapi import HTTPException

#--------------------------------------------------------------------------------------------
# Define a function to connect to the MySQL database
#--------------------------------------------------------------------------------------------
def connect_to_mysql():

    # Database configuration details
    config = {
        'host': 'localhost',
        'database': 'maseerdb',
        'user' : 'root',
	    'password' : '' 
    }
    try:
        # Attempt to establish a connection to the MySQL database
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
        else: 
            return None
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None






#--------------------------------------------------------------------------------------------
# Define a function to create a new user account
#--------------------------------------------------------------------------------------------
def create_user(user_data):
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    password = user_data.password + salt
    
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Check if the email already exists
    email_check_query = "SELECT COUNT(*) FROM User_Account WHERE Email = %s"
    cursor.execute(email_check_query, (user_data.email,))
    email_exists = cursor.fetchone()[0]

    if email_exists:
        cursor.close()
        conn.close()
        # If email exists, raise an exception
        raise HTTPException(status_code=400, detail="Email already exists. Please use a different email.")

    # Proceed with inserting the new user if email doesn't exist
    insert_query = "INSERT INTO User_Account (First_Name, Last_Name, Email, Phone_Number, Password, Salt) VALUES (%s, %s, %s, %s, (aes_encrypt(%s,'Maseer')), %s)"
    cursor.execute(insert_query, (user_data.first_name, user_data.last_name, user_data.email, user_data.phone_number, password, salt))
    conn.commit()

    cursor.close()
    conn.close()
    


#--------------------------------------------------------------------------------------------
# Define a function to retrieve a user by email
#--------------------------------------------------------------------------------------------
def get_user_by_email(email):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "SELECT Email, REPLACE (cast(aes_decrypt(`Password`, 'Maseer') as char(100)),`salt`,'') AS Password, User_ID FROM User_Account WHERE Email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user



#--------------------------------------------------------------------------------------------
# Define a function to retrieve a user by ID
#--------------------------------------------------------------------------------------------
def check_email(email: str) -> bool:
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Check if the email already exists
    email_check_query = "SELECT COUNT(*) FROM User_Account WHERE Email = %s"
    cursor.execute(email_check_query, (email,))
    email_exists = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return email_exists == 0



#--------------------------------------------------------------------------------------------
# Define a function to retrieve user data by ID
#--------------------------------------------------------------------------------------------
def get_user_by_id(user_id):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "SELECT User_ID, REPLACE (cast(aes_decrypt(`Password`, 'Maseer') as char(100)),`salt`,'') AS Password, User_ID FROM User_Account WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


#--------------------------------------------------------------------------------------------
# Define a function to update a user's phone number
#--------------------------------------------------------------------------------------------
def get_userData(user_id):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "SELECT CONCAT(First_Name, ' ' , Last_Name) AS Name, Email, Phone_Number FROM User_Account WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    conn.close()
    return user_data



#--------------------------------------------------------------------------------------------
# Define a function to update a user's password
#--------------------------------------------------------------------------------------------
def update_phone_number(user_id: int, new_phone_number: str) -> bool:
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "UPDATE User_Account SET Phone_Number = %s WHERE User_ID = %s"
    cursor.execute(query, (new_phone_number, user_id))
    conn.commit()  # Commit the changes
    rows_affected = cursor.rowcount  # Check the number of rows affected
    cursor.close()
    conn.close()

    # If rows_affected is greater than 0, it means the record has been updated
    return rows_affected > 0


#--------------------------------------------------------------------------------------------
# Define a function to update a user's password
#--------------------------------------------------------------------------------------------
def Update_Password(user_id: int, Newpassword: str) -> bool:
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    password = Newpassword + salt
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "UPDATE User_Account SET Password = (aes_encrypt(%s,'Maseer')), salt = %s WHERE User_ID = %s"
    cursor.execute(query, (password, salt, user_id))
    conn.commit()  # Commit the changes
    rows_affected = cursor.rowcount  # Check the number of rows affected
    cursor.close()
    conn.close()

    # If rows_affected is greater than 0, it means the record has been updated
    return rows_affected > 0



#--------------------------------------------------------------------------------------------
# Define a function to recover a user's password
#--------------------------------------------------------------------------------------------
def Recover_Password(email: str, Newpassword: str) -> bool:
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    password = Newpassword + salt
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "UPDATE User_Account SET Password = (aes_encrypt(%s,'Maseer')), salt = %s WHERE Email = %s"
    cursor.execute(query, (password, salt, email))
    conn.commit()  # Commit the changes
    rows_affected = cursor.rowcount  # Check the number of rows affected
    cursor.close()
    conn.close()

    # If rows_affected is greater than 0, it means the record has been updated
    return rows_affected > 0



#--------------------------------------------------------------------------------------------
# Define a function to delete a user account
#--------------------------------------------------------------------------------------------
def delete_user_account(user_id: int) -> bool:
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "DELETE FROM User_Account WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    conn.commit()  # Commit the changes
    rows_affected = cursor.rowcount  # Check the number of rows affected
    cursor.close()
    conn.close()

    # If rows_affected is greater than 0, it means the record has been deleted
    return rows_affected > 0



#--------------------------------------------------------------------------------------------



