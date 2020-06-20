# Datamining
### Data Mining Project
### Assignment – Finding Cheapest Air Flights Between Two Locations
#### Introduction:
Frequent travelers are always looking for cheap flight prices between two destinations in order to make a decision to book air tickets. Most flight bookings nowadays happen online, and flight booking websites contain lot of data about flights. By webscraping the data, it is possible to find ways of mining the data for real-world applications. One of the real-world problems is to find the cheapest fare between two destinations. This project aims to deploy an app that will provide the cheapest flight ticket price between two destinations on specific dates. This will help flyers to save cost and effort by using our app to book the cheapest flight.
#### Project Overview:
The project consisted of five milestones:
1)	Acquisition of flight price data
2)	Management of data by storing in datalake
3)	Processing of data
4)	Interpretation of data and Communication of Insights
5)	Deployment in mobile app using Kivy

This project was done using Python 3.8 and Pycharm Community Edition. The websites used for scraping were Expedia and Google Flights. Selenium package was used to do webscraping. Microsoft Azure was used as a datalake. The project was deployed in an app using kivy package.

#### Project Details:
#### 1)	Acquisition of flight price data.
First, we need to scrape the flight price data from a website containing flight prices. This can be done using Selenium in combination with Chrome webdriver.  The url passed for the webscraping was Expedia webpage.
Selenium is a library for accessing websites and automation testing. Chrome driver is a software than can open a browser automatically.
The url of Expedia was provided to the get function of browser which used Chromedriver to open a browser window with the Expedia URL. Within the Expedia webpage, the buttons for opening the flights page was located using Xpath. The inputs were fed into the text boxes for starting location, destination, travel date and return date. 
The webpage with the flights and the flights data was scraped to obtain the prices. These prices were entered into a dataframe along with the flight details. Finally, the dataframe is written and stored onto an Excel sheet.


#### 2)	Management of data in datalake.
The data obtained through webscraping will be stored in a datalake on Microsoft Azure. First, an account is created on Microsoft Azure.In Microsoft Azure, an active directory is created.
The datalake on Microsoft Azure has a tenant ID, account name and ResourceID. Using auth function, a credentials object is created for the Microsoft Azure account. This is then used to create a file system object adlsFileSystemClient. Once authentication is done, a directory is created within Microsoft Azure Active Directory.
Using the ADLUploader function, the file from the local machine is uploaded to the directory on Microsoft Azure datalake

#### 3)	Processing of data
Data present in datalake can be accessed using Python code. This is done through using the libraries in azure datalake. 
First, a connection is made to Microsoft Azure using the lib.tenant function. The tenant id of the Microsoft Azure datalake and the resource URL are passed as arguments to the lib.tenant function.
This creates a token.
After the connection is made, an adlsFileSystemClient object is made by passing the token and the resource name to the AzureDLFileSystem function.
Using the adlsFileSystemClient, the file on datalake is opened for reading by passing the filename to the open function. Then, the contents of the file are stored in a dataframe for processing.

#### 4)	Interpretation of data and Communication of Insights
The data obtained from the webscraper and stored in datalake is cleaned and processed. First, the column names are modified to make it clear what they are referring to. Next, the prices data are processed to remove the currency symbol land commas within the numbers. Finally, it is converted into an integer and stored in the dataframe.
Finally, the minimum price is calculated from the price column using the min() function. Multiple insights are drawn from the data by plotting the price vs duration of flight bar plot. The higher the duration, higher the price.
Another insight is obtained by plotting departure time vs price, which gives the best departure time for the cheapest price.

#### 5)	Deployment in mobile app using Kivy
Finally, the project is deployed as a mobile app using Kivy. Kivy is a python package that provides a framework for deploying the Python code to a mobile app. 
First, the kivy library is imported. From the kivy library, App, Label, Button, GridLayout and TextInput are imported.
The DemoGridLayout Class uses the GridLayout object to create a grid specified in the demo.kv file. Kv files are files that provide the UI design framework for the kivy app. It is similar to CSS and provides the specifications for the widgets on the app. 
First the app is built using the DemoApp class. It returns the DemoGridLayout which launches the app window. In the app window, there are input text boxes for source, destination, start date, and return date. Below the input text boxes, there is a button Check for Minimum Price. When the button is clicked, a function main() is launched which runs the python code for webscraping flights data and finding the cheapest flight price.
The cheapest flight price data is sent to the Label which displays the output. To clear the values and reenter a new set of values, a Clear button is provided. When the Clear button is pressed, the clear function is run which resets the values in the input and the output text boxes. The app can be run again.
As kivy apps can be packaged into mobile apps only using Linux system, it hasn’t been packaged into a mobile app.  
