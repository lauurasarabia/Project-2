# Project-2 - WWE Wrestlers
Data analysis - Python, API, Web Scrapping

![logo](https://github.com/lauurasarabia/Project-2/blob/main/images/logo-WWE.png?raw=true)


The main available tool to carry out this project was the WWE Wrestlers personal data (name, date of birth, nº of titles, etc).

# - 1_WWE Wrestlers
Database has been cleaned and prepared for being analysed in this notebook. 
These are the steps we have followed for cleaning: 
* Drop columns we are not going to use
* Change date of birth format for being able to work with it later
* Create some conditions to discover their horoscope
* Rename the columns

Do you think that their horoscope had something to do with their wins?

![John_Cena](https://github.com/lauurasarabia/Project-2/blob/main/images/png-transparent-john-cena-wwe-raw-poemas-de-amor-professional-wrestler-the-nexus-john-cena-tshirt-logo-jersey-thumbnail.png?raw=true)

# - 2_Scraping
On the other hand, Web Scraping has been used to know who was their adversary in their final battle.
Steps:
* Look for the information of the defeated person in battle in a website
* Download the table information and turn it into Pandas DataFrame
* Rename columns, remove unnecessary information, change column types to str in order to be able to merge both tables (WWE_Wrestlers)
* Merge, reset index
* Extract horoscope values from WWE_Wrestlers table and apply them to adversaries column

# - 3_Visualizations
 With all this data we navigate through the following visualizations:
 
 Who are our TOP 5 Wrestlers?
 
 
 
 Which is the strongest horoscope?
 
 
 
 Taurus vs Sagittarius battles



 
# - 4_API
We found an API which takes both names (winner and defeated) and makes a love percentage compatibility between them. So why not use it for our analysis? We have created a new column in our DataFrame with the results.

What are you waiting for? Go explore it!🧐





