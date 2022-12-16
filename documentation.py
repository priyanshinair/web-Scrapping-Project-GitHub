#TOP REPOSITRORIES ON GITHUB

#STEP 1:
'''
Pick a website and describe your objective

Browse through different sites and pick on to scrape. 
Identify the information you'd like to scrape from the site. Decide the format of the output CSV file.
'''

#outline:
#we're going to scrap "https://github.com/topics/"
#we'll get a list of topics, for each topic we'll get topic title, topic page url and topic description
#for each topic, we'll get the top 25 repositories int hte topic from topic page
#for each repositories we'll grab the repo nae, username, stars and repo URL
#for each topic we'll create a CSV file in the following format:

'''
repo name, username, stras, repo URL
three.js,mrdoob,69700,https://github.com/mrdoob/three.js
etc.
'''



#STEP 2:
'''
Use the requests library to download web pages

Inspect the website's HTML source and identify the right URLs to download.
Download and save web pages locally using the requests library.
Create a function to automate downloading for different topics/search queries.
'''


#STEP 3:
'''
Use Beautiful Soup to parse and extract information

Parse and explore the structure of downloaded web pages using Beautiful soup.
Use the right properties and methods to extract the required information.
Create functions to extract from the page into lists and dictionaries.
(Optional) Use a REST API to acquire additional information if required
'''


#STEP 4:
'''
Create CSV file(s) with the extracted information

Create functions for the end-to-end process of downloading, parsing, and saving CSVs.
Execute the function with different inputs to create a dataset of CSV files.
Verify the information in the CSV files by reading them back using Pandas.
'''


#STEP 5:
'''
Document and share your work!
'''

