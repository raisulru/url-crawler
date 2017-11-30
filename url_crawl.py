import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
import re
import sqlite3
import csv
from tqdm import tqdm


def find_url(url):
    # connect to a URL
    try:
        website = urllib2.urlopen(url)
    except HTTPError as e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError as e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason


    # read html code
    try:
        html = website.read()
    except NameError:
        print "Your URL is not valid"
    except ValueError:
        print "Your URL is not valid"


    '''
    Find all links from your 
    domain which have http or 
    https protocol
    '''
    links = []
    try:
        # use re.findall to get all the links
        links = re.findall('"(http|https?://.*?)"', html)
    except NameError:
        print 'Your input url may be wrong'

    return links


def filter_url(links, suffix):
    return [s for s in links if suffix in s]


def find_inner_url(link_list):
    link_list = link_list
    for link in tqdm(link_list):
        inner_links = find_url(link)
        # Add all links into link_list
        link_list = link_list + inner_links
    return link_list


def store_database(final_list):
    conn = sqlite3.connect('url.db')
    c = conn.cursor()
    c.execute(
        '''DROP TABLE IF EXISTS crawl'''
    )
    c.execute(
        '''CREATE TABLE crawl (url text)'''
    )
    for item in tqdm(final_list):
        c.execute('insert into crawl values (?)', (item,))


def csv_creator(final_list):
    with open('url.csv', 'wb') as f:
        writer = csv.writer(f)
        for val in tqdm(final_list):
            writer.writerow([val])


def main():
    input_url = str(raw_input(
        'Please input a url (example: "https: or http://www.brainstation-23.com/"): '
    ))
    input_domain_type = str(raw_input(
        'Please input a required suffix without dot(.) (eg: "com", "org", "gov"): '
    ))
    # Find all link from given domain
    main_links = find_url(input_url)
    # filter link which have required domain suffix
    filter_list = filter_url(main_links, input_domain_type)
    # Now search for inner links and add it to the filter_list
    all_list = find_inner_url(filter_list)
    # filter inner_link which have required domain suffix
    final_list = filter_url(all_list, input_domain_type)
    # add input url at first of the list
    final_list.insert(0, input_url)
    # create a database schema and a csv file for store
    if final_list:
        store_database(final_list)
        csv_creator(final_list)
        print "You have stored {} data succesfully".format(len(final_list))
    else:
        print "You have not any url for store"


if __name__ == "__main__":
    # execute only if run as a script
    main()
