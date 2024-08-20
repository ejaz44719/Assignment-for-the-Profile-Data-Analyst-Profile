import requests
from bs4 import BeautifulSoup
import csv

def get_courses_by_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        courses = soup.find_all('td')  
        
        course_list = []
        for course in courses:
            course_name = course.get_text(strip=True)
            if course_name:
                course_list.append(course_name)
                
        return course_list
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

def scrape_courses(college_name=None, url=None):
    if url:
        courses = get_courses_by_url(url)
        return courses
    elif college_name:
        predefined_urls = {
            'Aryabhatta College': 'https://aryabhattacollege.ac.in/ourcourses.aspx',
            'Atma Ram Sanatan Dharma College': 'https://arsdcollege.ac.in/under-graduate-courses/',
            'Ayurvedic & Unani Tibia College': 'https://autch.delhi.gov.in/autch/courses',
            'Bhim Rao Ambedkar College': 'https://www.drbrambedkarcollege.ac.in/courses',
            'Dyal Singh College': 'https://www.dsc.du.ac.in/courses-offered',
        }
        if college_name in predefined_urls:
            courses = get_courses_by_url(predefined_urls[college_name])
            return courses
        else:
            print("College not found in predefined URLs.")
            return []
    else:
        print("Please provide either a college name or a URL.")
        return []

college_names = [
    'Aryabhatta College',
    'Atma Ram Sanatan Dharma College',
    'Ayurvedic & Unani Tibia College',
    'Bhim Rao Ambedkar College',
    'Dyal Singh College'
]


# Create or open a CSV file to write
with open('courses_all.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['College Name', 'Course Number', 'Course Name'])  # Header row
    
    # Fetch and write courses for each college
    for college_name in college_names:
        courses = scrape_courses(college_name=college_name)
        for idx, course in enumerate(courses, 1):
            writer.writerow([college_name, idx, course])
    
print("Data has been written to 'courses.csv'")
