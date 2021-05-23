#reveiw analyzer

#ask input -string
# open file
#read file
#search every review
# keep track of review stars
# if the reveiew has the input string in it add stars to average

def re_find(string,ask):
    string = string.lower()
    ask = ask.lower()
    found = 0
    
    string = string.split(" ")
    for i in string:
        
        if(i == ask):
           found +=1
    
    
    return found
        


    

mentioned = 0
unique_mentioned = 0
review_total = 0

s = open("Assignment#7\movie_reviews.txt","r").read().split("\n")


ask = input("Enter a word to test: ")

for i in s :
    temp = int(i[0])
    temp2 = re_find(i,ask)
    if temp2 != 0:
        mentioned += temp2
        unique_mentioned += 1
        review_total += temp


if unique_mentioned == 0:
    avg = 0
else:
    avg = review_total / unique_mentioned 




ask = "'"+ ask +"'"
print( ask + " appears " + str(mentioned) + " times")
if avg !=0:
    print("The average score for reviews containing the word" , ask , "is",avg)
else:
    print("There is no average score for reviews containing the word",ask)
    print("Cannot determine if this word is positive or negative")
    exit()



if avg < 2:
    print("This is a negative word")
elif avg > 2:
    print("This is a positive word")
else:
    print("This is a neutral word")

