# python url-crawler
A python script application for web url crawling

# Feature
1. By giving a valid http or https url domain you can get all of it's url according to suffix
2. Then it's find the inner url from the main url list
4. It is filter all url by your required suffix like .com, .gov etc.
3. By completing find url it's create a data base schema table and a csv file for storing url list

# How can you run it ?
1. You need to install python(python2) first on your machine
2. Then install git and clone it to your folder
3. Install the requirments file from requirments.txt
4. Then simply run script on your terminal  -  'python url_crawl.py'
5. If you face IP blocking problem then you can use tor for change ip address for every request
6. You can use cron service for running this script automatically on a shedule

## Setup Crontab on your machine for your script
1. first create a crontab file like service.cron
vim or nano service.cron
2. edit the file and write this code

* * * * * your script

3. eg: 30 12 * * * python url_crawl.py
4. This is indicate that your script will run every day at 12.30pm automatically
5. Save and exit and add the cron file into cron tab

crontab service.cron

6. check is it done

crontab -l

Thank you all
