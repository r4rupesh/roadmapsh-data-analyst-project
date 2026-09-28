import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://realpython.github.io/fake-jobs/'

def fake_job_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_elements = soup.find_all('div', class_='card-content')

    job_data = []
    for job_element in job_elements:
        title_element = job_element.find('h2', class_='title')
        company_element = job_element.find('h3', class_='company')
        location_element = job_element.find('p', class_='location')
        link_element = job_element.find('a')

        title = title_element.text.strip() if title_element else 'No Title Found'        
        company = company_element.text.strip() if company_element else 'No Company Found'
        location = location_element.text.strip() if location_element else 'No Location Found'
        link = link_element['href'] if link_element else 'No Link Found'

        job_data.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'Link': link
        })

    return  pd.DataFrame(job_data).to_csv('fake_jobs.csv', index=False)
fake_job_data()