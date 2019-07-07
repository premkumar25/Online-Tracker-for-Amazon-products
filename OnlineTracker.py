import requests
from bs4 import BeautifulSoup
import smtplib      #used to send email


#copy the url of the item which you want to search
URL = 'https://www.amazon.in/gp/product/B07KY3K2YG/' \
      'ref=s9_acsd_top_hd_bw_b1Vzlo7_c_x_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-11&pf_rd_' \
      'r=F17PHM1QQ1FT0Q8J7HTV&pf_rd_t=101&pf_rd_p=e1b534f1-3276-56a6-91b1-814616b41341&pf_rd_i=1388921031'

#search for user agent in your browser and copy the link available
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


#function to check the price of the product
def check_price():

    page = requests.get(URL, headers=headers)

    #parse the url and scrap the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    #search for the id in the url using developer option(Use F12 key) and enter the correct id to search
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    #display the price of the product in float value upto 5 digits excluding rupee symbol
    converted_price = float(price[1:5])

    print(title.strip())
    print(converted_price)

    #condition to check the price is lower or not
    if converted_price < 500:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Here '#' is the user email id and * is the app password created (Check README)
    server.login('#########@gmail.com', '*******')

    sub = 'Price dropped'
    body = 'Check the below link https://www.amazon.in/gp/product/B07KY3K2YG/' \
      'ref=s9_acsd_top_hd_bw_b1Vzlo7_c_x_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-11&pf_rd_' \
      'r=F17PHM1QQ1FT0Q8J7HTV&pf_rd_t=101&pf_rd_p=e1b534f1-3276-56a6-91b1-814616b41341&pf_rd_i=1388921031'

    msg = f'Subject: {sub}\n\n{body}'
    server.sendmail(
        '#########5@gmail.com',   #Sender mail id, Should be same as the server login id
        '#########@gmail.com',     #Receiver mail id, Can be of any id
        msg
    )
    print('Email sent')

    # After completing it is necessary to quit the server
    server.quit()


#Calling the function
check_price()

