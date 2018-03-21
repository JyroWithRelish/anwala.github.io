#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Original Code: https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter2/recommendations.py 
'''

from math import sqrt

def userSimilarity(people, JD, person, sumSquares):
    '''
    Returns a distance-based similarity score for JD and person.
    '''

    '''
    Value Conversion Key: 
    Example = (User ID, Age, Gender, Occupation, Zip Code)

    Gender: 
    0 = Female
    1 = Male

    Occupation: 
    0 = None
    1 = Student
    2 = Educator
    3 = Librarian
    4 = Writer 
    5 = Artist
    6 = Administrator 
    7 = Executive
    8 = Technician 
    9 = Engineer
    10 = Programmer
    11 = Scientist
    12 = Marketing
    13 = Salesman
    14 = Homemaker
    15 = Lawyer
    16 = Entertainment  
    17 = Healthcare
    18 = Doctor 
    19 = Retired 
    20 = Other
    '''
    
    # Add the sum of the squares for Age
    value1 = int(JD[0][1])
    value2 = int(person[1])
    sumSquares += (value1 - value2) * (value1 - value2)
    
    # Add the sum of the squares for Gender
    if (JD[0][2] == 'M'):
        value1 = 1
    else: 
        value1 = 0

    if (person[2] == 'M'):
        value2 = 1
    else:
        value2 = 0
        
    sumSquares += (value1 - value2) * (value1 - value2)
    
    # Add the sum of the squares for Occupation
    if (JD[0][3] == 'none'):
        value1 = 0
    if (JD[0][3] == 'student'):
        value1 = 1
    if (JD[0][3] == 'educator'):
        value1 = 2
    if (JD[0][3] == 'librarian'):
        value1 = 3
    if (JD[0][3] == 'writer'):
        value1 = 4
    if (JD[0][3] == 'artist'):
        value1 = 5
    if (JD[0][3] == 'administrator'):
        value1 = 6
    if (JD[0][3] == 'executive'):
        value1 = 7
    if (JD[0][3] == 'technician'):
        value1 = 8
    if (JD[0][3] == 'engineer'):
        value1 = 9
    if (JD[0][3] == 'programmer'):
        value1 = 10
    if (JD[0][3] == 'scientist'):
        value1 = 11
    if (JD[0][3] == 'marketing'):
        value1 = 12
    if (JD[0][3] == 'salesman'):
        value1 = 13
    if (JD[0][3] == 'homemaker'):
        value1 = 14
    if (JD[0][3] == 'laywer'):
        value1 = 15
    if (JD[0][3] == 'entertainment'):
        value1 = 16
    if (JD[0][3] == 'healthcare'):
        value1 = 17
    if (JD[0][3] == 'doctor'):
        value1 = 18
    if (JD[0][3] == 'retired'):
        value1 = 19
    else:
        value1 = 20
    
    if (person[3] == 'none'):
        value2 = 0
    if (person[3] == 'student'):
        value2 = 1
    if (person[3] == 'educator'):
        value2 = 2
    if (person[3] == 'librarian'):
        value2 = 3
    if (person[3] == 'writer'):
        value2 = 4
    if (person[3] == 'artist'):
        value2 = 5
    if (person[3] == 'administrator'):
        value2 = 6
    if (person[3] == 'executive'):
        value2 = 7
    if (person[3] == 'technician'):
        value2 = 8
    if (person[3] == 'engineer'):
        value2 = 9
    if (person[3] == 'programmer'):
        value2 = 10
    if (person[3] == 'scientist'):
        value2 = 11
    if (person[3] == 'marketing'):
        value2 = 12
    if (person[3] == 'salesman'):
        value2 = 13
    if (person[3] == 'homemaker'):
        value2 = 14
    if (person[3] == 'laywer'):
        value2 = 15
    if (person[3] == 'entertainment'):
        value2 = 16
    if (person[3] == 'healthcare'):
        value2 = 17
    if (person[3] == 'doctor'):
        value2 = 18
    if (person[3] == 'retired'):
        value2 = 19
    else:
        value2 = 20
    
    sumSquares += (value1 - value2) * (value1 - value2)
    
    return 1 / (1 + sqrt(sumSquares))


def userCorrelation(prefs, p1, p2):
    '''
    Returns the Pearson Correlation Coefficient for persons p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

def movieCorrelation(prefs, m1, m2):
    '''
    Returns the Pearson Correlation Coefficient for movies m1 and m2.
    '''
    
    # Get the list of mutually rated items
    si = {}
    for item in prefs[m1]:
        if item in prefs[m2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = sum([prefs[m1][it] for it in si])
    sum2 = sum([prefs[m2][it] for it in si])
    # Sums of the squares
    sum1Sq = sum([pow(prefs[m1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[m2][it], 2) for it in si])
    # Sum of the products
    pSum = sum([prefs[m1][it] * prefs[m2][it] for it in si])
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

def getNotSeenRatings(prefs, person, similarity=userCorrelation):
    '''
    Gets ratings for a user who has not seen the other movies 
    by using a weighted average of every other user's ratings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
    # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in totals.items()]
    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings


def flipPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result

def loadPeople(path='C:\\Users\\James Pindell\\Desktop\\CS 432\\Assignment 6\\ml-100k'):
    people = [tuple(line.split('|')) for line in open(path + '\\u.user')]
    return people  

def loadPreferences(path='C:\\Users\\James Pindell\\Desktop\\CS 432\\Assignment 6\\ml-100k'):
    # Get movie titles
    movies = {}
    for line in open(path + '\\u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
    # Load movie data
    prefs = {}
    for line in open(path + '\\u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

def loadMovies(path='C:\\Users\\James Pindell\\Desktop\\CS 432\\Assignment 6\\ml-100k'):
    # Get movie titles
    movies = {}
    for line in open(path + '\\u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = id
    # Load movie data
    prefs = {}
    for line in open(path + '\\u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

'''
Problem 1
'''

# Defines people for User Distance-Based Similarity Scores
people = loadPeople(path='C:\\Users\\James Pindell\\Desktop\\CS 432\\Assignment 6\\ml-100k')

# This is my demographic info
JD = [(0, 22, 'M', 'student', '22405\n')]

# Displays the User Distance-Based Similarity Scores
sumSquares = 0
for i in range(0,943):
    person = people[i]
    print('Similarity for User ' + people[i][0] + ': ' + str(userSimilarity(people, JD, person, sumSquares)))

print(' ')

'''
Problem 2
'''

# Defines prefs for User Pearson Correlation Coefficients
prefs = loadPreferences(path='C:\\Users\\James Pindell\\Desktop\\CS 432\\Assignment 6\\ml-100k')

# User 245 is the 'substitute me'
p1 = '245' 

# Displays the User Pearson Correlation Coefficients 
for i in range(1,944):
    p2 = str(i)
    print('Correlation for User ' + p2 + ': ' + str(userCorrelation(prefs, p1, p2)))

print(' ')

'''
Problem 3
'''
# User 245 is the 'substitute me'
person = '245'

# Displays the ratings for all the movies that the 'substitute me' has not seen 
ratings = getNotSeenRatings(prefs, person, similarity=userCorrelation)
print('Ratings For Movies That Have Not Been Seen: ')
for i in range(0, 1493):
    print(str(ratings[i]))

print(' ')

'''
Problem 4
'''

# Defines itemPrefs for Movie Pearson Correlation Coefficients
prefs = loadMovies(path='C:\\Users\\James Pindell\\Desktop\\CS 432\\Assignment 6\\ml-100k')
itemPrefs = flipPrefs(prefs)

# Movie 1 is my favorite movie
m1 = '1'

#  Displays the Movie Pearson Correlation Coefficients for my favorite movie
for i in range(1, 1683):
    m2 = str(i)
    print('Correlation for Movie ' + m2 + ': ' + str(movieCorrelation(itemPrefs, m1, m2)))

print(' ') 

# Movie 219 is my least favorite movie
m1 = '219'

#  Displays the Movie Pearson Correlation Coefficients for my least favorite movie
for i in range(1, 1683):
    m2 = str(i)
    print('Correlation for Movie ' + m2 + ': ' + str(movieCorrelation(itemPrefs, m1, m2)))
