# Developer: Richard Brown
# SDEV 400 - Homework #1
# This does the uh, it'll take an input and ahhh, with that... after you've entered that... Oh you know the thing!
# version 1.0.0.0 (major, function, output, minor just for fun)

# import my_package
import datetime
import logging
import boto3
import uuid
import botocore.exceptions
from random import randint
from botocore.exceptions import ClientError
# create client
s3 = boto3.client('s3')

# bucket_list = s3.list_buckets()
# for bucket in bucket_list['Buckets']:
#     print(f' {bucket["Name"]}')


def user_menu():
    """ provide menu for user to chose from. user selection is passed
        to the user choice function after capture """
    # menu banner
    print('\n  >>>>>>>>  THANK YOU FOR CHOSING THIS PROGRAM  <<<<<<<<\n'
          '    >>>>>>>>    HERE ARE YOUR MENU OPTIONS    <<<<<<<<    ')
    # present menu options
    print('\nOption 1: GENERATE A BUCKET\nOption 2: PUT OBJECT INTO A BUCKET'
          '\nOption 3: DELETE A BUCKET\nOption 4: DELETE AN OJECT(S) FROM A BUCKET\n'
          'Option 5: COPY AN OBJECT INTO A BUCKET\nOption 6: DOWNLOAD AN OBJECT'
          '\n0: EXIT PROGRAM\n')
    # collect user selection
    try:
        
        user_input = int(input('\n Please enter your menu selection:\n\t>>>>  '))
    except ValueError as in_e:
        print('TRY SOMETHING ELSE, LIKE FOLLOWING INSTRUCTIONS,\n'
              'OR SIMPLY PICKING A NUMBER FROM THE LIST!\n', in_e)
        user_menu()
    
    # user input sent to driving while loop
    user_choice(user_input)

                        
def user_choice(u_input):
    """ function call based on user input from menu """
    while u_input != 0:
        
        if u_input == 1:
            print('\n--You have chosen to create a bucket--')
            generate_bucket_data() # creates new bucket in s3 location
        elif u_input == 2:
            print('\n--You have chosen to put a file into a bucket--')
            put_bucket_object() # puts a file into an existing bucket
        elif u_input == 3:
            print("\n--Okay, you'd like to delete an entire bucket--")
            remove_bucket() # deletes an existing bucket
        elif u_input == 4:
            print('\n--You are about to delete things inside a bucket--')
            remove_bucket_object() # deletes one or more files inside an existing bucket
        elif u_input == 5:
            print('\n--You have chosen to copy a file into a bucket--')
            copy_bucket_object() # copies file into specified bucket
        elif u_input == 6:
            print('\n--You are about to download a file from a bucket--')
            download_object() # downloads existing file from an existing bucket
        elif u_input == 7 or (u_input > 7):
            print('No sir, please make a CORRECT selection')
            user_menu()
    # exit program        
    else:
        program_termination()
    
    
def generate_bucket_data():
    """ function to generate a new bucket in the specified s3 location.
        A unique extention is added to the end of each bucket to ensure the name
        will not be rejected by the s3 """
    # create random integer for unique name creation of bucket
    ending = randint(99999, 999999)
    # collect from user the new name of the bucket
    try:
        user_bucket_creation = input('\tPlease enter the name in which you would like\n\tyour'
                                     ' newly created bucket to be called\n\t>>  ')
        # boto3 module function call to create the bucket in the s3 location
        s3.create_bucket(Bucket= str(''.join([user_bucket_creation, str(ending)])))
    except ClientError as in_e:
        print('THERE IS A PROBLEM WITH THAT BUCKET NAME,\n'
              'CHECK YOUR BUCKET LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    user_menu()
  
    
def put_bucket_object():
    """ function to put data into s3 bucket """
    # user input for variables needed to put an object into a bucket
    try:
        user_object_destination = input('\tPlease provide destination bucket location\n\t>>  ')
        user_object_name = input('\tPlease provide the file name\n\t>>  ')
        user_object_srcdata = str(input('\tPlease provide the path to the file\n\t>>  '))
        # boto3 module function call to put object into bucket
        s3.put_object(Bucket=user_object_destination, Key=user_object_name, Body=user_object_srcdata)
    except ClientError as in_e:
        print('THERE IS A PROBLEM WHICH PREVENTS COMPLETION,\n'
              'CHECK YOUR OBJECT LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    user_menu()
    

def remove_bucket():
    """ function to delete s3 Bucket """
    # determine which bucket the user wants to delete
    try:
        user_bucket_delete = input('\tPlease provice a bucket to delete\n\t>>  ')
        # boto3 module function call to delete a bucket
        s3.delete_bucket(Bucket=user_bucket_delete)
    except ClientError as in_e:
        print('THERE IS A PROBLEM WHICH PREVENTS COMPLETION,\n'
              'CHECK YOUR BUCKET LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    user_menu()
    

def remove_bucket_object():
    """ This function will delete files from a s3 bucket.  The user provides the number of fles that
        need to be deleted in order to speed up the process for mulitiple deletions. """
    # collect user input for variables needed to delete files from a bucket
    try:
        user_bucket_delete = input('\tPlease provide the bucket which contains the file for deletion\n\t>>  ')
        user_object_count = input('\tAre you trying to delete the entire contents?\n\t>>  ').title()
        if user_object_count == 'Y': # deletes more than one file
            # boto3 module function call to delete all objects in a bucket
            s3.delete_objects(Bucket=user_bucket_delete)
        else: # deletes only a single file
            user_object_single_delete = input('\tPlease provide the name of the file for deletion\n\t>>  ')
            # boto3 module function call to delete only a single object
            s3.delete_object(Bucket=user_bucket_delete, Key=user_object_single_delete)
    except ClientError as in_e:
        print('THERE IS A PROBLEM WHICH PREVENTS COMPLETION,\n'
              'CHECK YOUR BUCKET AND OBJECT LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    user_menu()    


def copy_bucket_object():
    """ function to copy data from S3 bucket """
    # user input for variables needed to copy an object into a bucket
    try:
        source_bucket_name = input('\tPlease provide the source bucket\n\t>>  ')
        source_obj_name = input('\tPlease provide the source object\n\t>>  ')
        destination_bucket_name = input('\tPlease provide the destination bucket\n\t>>  ')
    # copy sourse
        copy_source = {'Bucket': source_bucket_name, 'Key': source_obj_name}
        # boto3 module function call to copy an object into a bucket
        s3.copy_object(CopySource= copy_source, Bucket= destination_bucket_name, Key= source_obj_name)
    except ClientError as in_e:
        print('THERE IS A PROBLEM WHICH PREVENTS COMPLETION,\n'
              'CHECK YOUR OBJECT LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    user_menu()


def download_object():
    """ function to download an object from S3 bucket """
    # reassign s3 only for download only, and is returned to 
    # client once the function exits
    s3 = boto3.resource('s3')
    # user input needed to download a file from a s3 bucket
    try:
        bucket_in = input('\tPlease provide the source bucket\n\t>>  ')
        file_in = input('\tPlease provide the name of the file\n\t>>  ')
        new_file_name = input('\tPlease provide the new file name\n\t>>  ')
        # boto3 module function call to download a file from a bucket
        s3.Bucket(bucket_in).download_file(file_in, new_file_name)
    except ClientError as in_e:
        print('THERE IS A PROBLEM WHICH PREVENTS COMPLETION,\n'
              'CHECK YOUR OBJECT LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    user_menu()


def program_termination():
    """ designed for user to confirm exit prior to termination.  
        DATE & TIME displayed upon program termination. """
    try:
        confirm_terminate = input('Are you sure you want to terminate the program?\n\t>>  ').title()
    except IOError as in_e:
        print('THERE IS A PROBLEM WHICH PREVENTS COMPLETION,\n'
              'CHECK YOUR OBJECT LIST AND TRY AGAIN!\n', in_e)
        user_menu()
    if confirm_terminate == 'Y':
        date_and_time = datetime.datetime.now()
        print('here is your time and date object:  ', date_and_time,
              '\nnow be gone')
        exit()
    else: user_menu()


def get_s3_keys(bucket1):
    """  """
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket1)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys


user_menu()

