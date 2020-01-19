# Step 1 : Program

from bs4 import BeautifulSoup
import requests
import csv
import time
import os

# import urllib2
# from bs4 import BeautifulSoup
# import csv
# from datetime import datetime
# import os
# import schedule
# import time


pages=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

	
with open('C:/Users/Karthik/Desktop/scrap/scraping.csv','a') as f_output:
	csv_print=csv.writer(f_output)
	
	file_is_empty=os.stat('C:/Users/Karthik/Desktop/scrap/scraping.csv').st_size==0
	if file_is_empty:
	    csv_print.writerow(['Review','Username'])
	for page in pages:
	    source=requests.get('https://www.bankbazaar.com/reviews.html?reviewPageNumber={}'.format(page)).text
	    soup=BeautifulSoup(source,'html.parser')
	    for jobs in soup.find_all('li',{'class':'review-box'}):
	        review=jobs.find('div',{'class':'text_here review-desc-more'}).text.strip()
	        user_name=jobs.find('a',{'class':'user-review-comment js-individual-title'}).text.strip()
	        csv_print.writerow([review,user_name])
	        time.sleep(2)


