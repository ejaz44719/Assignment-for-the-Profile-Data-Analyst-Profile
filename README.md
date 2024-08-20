# web-scraping
A Python script that scrapes the list of courses being offered by different colleges in India. This script takes either the name of the college or the URL of the college's course page as input and return a list of all courses offered by that college.

# Course Scraper Script
## Overview

This script is designed to scrape course offerings from a CSV file containing information about various colleges. It processes the data to filter out irrelevant rows, cleans up the course information, and provides a summary of the courses available at each college.

## Requirements

- Python 3.12
- Pandas
- Matplotlib

You can install the required packages using pip:

```bash
pip install pandas matplotlib

```

# Script Usage
## Prepare the CSV File
Ensure that you have a CSV file with columns named College Name, Course Number, and Course Name. The file should be formatted correctly with these columns.

## Save the Script

Save the Python script to a file, e.g., main.py

## Run the Script
Execute the script from the command line:

```bash
python main.py
```

## Assumptions

- The CSV file is correctly formatted with columns `College Name`, `Course Number`, and `Course Name`.
- Course numbers are numeric or can be coerced into numeric values.
- Course names are not empty or irrelevant.
- The script assumes that there are no duplicate entries for the same course.

## Limitations

- The script does not handle missing or incorrect data beyond basic filtering.
- It assumes that the CSV file is well-formed and does not contain any unexpected formats or characters.
- The visualization will be basic; more sophisticated visualizations may require additional libraries or custom code.

## Future Enhancements

- Handle more complex data formats or additional fields.
- Improve error handling and data validation.
- Enhance visualizations for better insights.<br>

- To save this as a `.md` file:

1. Open a text editor (e.g., Notepad, VSCode, or any code editor).
2. Paste the content above.
3. Save the file with the name `README.md`.



This README file provides clear instructions on how to use the script, its assumptions, limitations, and potential future enhancements.

REFERENCES
Beautiful soup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ pandas and matplotlib documentation: https://tanthiamhuat.files.wordpress.com/2018/04/pythondatasciencehandbook.pdf Request documentation: https://realpython.com/python-requests/

This README file provides clear instructions on how to use the script, its assumptions, limitations, and potential future enhancements.

