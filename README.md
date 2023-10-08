# WebScraping using BeautifulSoup

This repository is about python libraries requests and BeautifulSoup which are used to extract data from different websites tables.

## Extracting Stock Data Using a Web Scraping.

We will use web-scraping to obtain financial data.  
Using beautiful soup we will extract historical share data from a web-page.

## Steps to be followed for extracting data

1. Send an HTTP request to the webpage using the requests library.
2. Parse the HTML content of the webpage using BeautifulSoup.
3. Identify the HTML tags that contain the data you want to extract.
4. Use BeautifulSoup methods to extract the data from the HTML tags.
5. Print the extracted data

## Step-1 Send an HTTP Request to the webpage

We are using Request library for sending an HTTP request to the webpage.

The requests.get() method takes a URL as its first argument, which specifies the location of the resource to be retrieved. In this case, the value of the url variable is passed as the argument to the requests.get() method, as we've stored a webpage URL in a url variable.

we can use .text method for extracting the HTML content as a string in order to make it readable.

## What is parsing?

In simple words, parsing refers to the process of analyzing a string of text or a data structure, usually following a set of rules or grammar, to understand its structure and meaning. Parsing involves breaking down a piece of text or data into its individual components or elements, and then analyzing those components to extract the desired information or to understand their relationships and meanings.

## Step-2 How to parse data using Beautiful Soup library?

### Create a new Beautiful soup object.

Note: To create a Beautiful Soup object in Python, you need to pass two arguments to its constructor:

1. The HTML or XML content that you want to parse as a string.
2. The name of the parser that you want to use to parse the HTML or XML content. This argument is optional, and if you don't specify a parser, Beautiful Soup will use the default HTML parser included with the library. here in this lab we are using "html5lib" parser.

## Step-3 Identify the HTML tags

We want to extract data from a table on a webpage.So we will be scrapping the content of the HTML webpage and convert the table into a dataframe.

We will creates an empty DataFrame using the pd.DataFrame() function with the desired columns we want to extract.

## Step-4 Use Beautiful soup method for extracting data

We will use find() and find_all() methods of the BeautifulSoup object to locate the table body and table row respectively in the HTML.

The find() method will return particular tag content.
The find_all() method returns a list of all matching tags in the HTML.

## Step-5 Print the Extracted Data

We can now print out the DataFrame using head() or tail() functions
