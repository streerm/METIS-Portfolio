## Module #2 Project Proposal
### Mark Streer (DS/ML)

#### Question / Need:
Digital nomadism is presented to remote workers as an attractive lifestyle which affords travel opportunities in different countries and cultures around the globe. Cities and towns vary greatly in their cost of living, however, meaning not all destinations are equally desirable for a given income level. This project aims to capture how cities' cost of living is influenced by geographic and demographic characteristics as well as key expenses such as rent in a linear regression model, and then to predict cost of living for cities 'off the beaten path' of digital nomads.

#### Data Description:

Feature data will be scraped from two key sources: [Expatistan.com](https://www.expatistan.com/cost-of-living) and Wikipedia. Neither website prohibits or impedes scraping. Each 'observation' will consist of a city and the following features.
Expatistan:
* Single person estimated monthly costs (US$) - **target variable** ("Cost of Living")
* Proxies for typical prices of rent, food, transportation, and Internet ("Monthly rent for furnished studio (85 m2) in normal area", "Basic dinner out for two", "Taxi trip on a business day (8 km)", "Internet (8 Mbps) for one month"; all US$).
Wikipedia:
* Country, Area (km2), Population, Population Density, Year Founded, Latitude, Climate (Koppen classification)

To avoid 150+ dummy variables to represent the countries of the world, they will be encoded as 1. Continent and 2. Country's Human Development Index to simplify analysis.

Expatistan crowd-sources price data for 2000+ cities and towns worldwide, but not all estimates are equally accurate. Fortunately, the number of people who entered price data for a given city is provided at the bottom of its page. 

1. Scrape complete list of cities (and corresponding URLs) on Expatistan's ['All Cities' page](https://www.expatistan.com/cost-of-living/all-cities).
2. From each city page, in addition to Rent, Food, Transportation, and Internet as defined above, scrape the number of price  and distinct user entries (X and Y in the string "...based on X prices entered by Y different people.")
3. Scrape each city's Wikipedia page for seven features listed above.
4. Sort cities descending by distinct users Y: select top 1000 cities for model training (more reliable).
5. Train linear regression model; compare predicted cost of living for other cities with sparse user data (City #1001+).

I expect strong collinearity in the Expatistan data: cities with expensive rent are likely to have expensive food, transportation, Internet, and other typical needs. For the presentation, perhaps unusual results should be the emphasis over the demonstration of a linear relationships (e.g., Seoul has unusually cheap Internet for its cost of living; Beirut has unusually expensive rent; etc.).

#### Tools:

1. [Wikipedia can be scraped using Beautiful Soup](https://towardsdatascience.com/scraping-from-all-over-wikipedia-4aecadcedf11). I will be following this tutorial closely.
2. Expatistan may need to be scraped using Selenium. Prices are presented in local currency, and clicking/reloading will be necessary to get the USD equivalent prices.

#### MVP Goal:
* Cleaned data for top 1000+ countries saved in SQL database; plus 
* Jupyter notebook including scatterplots of interesting relationships with Cost of Living. Probably Rent, Food, Transportation, and Internet first, since they'll be accessible from the same website.

### Template

#### Question/need:
* *What is the framing question of your analysis, or the purpose of the model/system you plan to build?* 
* *Who benefits from exploring this question or building this model/system?*

#### Data Description:
* *What dataset(s) do you plan to use, and how will you obtain the data?*
* *What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?* 
* *If modeling, what will you predict as your target?*

#### Tools:
* *How do you intend to meet the tools requirement of the project?* 
* *Are you planning in advance to need or use additional tools beyond those required?*

#### MVP Goal:
* *What would a [minimum viable product (MVP)](./mvp.md) look like for this project?*


