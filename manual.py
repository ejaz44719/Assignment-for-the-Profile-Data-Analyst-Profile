from bs4 import BeautifulSoup
import csv

def scrape_courses_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the table by ID (if present) or other attributes like class or tag
    course_table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_grdcouncil'})
    
    courses = []
    
    # Iterate over the rows in the table, skipping the header
    for row in course_table.find_all('tr')[1:]:
        # Find the columns in the row
        cols = row.find_all('td')
        if len(cols) >= 2:
            course_title = cols[1].get_text(strip=True)
            courses.append(course_title)
    
    # Create the list with indexes as requested
    course_list = []
    for idx, course in enumerate(courses, 1):
        course_list.append([str(idx), course])
    
    return course_list

# Read HTML content from the file
with open('clg.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use the scraping function
courses = scrape_courses_from_html(html_content)

# Write the output to a CSV file
with open('courses.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Index', 'Course Title'])  # Write header
    writer.writerows(courses)  # Write course data

print("Courses have been written to courses.csv")
