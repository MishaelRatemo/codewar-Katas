'''
Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4

'''
#BDD
#>>> able to count the number od points in a team

#pseudocode
#>>> initialize points (points)
#>>> loop through the games
#>> spilt the score at : >> split(':')
#>> if score is win points=3
#>> if score is draw points=1
#>> else points=0

from unittest import result


def points(games):
    countpoints=0
    for scorepoints in games:
        result = scorepoints.split(':')
        if result[0]> result[1]:
            countpoints+=3
        elif result[0]== result[1]:
            countpoints+=1
    
    return countpoints
print(points(['3:2','4:5','1:1','2:1']))