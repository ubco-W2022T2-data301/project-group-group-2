# 1 DATA 301 Final Report

### Introduction:

For our project, our group took a look at the housing market in canada in order to address some potentially common concerns involving the housing market here in canada, as it has been an important issue as of late. We took the opportunity to look at data from Stats Canada in order to come to form so data-based conclusions on ou work. Our Dataset was quite complicated, so form simplicities sake we isolated a lot of speciofic data from the Datasets, as analysing the entire dataset in all collumns would have taken ages. We crafted our research questions based on what we personally deemed the most interesting and potentially the most valuable questions that maybe other students make take some interest in. A large portion of the talk around the housing market is the pricing of the market and especially for Students at UBC Vancouver, and increasingly UBCO as well, the price of Housing has looked worse year-to-year. Following from that we will each give a short synopsis of some of the EDA discoveries that we each made, and how it may either enforce or scew our final results, or if it was just an interesting fact.



##### Jack's EDA findings: 
Because my research question delved into the trends in value over the past year, The largest and most interesting EDA findings I had was the Differences between provinces in terms of Value over time. The biggest Outlier that I personally found was actually the entire province of BC up untill the mid 2000's.
![British Columbia](/images/index_BC.png) 
While almost all the other provinces had most only increase in value over time, BC had a completely sparatic history, with having massive shifts in value. While the other graphs seemed so reflect more of a trend that may mirror what people would expect, BC's history of values looks more like a roller coater you would find at a theme park. What make it so interesting was that the value was so large, even back in 1981. BC was by far the most expensive place to live for a very long time, yet it still had massive ups and downs, which indicate there may be more to that story. Looking deeper into the topic, Vancouver Hosted the EXPO 86 a massive wolrdwide event that skyrocked the prices of basically everything in Vancouver, subsequently, the sharp decrease in housing prices right ater could have been due to the fallout after the event.

Another smaller thing I would like to also mention is that in terms of provinces, Ontario was the  most linear in terms of the increases, which in my personal opinion could have been due to the goverment being situated there, perhaps resulting in more attention to stricter housing price guidlines. Following that Alberta Seemed to experience the least linear (outside BC) and was affected the most by the 2008 crash and 2019 COVID outbreak. Contrary to Ontario this could potentially be due to Alberta generally being more conservative, and therefore more lax on the rules of the housing market. Tha allowed land owners to list prices at very high prices during rough times which could have caused the sharp increases you can see on the graphs.



##### Aditya's EDA findings:
The primary objective of this research was to look into the trends and patterns that emerged in the housing index data among all of the months and provinces in our dataset, which spanned the entire time period. By examining the patterns of rising or falling housing index value, I hoped to get insight into the variables that affect a state's economic demography and why some months are the most expensive to live in. 

Our investigation produced a number of intriguing results. First, we noticed significant differences in the housing index values among the provinces. It's interesting to note that most of the provinces with rising housing index values and the highest values overall weren't those with steadily rising real estate prices. Secondly, we pinpointed specific months that had a tendency to be the most expensive to live, this analysis made perfect sense when we looked at Canadian weather patterns and the ability of individuals to work in them.

![max_Prov](/images/max_province.png) 
Here we see that the highest housing index value ever hit was from quebec and manitoba but these were the province which didn't see a steady increase in their housing index values. 

In some provinces, we also discovered trends in the values of the housing index that could be explained by variations in the population density, the average income, and unemployment rates. According to our analysis, these variables may have an effect on the dynamics of supply and demand in the housing market, which in turn impacts the values of housing indexes. For example PEI having the most steady growth in housing index prices thourghout the dataset, it usually had 2x rate of growth than most of the provinces taken into consideration in out data. 

Another unexpected thing I noticed was that some places, including Kitchener-Waterloo, London in the province of Ontario, and Windsor, had max housing index values that were far higher than I had anticipated. Aside from that, every city in the data set with a greater value was a capital city. After doing some research, I was able to identify two factors that contributed to the high cost of living in these cities: the concentration of universities there (Waterloo area having 2 big universities at a walking distance) and the high rates of immigration from other countries. This fact also explained why Ontario's housing index value continues to rise and why it is regarded as one of the most expensive jurisdictions to live in. 

![max_city](/images/maxcity.png) 



##### Stephens's EDA findings:
My research question delved deeply into capital city data of the last year and my Exploratory data analysis focused primarily on that. When looking into the housing index data of capital cities over the entire time period *1980-2022*, there are 2 significant points in time:
    1. The first is that Victoria is the only capital city to have actually dropped in housing index cost since
    2. The second is that all of the capital cities index values converge around the time of 2017.

Looking specifically at the index results of the last year, the rankings from highest to lowest index value are:
    1. Winnipeg
    2. Quebec
    3. Victoria
    4. Halifax
    5. Ottawa
    6. Edmonton
    7. St. John's
    8. Regina

An interesting calculated data point for the last year was the maximum change in index (taking the highest and lowest possible values). Of that, the suprising lowest change in index was that of Ottawa. It changed less than a single point in value. Which means that for the last year the value of houses in Ottawa have had a near completely proportional change to the income and the cost of other essential goods in the city. The other significant city for the maximum change in index was Winnipeg, ranking the highest for change with a significant 12 point change for the maximum and minimum of the year which is reflected in the graph of index values in the last year. 

The second data set explored was the qualitative non-response rates of capital cities. 
This one, while not as extensive revealed a few interesting things. While ranking 3rd lowest for housing index within the last year, Edmonton specifically had the highest non-response rates for dwelling conditions non-response, tenure non-response, monthly rent non-response, and mortgage payment non-response by a significant margin. The Winnipeg and Quebec both rank within the the top 2-4 for all of those categories as well. St John's consistently ranks low, correlating to it's position in the index chart, while Regina ranks around 4th lowest in those categories consistently. There seems to be a slight correlation betweent the qualitative non-response data and the Index ranking with a strong exception being Edmonton

#### Reasearch Question 1 (Jack) and results:
So for my reaserch question, I looked at the trends in value across canada to see if there is any sort of a pattern that could lead to any conclusions about the potential next few years.

While Analysing the Data, the most intersting parts were definetely the 2008 market crash, as well as the 2019 COVID Pandemic. Both of these events sparked a large increase in the prices of houses, and because COVID was rather recent, and the fact that we are approaching the tail end of the Pandemic, if there are enough parralels between the the 2 events, it could help in determining the near future.
![Alberta](/images/index_AB.png) ![Manitoba/Saskachewan](/images/index_MB_SK.png) ![Ontario](/images/index_ONT.png) ![Quebec](/images/index_QB.png) 
Looking at the behavior of the 2008 crisis, we can see a large increase in prices as expected. Alberta and Manitoba/Saskachewan were the most affected areas, while Ontario and Quebec were the least affected (EDA findings indicated why this may be). Following the large increase4 across the country, we saw a sort of plateau as the prices of houses increased at a slower rate than in years prior. This follows simply economic logic that a continuos large increase in prices is never sustainable, and thus the market flattened out. 

Comparing this to 2019, we see a very similar trend. A very large pike in prices, which was even larger than 2008, which was significantly noticable across te entire country. Every single province saw record high housing index value and the largest contributor to this is likely the COVID-19 Pandemic. While COVID has a massive effect in all secotrs, not just housing, The housing market was definetely affected. Now that we are (mostly) out of the high restrictions part of the pandemic, and life has begun to return to normal, there is a small sample size of Data that stops the sharp slope in all areas. Looking to 2008 and comparing to after recovery had started, we are beginning to see the same trends. 

This leads me to what my data-based conclusion to my reaserch question: I believe that the next few years, it will plateaus like it did in 2008. While working with Tableau, they also had a feature which predicts a short time in the future of Data, and looking at that, it seems to indicated data that supported my conclusion. While it is definetely not set in stone, provided that there are no more disasters in the economy, I feel confident in my conclusion.



#### Reasearch Question 1 (Aditya) and results:
My research question was:
>**Through a comparative analysis of the housing index across various provinces and the complete time periods in a given dataset, which provinces and months exhibited the highest cost of living?**

The main goal of this study was to compare the housing index values between different provinces and time periods in a specific dataset in order to pinpoint the regions and months with the highest cost of living. We discovered important trends and patterns in the values of the housing index through comparative analysis.

Our data showed that the housing index's value increased consistently throughout the year, peaking in January at its lowest value and gradually rising thereafter. Notably, the greatest housing index values ever reached in our dataset were reported in October and July.

Although October and July had the greatest values, we also looked at the average rate of change in value and the highest value these months may attain. Considering this evaluation, we can conclude that the last quarter of the year, i.e., October to December, is the period with the highest cost of living across the various provinces and time periods in our dataset.

![max_month](/images/max_month.png) 
![mean progression](/images/mean_prog.png) 

After comparing the housing index values across the several provinces in our dataset, we found that Manitoba and Quebec had the highest housing index prices ever recorded. Prince Edward Island and British Columbia, on the other hand, had a noticeably faster growth in the housing index value than other provinces when we compared the mean progression in values. This data suggests that the cost of living in these two provinces has significantly increased, moving them up the rankings of most expensive places to live.

![max_province](/images/max_province.png) 
![mean progression](/images/mean_province.png)

Prince Edward Island and British Columbia's quick rise in housing index prices can be linked to a number of variables, including rising home demand, a lack of housing supply, an expanding population, and a growing economy. These results imply that investors and decision-makers should take these provinces into consideration when making real estate investments. Overall, my analysis shows the large regional differences in the housing index values, highlighting the necessity for region-specific policies and methods to effectively manage the real estate market. To learn more about the underlying causes of these changes and their long-term effects on the housing market and the economy, more research can be done.



#### Reasearch Question 3 (Stephen) and results:
My research question was:
>**What is the best place to live in provincial capital cities based off of the housing index and quality of the housing market in the last year?**

Based off of the housing index alone, the results for the last year in capitals cities is very straightforward. The cheapest place relative to the housing index right now, is Regina Saskatchewan and the most expensive with a significant margin is Winnipeg Manitoba.
Based off of the quality non-responsee rates of the second data set, there were 4 significant data points chosen that related to quality and pricing of the houses:
    - Tenure non-response rate
    - Monthly rent non-response rate
    - Mortgage payments non-response rate
    - Dwelling conditions non-response rate
    
For these 4 data points considered, St Johns had the lowest non-response for Dwelling conditions and Tenure while Quebec City has the lowest monthly rent non-response rate and Ottawa had the lowest non-response for mortgage payments. Edmonton, in contrast, ranked the highest non-response rate in all 4 categories.

Connecting the two categories together we get the following:

    - Ottawa: #5 highest in index, 3.0 average non-response rate across the 4 categories

    - Winnipeg: #1 Highest index, 3.38 average non-response rate across the 4 categories

    - Regina: #8 Highest index, 3.35 average non-response rate across the 4 categories

    - Victoria: #3 Highest index, 3.03 average non-response rate across the 4 categories

    - St John's #7 Highest index, 2.78 average non-response rate across the 4 categories

    - Edmonton #6 Highest index, 4.45 average non-response rate across the 4 categories

    - Halifax: #4 Highest index, 3.00 average non-response rate across the 4 categories
    
    - Quebec: #2 Highest index, 3.50 average non-response rate across the 4 categories

By those marks and assuming that the lowest value is preffered for both metrics: If the value is placed more on the qualitative data then St John's Newfoundland ranking 2nd lowest in housing index cost and absolute lowest in qualitative non-response is the best place to live currently based off of data within the last year. If instead, the housing index is preferred then Regina Saskatchewan ranking lowest in housing index and 3rd in average non-response rate is preferred. Personally I am keeping my eye on Regina as I prefer having as much money above zero in my wallet as I can but St Johns does boast a considerable argument. 

## Conclusion:
The housing market is complex. Had time permitted, there is so much more info to be gleaned from the Datasets we used. There is a whole line of work for people analysing  the housing market as a whole. Our group took a look at some of the questions that us as students may find the most useful, and we all came to a solid conclusion, based on each of our research. In doing so, each of the group members gained valuable knowledge of the market as a whole, as well as gained knowledge on the skills and what it takes to present data from research. There were definitely points during the project that did not go how we expected them to, and factors that went better than expected, but all of it culminated in the members of our group becoming better and more adept with the practice of Data Science. 
