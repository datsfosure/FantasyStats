# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import bs4, requests
#
## Stage 1: Scraping HTML File
## Using example text file
#exampleFile = open('example.html')
#exampleSoup = bs4.BeautifulSoup(exampleFile)
#
#elems = exampleSoup.select('#author')
#elems[0].getText()


####
# Function to compute score
def computeScore(stats):
    for x in range(1, len(stats)-1):
        
        # TODO: Will need condition to handle TO (turnovers) or can make values negative to avoid condition
        
        # numpy.argsort() sorts index for sorted list in ascending order (low -> high)
        #  ie: [5, 3, 1 ,2, 4] -> [2, 3, 1, 4, 0]
        score = numpy.argsort(stats[x])
        print(score)
        
        # Last index of stats used to store running sum of score
        # Score from 1-10
        point = 1
        for y in score:
            stats[len(stats)-1][y] += point
            point += 1;
            
def printScore(name, score):
    print('Team Name\t\tScore')
    for x, y in zip(name, score):
        print(x,':\t',y)
    
# Stage 2: Analyzing Data
import numpy  # Need argsort to get indices in ascending order (list)

# Main list
SeasonStats = []

TeamName = ['Boss-town Dragons', 
            'bean town 4wds', 
            'Blake Gryffindor',
            'Team Krispy Cream',
            'ROY Simmons',
            'big apple nsa',
            'Team Flat Earth',
            'Team EnemaOfTheState',
            'MAYHEM UBUNTU',
            'TEAM DOMination']
#Categories
FGM = [5507, 5357, 5417, 5449, 5284, 5007, 5022, 4761, 3252, 3620]
FGP = [.4896, .4846, .4618, .4692, .4860, .4586, .4740, .4575, .4533, .4578]
TotalScore = [0] * len(FGM)

# Method 1
SeasonStats.append(TeamName)
SeasonStats.append(FGM)
SeasonStats.append(FGP)
# TODO: Additional categories

SeasonStats.append(TotalScore)

computeScore(SeasonStats)

# Updated total score (currently for first two categories)
printScore(TeamName, TotalScore)
    