from apify_client import ApifyClient
import os 
from dotenv import load_dotenv
import requests
load_dotenv()

apify_client = ApifyClient(os.getenv("Apify_Api_Key"))


SCRAPINGDOG_API_KEY = os.getenv("Scrapdog_Api_Key")  # Make sure key name matches your .env

def fetch_linkedin_jobs(search_query, location="india", page=1, sort_by=None, job_type=None,
                        exp_level=None, work_type=None, filter_by_company=None):
    """
    Fetch LinkedIn jobs using the Scrapingdog API.
    
    Args:
        search_query (str): Job title or keywords.
        location (str): Job location. Default is 'india'.
        page (int): Pagination page number.
        sort_by (str): Sorting criteria ('R', 'DD', etc.).
        job_type (str): 'F' for Full-time, 'P' for Part-time, etc.
        exp_level (str): Experience level filter.
        work_type (str): Work arrangement ('R' Remote, etc.).
        filter_by_company (str): Company name filter.

    Returns:
        dict: JSON data containing job listings.
    """
    
    url = "https://api.scrapingdog.com/linkedinjobs"

    params = {
        "api_key": SCRAPINGDOG_API_KEY,
        "field": search_query,
        "geoid": "",
        "location": location,
        "page": page,
        "sort_by": sort_by or "",
        "job_type": job_type or "",
        "exp_level": exp_level or "",
        "work_type": work_type or "",
        "filter_by_company": filter_by_company or ""
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Scrapingdog request failed: {response.status_code} - {response.text}")



# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location = "india", rows=60):
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs