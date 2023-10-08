import requests
from bs4 import BeautifulSoup
import pandas as pd


# We will extract netflix stock data from this website.
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'

r = requests.get(url)

#Creating a soup object.
soup = BeautifulSoup(r.text, 'html.parser')


# we will be scrapping the content of the HTML webpage and convert the table into a dataframe.
#We will creates an empty DataFrame using the pd.DataFrame() function with the following columns.
#"Date"
#"Open"
#"High"
#"Low"
#"Close"
#"Volume"

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "volume"])

# Intialize an empty list to store the data
data_list = []

for row in soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    # Append the data of each row as a dictionary to the list.
    data_list.append({"Date":date, "Open":open, "High":high, "Low":low, "Close":close,"Adj Close":adj_close, "Volume":volume})


# Create the DataFrame from the list of dictionaries
netflix_data = pd.DataFrame(data_list)

# print the extracted data
print(netflix_data.head(50))

# now we can save this data into a CSV file

file_path = 'netflix-data.csv'
netflix_data.to_csv(file_path, index=True)

print(f"DataFrame saved to '{file_path}'")