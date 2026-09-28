# Fake Job Scraper

A simple Python project that scrapes fake job listings from Real Python and saves the data into a CSV file.

## What this project does

This script visits the fake jobs website, extracts job details such as:

- Job title
- Company name
- Location
- Job link

Then it stores the collected data in a CSV file named `fake_jobs.csv`.

## Technologies used

- Python
- Requests
- BeautifulSoup
- Pandas

## Project structure

```text
roadmapsh-data-analyst-project/
├── python_fake_job_scraping/
│   └── fake_jobs_scrap.py
├── fake_jobs.csv
└── Readme.md
```

## How to run

1. Open your terminal.
2. Go to the project folder.
3. Install the required packages:

```bash
pip install requests beautifulsoup4 pandas
```

4. Run the script:

```bash
python python_fake_job_scraping/fake_jobs_scrap.py
```

## Output

After running the script, a file called `fake_jobs.csv` will be created in the project folder.

## Purpose

This project is a beginner-friendly data collection exercise for learning web scraping and working with structured data in CSV format.
