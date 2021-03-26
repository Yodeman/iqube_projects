# End Sars Project

This project is about classifying tweets pertaining to **#ENDSARS** movement.

### Data collection

The twint python package was used to scrape tweets from twitter. It is a nice package that doesn't require a twitter api and the web driver packages in order to scrape tweets from twitter. Over 10,000 tweets were scraped.

### Data exploration

From the [notebook](https://github.com/Yodeman/iqube_projects/tree/main/endsars/endsars.ipynb), it can be seen from the generated word cloud for the **hashtags** that a lot of the movement was about ending the Nigeria Special-Anti Robbery squad, people were demanding justice for the lives lot at Lekki toll gate and many more. It can as well be seen that a lot of organizations were tagged to help the movement.

### Sentiment Analysis

Since the data were unlabeled, I used the python natural language processing toolkit(NLTK) VADER sentiment analyzer to classify the tweets into positive and negative sentiments. The VADER sentiment analyzer returns  variable **compound** which ranges from -1 to 1 and the more the sentiment is closer to 1 the more positive it is and vice versa. For this project I classified tweets with compound greater than zero to be positive and tweets with compound less than zero to be negative.

### Conclusion

From the classified sentiments, it can be seen that there are more negative sentiments than positive which means that people really expressed how bitter they were about the actions of SARS, and the positive sentiments arises from tweets where people were praised for the actions taken and also from consolations.