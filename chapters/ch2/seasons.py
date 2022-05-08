""" Challenge 2
Write a program, with Scenarios and Tests, that does the following:
1. Ask the user to enter a Season
2. Using this input, create the logic to handle different seasons:
    * If the input is "winter", print "snow"
    * If the input is "spring", print "flowers"
    * If the input is "summer", print "beach"
    * If the input is "fall" or "autumn", print "leaves"
    * If the input is anything else, print "I don't know that season"
"""

def seasons():
    season = input('Enter a season: ').lower()
    print(get_season(season))


def get_season(s):
    dict_seasons = {'winter': 'snow', 'spring': 'flowers', 'summer': 'beach', 'autumn': 'leaves'}
    if s not in dict_seasons.keys():
        return "I don't know that season"
    else:
        return dict_seasons[s]

if __name__ == '__main__':
    seasons()