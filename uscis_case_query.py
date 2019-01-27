#!/usr/bin/env python3

import argparse
import lxml.html
import re
import requests

def query_case(case_number):
    """
    func: query a receipt number and return case status
    """
    if len(case_number) > 13:
        print('ERROR: %s: invalid length of the receipt number.' %(case_number))
    else:
        query_form = {}
        query_form['appReceiptNum'] = case_number
        query_form['initCaseSearch'] = "CHECK STATUS"
        query_form['changeLocale'] = ""

        s = requests.session()
        query_response = s.post(uscis_q_url, data=query_form)
        if query_response.status_code == 200:
            query_response_html = lxml.html.fromstring(query_response.text)
            query_response_xpath = query_response_html.xpath('//h1')
            query_response_text = query_response_xpath[0].text
            """
            query_response_text can return 2 empty lines if no result found. it's 
            necessary to check the return string in \w+ pattern
            """
            if query_response_text != None and re.match(r'\w+', query_response_text):
                print('%s: %s' %(case_number, query_response_text))
            else:
                print('ERROR: %s: no result returns' %(case_number))
        else:
            print('ERROR: %s: USCIS portal returns non-200 response code %d.' %(case_number, query_response.status_code))

if __name__ == '__main__':
    """
    initialize vars
    """
    uscis_q_url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'

    """
    set up args
    """
    parser = argparse.ArgumentParser(description="USCIS Case Query Tool")
    parser.add_argument("-c", "--case", type=str, required=True, help="USCIS receipt number")
    args = parser.parse_args()

    case_number = args.case

    query_case(case_number)
