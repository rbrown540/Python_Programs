# 
# 
# 
# 
# 
# import boto3 
# create client
s3 = boto3.client('s3')

def user_menu():
    print('\t1: View Group Schedule\n',
          '\t2: Register for Group Class\n',
          '\t3: Unregister for Group Class',
          '\t4: Download Group Schedule\n',
          '\t5: Body Mass Index Calculator\n',
          '\t6: Upload Exercise Photo for Social Media Posting\n',
          '\t0: Exit')
     
    try:
        user_selection = int(input('\n Please enter your menu selection:\n\t>>>>  '))
    except ValueError as in_e:
        print('TRY SOMETHING ELSE, LIKE FOLLOWING INSTRUCTIONS,\n'
              'OR SIMPLY PICKING A NUMBER FROM THE LIST!\n', in_e)
        user_menu()
                               
    while user_selection != 0:
        
        if user_selection == 1:
            view_schedule()
        elif user_selection == 2:
            register_class()
        elif user_selection == 3:
            unregister_class()
        elif user_selection == 4:
            download_schedule()
        elif user_selection == 5:
            bmi_index()
        elif user_selection == 6:
            upload_photo()
        else:
            print('\nNOPE!!\nMake a selection from THIS menu')
            user_menu()
    print('ZERO')
    



def view_schedule():
    """ """


def register_class():
    """ """


def unregister_class():
    """ """


def download_schedule():
    """ """


def bmi_index():
    """ """


def upload_photo():
    """ """



user_menu()
