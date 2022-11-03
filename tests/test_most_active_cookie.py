import sys
import glob
import pytest
sys.path.append('..')
from most_ac_cookie import get_parameters,get_dataframe


def get_test_parameters(test_file):

    test_cookie_data = []

    with open(test_file) as f:
        
        data = []

        for line in f.readlines():

            data.append(line)
        len_data = int(data[0])
        test_cookie_data = data[1:len_data+1]
        test_given_date = data[len_data+1].replace('\n','')
        if len_data+2 <= len(data):
            expected_output = ''.join(data[len_data+2:])
        else:
            expected_output = ''

       
    return test_cookie_data,test_given_date, expected_output



def get_files():
    
    files = glob.glob('../tests/test_case*.txt') 
  
    return files

@pytest.mark.parametrize("test_cookie_data,test_given_date,expected_output",[get_test_parameters(filee) for filee in get_files()])

def test_most_active_cookie(test_cookie_data,test_given_date, expected_output):
    
    assert '\n'.join(get_dataframe(test_cookie_data,test_given_date))== expected_output