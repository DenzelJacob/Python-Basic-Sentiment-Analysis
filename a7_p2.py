import time


start_time = time.time()
words = {}
s = open("Python-Basic-Sentiment-Analysis\movie_reviews.txt", "r").read().split("\n")

for i in s:#line
    i = i.lower()
    temp_rating = int(i[0])
    temp_s = i.split(" ")
    for j in temp_s:#word

        if j in words:
            # edit the number of mentions
            words[j][0] += temp_rating
            words[j][1] += 1
        else:
            #new word, init j
            words[j]= [temp_rating,1]


end_time = time.time()
print("Initializing sentiment database\nSentiment database initialization complete\nTotal unique words analyzed:" ,len(words)-1, "\nAnalysis took",format(end_time-start_time,".2f"),"seconds to complete") 

ask = input("\nEnter a phrase to test: ")
phrase = ask.split(" ")
sum_phrase = 0
not_appear = 0
for i in phrase:
    #fix for zero times
    word = words.get(i,0)
    if word != 0:
        mentions = word[1]
        total_score = word[0]
        sum_phrase += total_score/mentions

    if word == 0:
        print("* '" + i + "' does not appear in any movie review")
        not_appear +=1
    else:
        print ("* '" + i + "' appears",str(mentions),"times with and average score of",str(total_score/mentions))

if sum_phrase !=0:
    phrase_avg = sum_phrase / ( len(phrase) - not_appear )
    print("Average score for this phrase is:", phrase_avg)

    if phrase_avg > 2:
        print("This is a POSITIVE phrase")
    elif phrase_avg < 2:
        print("This is a NEGATIVE phrase")
    else:
        print("This is a NEUTRAL phrase")


else:
    print("Not enough words to determine sentiment.")
