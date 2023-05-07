# -*- coding: latin-1 -*-

import csv
import requests
from bs4 import BeautifulSoup
 
file = open('linkedin-jobs.csv', 'w',encoding="utf-8",newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Company', 'Location', 'DatePosted'])

 
def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')
    
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_date_bool = job.find('time')
        print(job_location)
        if job_date_bool:
            job_date = job_date_bool['datetime']
        
        writer.writerow([
        job_title.encode("utf-8").decode('utf-8'),
        job_company.encode("utf-8").decode('utf-8'),
        job_location.encode("utf-8").decode('utf-8'),
        job_date.encode("utf-8").decode('utf-8')
        ])
    
        print('Data updated')
    if page_number < 10000:
        page_number = page_number + 25
        linkedin_scraper(webpage, page_number)
 
    else:
        file.close()
    print('File closed')
 
linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%2BAnalyst&location=%C3%8Ele-de-France%2C%2BFrance&locationId=&geoId=104246759&f_TPR=r2592000&start=',0)
