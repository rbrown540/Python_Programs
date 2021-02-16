# Richard Brown - SDEV 300
# April 11, 2020
# This module is design to read in a CSV file of existing address records of   
# know Avengers (tm), and eliminate records with missing critical fields. 
# Critical fields include: First and Last Name, Zip Code, and Phone Number.
import re
import pandas as pd

# Read directory file
address_group = pd.read_csv('Directory.csv', sep=',', header=0)
# assign column names
address_group.columns =['First Name', 'Last Name', 'Zip Code', 'Phone Number']


def mung_my_phone_number(value):
    """ Designed to receive an Integer value and determine if the value is
        capable of being in a phone number digit format 3-3-4. If value is
        already in 3-3-4, it is returned. Values that are not 10 digits are
        replaced with empty string """
    
    # match to xxx-xxx-xxxx phone number format.
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    # values containing less than the required 10 integers
    result3 = re.fullmatch(r'\d{3}-\d{3}-\d{4}', value)
    if result:
        # add hyphen to values that are 10 in length and do not have hyphen
        # format is xxx-xxx-xxx
        return '-'.join(result.groups())
    elif result3:
        # value returned if == xxx-xxx-xxxx format already
        return value
    else:
        # return empty string for values that are not formattable
        return ' '


def mung_my_zip_code(value):
    """ Designed to receive an Integer value and determine if the value is
        capable of being in a zip code digit format 5-4 or only 5. If value is
        already in 5-4 format or 5 only, it is returned. Values that are not
        5 or 9 digits are replaced with empty string """
        
    # match to valid format XXXXX-XXXX
    result2 = re.fullmatch(r'\d{5}-\d{4}', value)
    # valid match of NINE digits that can be broken into two groups
    result = re.fullmatch(r'(\d{5})(\d{4})', value)
    # match valid FIVE digit postal zip code
    result1 = re.fullmatch(r'\d{5}', value)
    if result1:
        # return all valid five digit zip code values
        return value
    elif result2:
        # value returned if == xxxxx-xxxx
        return value
    elif result:
        # add hyphen to values that are 9 in length and do not have hyphen
        # format is xxxxx-xxxx
        return '-'.join(result.groups())
    else:
        # return empty sting for values that are not formattable
        return ' '


def mung_my_name(value):
    """ Designed to receive a string value and determine if the value is
        intirely string in value. If the value is string only (no Integers),
        then the value is returned. String that contain non-string characters
        are replaced with an empty string """
    # all character in string are alphanumerical values
    results = re.fullmatch(r'(\D*)', value)
    if results:
        # properly formatted string values are returned
        return value
    else:
        # imporperly formatted string values are replay with empty string
        return ' '


def formatted_values_for_print():
    """ Designed to format each column using the appropriate function call.
        Each value is returned to the address_group DataFrame based on the
        munging function handeling. The entire DataFrame is printed with
        values formatted. """
        
    # format phone number using function then return a value to the DataFrame
    f_phone_number = address_group['Phone Number'].map(mung_my_phone_number)
    address_group['Phone Number'] = f_phone_number
    
    # format zip code using function then return a value to the DataFrame
    f_zip_code = address_group['Zip Code'].map(mung_my_zip_code)
    address_group['Zip Code'] = f_zip_code
    
    # format both first/last names using function then return to the DataFrame
    f_names_last = address_group['Last Name'].map(mung_my_name)
    address_group['Last Name'] = f_names_last
    f_names_first = address_group['First Name'].map(mung_my_name)
    address_group['First Name'] = f_names_first
    
    # print full formatted DataFrame
    print(f'\n\n{address_group.to_string(index=False)}')


print(address_group)
formatted_values_for_print()  # call driver function
