'''
give the url , file name
'''
 
import requests
from bs4 import BeautifulSoup 
import lxml
import csv
import time
import random

#url_text ='https://www.booking.com/searchresults.en-gb.html?ss=Bangalore%2C+Karnataka%2C+India&ssne=India&ssne_untouched=India&label=in-HvtKIh8HYqxrATaP24vtSgS513276691127%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-303403359744%3Alp9181358%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGgfEoJVv7zYo&sid=af032abd238e1b7c6567de252787cb2f&aid=1610687&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2090174&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=8aa07a2c85710e0c&ac_meta=GhA4YWEwN2EyYzg1NzEwZTBjIAAoATICZW46BGJlbmdAAEoAUAA%3D&checkin=2025-04-07&checkout=2025-04-08&group_adults=2&no_rooms=1&group_children=0'
#mumbai=https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi%2C+Delhi+NCR%2C+India&ssne=Bangalore&ssne_untouched=Bangalore&efdco=1&label=in-HvtKIh8HYqxrATaP24vtSgS513276691127%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-303403359744%3Alp9181358%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGgfEoJVv7zYo&sid=af032abd238e1b7c6567de252787cb2f&aid=1610687&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2106102&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b7de6852bf36003b&ac_meta=GhBiN2RlNjg1MmJmMzYwMDNiIAAoATICZW46BWRlbGhpQABKAFAA&checkin=2025-04-09&checkout=2025-04-10&group_adults=2&no_rooms=1&group_children=0

def webscraper1(web_url,f_name):

    #greetings
    print('Thank you for sharing the url and filename!\n Reading the content')

    num= random.randint(3,7)

    #processing
    time.sleep(num)

    header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
    response = requests.get(web_url, headers=header)

    if response.status_code == 200:
       print("connected to the website")
       html_content = response.text
    
       # creating soup
       soup = BeautifulSoup(html_content,'lxml')
       #print(soup.prettify())
    
       #main containers
       hotel_divs = soup.find_all('div',role="listitem")
    
    
       with open(f'{f_name}.csv', 'w', newline='', encoding='utf-8') as file_csv:
         
         writer = csv.writer(file_csv)

         #adding header
         writer.writerow(['hotel_name','locality','price','rating','score','review','link'])
         

         for hotel in hotel_divs:
            hotel_name= hotel.find('div',class_="f6431b446c a15b38c233").text.strip()  
        
            location = hotel.find('span',class_="aee5343fdb def9bc142a").text.strip()
        
            price = hotel.find('span',class_="f6431b446c fbfd7c1165 e84eb96b1f").text.strip().replace('₹ ','')
        
            rating_div = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb")
            rating = rating_div.text.strip() if rating_div else "No rating"


            score_div = hotel.find('div', class_="a3b8729ab1 d86cee9b25")
            score = score_div.text.strip().split(' ')[-1] if score_div else "No score"

            review_div = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47")
            review = review_div.text.strip() if review_div else "No review"

            # getting the link
            link = hotel.find('a',href=True).get('href')
  
            # saving the file into csv
            writer.writerow([hotel_name,location,price,rating,score,review,link])
        
         print("web scrapped done")
            #  print(hotel_name)
            #  print(location)
            #  print(price)
            #  print(rating)
            #  print(score)
            #  print(review)
            #  print(link)
            #  print('')
  
    else:    
      print(f"connection failed! {response.status_code}")
 

#if using this script directly than below task will be executed

if __name__ == '__main__':
   url = input("please enter url! :")
   fn = input('pleaase give file name! :')


   # calling the function 
   webscraper1(url,fn)