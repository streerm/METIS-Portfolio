## Module #3 Project Proposal
### Mark Streer (DS/ML)

#### Question / Need:
Sapporo is the capital of Hokkaido, Japan's northernmost island and largest prefecture, as well as its fifth largest city by population. Once host to the 1972 Winter Olympics, the city is also a gateway to internationally renowned ski resorts on the island such as Niseko. Japanese and foreign firms alike would do well to understand the unique characteristics of the Hokkaidoan market. 

This project aims to compile and visualize demographics such as age and household income for different neighborhoods in Sapporo, to inform market research and targeted advertising. Case studies will be introduced for two potential advertising clients: a snowboard & accessories retailer aimed at youth buyers (20-25), and a yoga studio aimed at late-working-age women (50-65).

#### Data Description:

The Sapporo Industrial Promotion Foundation provides a website platform for users to analyze and visualize a number of datasets collected by the municipal government and private entities. Categories range from neighborhood demographics such as age and sex ratio, economic measures such as household expenditures and income, and industry-specific metrics such as ledger balances by bank. I've already pulled several datasets from the organization's platform, [Data-Smart City Sapporo (in Japanese)](https://data.pf-sapporo.jp):  

* Population / no. households by sex, ward
* Population by ward, gender, age group
* No. households by ward, block

These and other relevant datasets will be incorporated as separate tables in a SQLlite database, ultimately for importing and visualizing in Tableau. I hope to overlay relevant data on a map of the city, as indeed the website administrators have already done for several feature sets such as school and park locations ([using Tableau no less!](https://data.pf-sapporo.jp/sapporo_living_map2)).

Physical advertisements such as posters and flyers are widespread in Japanese commerce. Market segmentation using publicly available, readily updated data could prove useful for placing ads where they will make the most impact (regional sales). Two use cases will be presented for variety: youth aged 18-25 (for a boutique winter sporting equipment firm), and women aged 50-65 (for a yoga studio/health promotion). Put simply, "In which ward/block(s) does the greatest number of {market segment} live?"

**Impact Hypothesis**  

Identifying the locations of target demographics will make physical advertising (e.g. posters, flyers) to those demographics more efficient.

#### Tools:

1. Datasets provided by Data-Smart City Sapporo.
2. DB Browser for SQLite, to combine datasets provided separately.
3. Tableau for data exploration.visualization.

#### MVP Goal:
* Data combined in SQL database; plus 
* Tableau visualization of a map of Sapporo City overlaid with the total population of each of its nine main wards.

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


