import argparse
from datetime import datetime
from collections import OrderedDict

def get_parameters():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('--file')
    parser.add_argument("-d")

    args = parser.parse_args()


    return args.file, args.d

def get_data(path_file):

    cookie_data = []

    with open(path_file) as f:

        for line in f.readlines():
            if line !='cookie,timestamp\n':

                cookie_data.append(line)
    return cookie_data


def get_dataframe(cookie_data, given_date):



    cookie_dict = OrderedDict()

    given_date = datetime.strptime(given_date, '%Y-%m-%d').strftime('%Y-%m-%d')

    for data in cookie_data:

        data_timestamp = datetime.strptime(data.split(',')[1].replace('\n',''),'%Y-%m-%dT%H:%M:%S%z')
       
        if data_timestamp.strftime('%Y-%m-%d') == given_date:
            cookie = data.split(',')[0]

            
            if cookie in cookie_dict:
                cookie_dict[cookie]+=1
            else:
                cookie_dict[cookie]=1

   
    if len(cookie_dict) == 0:
        return ''
    else:
        max_occurance = []
        max_val = max(cookie_dict.items(),key = lambda x: x[1])

        for k,v in cookie_dict.items():
            if v == max_val[1]:
                max_occurance.append(k)

        return max_occurance