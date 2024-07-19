# Cricket_Sim
1.1 Aim
The aim of this project is to build a mathematical model that can accurately represent the game of cricket. We hope that the model is useful in investigating the different variables in cricket and the relationships between them. We hope that by understanding and predicting, we can mathematically experiment with different rules and formats of the game. This would provide a strong basis for building insights and evaluating new formats of the game. 
The motivation behind this project is the instant adoption of T20 and its success in attracting millions of new viewers. T10 is a truncated version of T20 and has become increasingly popular. It is still in its nascent stages and therefore is not widely known by fans of cricket. There is reason to believe that T10 is the future of cricket. We hope to evaluate this new format by providing a model that can simulate a T10 game. This will allow us to gain insights on the new format and will help us assess it’s viability.

1.2 Background
●	To make a predictive model for a 10-over cricket format, we first looked at data from other T10 leagues. We found five T10 leagues. However, the data from these leagues were too small to use.
○	Abu Dhabi T10: Comprises 6 teams. Has completed only 2 seasons.
○	Qatar T10 League: Comprises 6 teams and only completed one season in 2019
○	European Cricket League: Completed two seasons: one in 2019 with 8 teams and one in 2022 with 30 teams
○	The 6ixty: Scheduled to play this year with 6 men’s teams and 3 women’s teams
●	Due to the inadequate amount of data, we decided to collect data from the Indian Premier League. We found a kaggle dataset that had IPL per-match data from 2008-2020. However, we felt this data did not have everything that is required to make a good model. For example, the kaggle dataset did not have the statistics(runs, wickets, overs) of each team in a match, rather just the difference in scores and the winner.
●	Therefore, we decided to scrape the statistics of each of the teams playing a match from the IPL website. We scraped the data from all the years (2008-2022) and merged it with the kaggle dataset. We then cleaned the data and preprocessed it. 


More information present in report
