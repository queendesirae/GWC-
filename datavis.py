




import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweetsdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)
# print(tb.subjectivity)
polar = []
subject = []
i = 0
while i < len(tweetData):
    tb = TextBlob(tweetData[i]["text"])
    polar.append(tb.polarity)
    subject.append(tb.subjectivity)
    i = i+1
print(polar)
print(subject)
# Fixing random state for reproducibility



# the histogram of the data
plt.hist(polar,[-1, -0.5, -0.5, 0.5, 0.5, 1], normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([-1, 160, 0, 1])
plt.grid(True)
plt.show()
