#STEP 1:

import requests
from bs4 import BeautifulSoup

topics_url = 'https://github.com/topics'

response = requests.get(topics_url)

#a = response.status_code
#print(a)


page_content = response.text    #content
#len(response.text)       #not recommended to print just check out the line

page_content[:1000]     #first 1000 characters


#writing the html code in a file
#with open('webpage.html','w') as file:
#    file.write(page_content)





#STEP 2:
doc = BeautifulSoup(page_content,'html.parser')

'''
q = type(doc)
print(q)
'''


'''
p_tags = doc.find_all('p')
a = len(p_tags)
print(a)

a = p_tags[:5]
print(a)
'''

#finding the 3D topic title using class
selection_class = "f3 lh-condensed mb-0 mt-1 Link--primary"
topic_title_tags = doc.find_all('p',{'class':selection_class})


#checking the description related to 3D topic 
desc_selector = 'f5 color-fg-muted mb-0 mt-1'
topic_description_tags = doc.find_all('p',{'class':desc_selector})
print(topic_description_tags)


#find the url of the 3D topic page
topic_title_tag0 = topic_title_tags[0]
topic_title_tag0.parent











