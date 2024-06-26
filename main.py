import requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key="********"
api_key_news="*****************"

stock_params={
    "function" : "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":api_key
}

news_params={
    "q":COMPANY_NAME,
    "apiKey":api_key_news,
    "pageSize":3
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response=requests.get(url=STOCK_ENDPOINT,params=stock_params)
data=response.json()
print(data)

# price_today=[newvalue for value in data[Time Series (Daily)]]

price_today=float(response.json()["Time Series (Daily)"]["2024-02-09"]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
price_yesterday=float(response.json()["Time Series (Daily)"]["2024-02-08"]["4. close"])
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_diff=round(abs(price_yesterday-price_today),2)
# print(price_diff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
price_percent_diff=round((price_diff/price_yesterday)*100,2)
# print(price_percent_diff)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if price_percent_diff >2:
    response_news=requests.get(url=NEWS_ENDPOINT,params=news_params)
    first_three_articles=response_news.json()["articles"][:3]
    article_headline=[article["title"] for article in first_three_articles]
    article_description=[article["description"]for article in first_three_articles]
    # print(article_description)
    # print(article_headline)
    for article in first_three_articles:
        account_sid = "***************"
        auth_token = '***********'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}:{price_percent_diff}%\nHeadline:{article['title']}\nBrief:{article['description']}",
            from_='+12138954***',
            to='+1647877****'
        )
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

