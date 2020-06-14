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
            try:
                query_response_case_status = query_response_html.xpath('//div[@class=\'rows text-center\']/h1')[0].text_content()
                query_response_case_text = query_response_html.xpath('//div[@class=\'rows text-center\']/p')[0].text_content()
            except:
                print('ERROR: %s: no result returns' %(case_number))
            else:
                print('%s: %s\n\n%s' %(case_number, query_response_case_status, query_response_case_text))
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
