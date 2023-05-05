# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from itertools import starmap

#find_longest_match, get_opcodes, get_ratio

# set a random state for deterministic sampling
random_state = np.random.RandomState(1968)

#This aims to collect cases from the raw data randomly
#data = p.read_csv('./top_mentioned_cleaning.csv')

#def take_sample(df):
#    sample = df.sample(n=200, axis = 0, random_state=random_state)
#    sample.to_csv('./data/sample.csv')
#    return sample

#This aims to calculate the editing distance between strings
def get_string_similarity_features(str1, str2):

    matcher = SequenceMatcher(a=str1, b=str2, autojunk=True)

    return {'lev_dist': levenshtein_distance(str1, str2, matcher),
            'lcs_dist': lcs_distance(str1, str2, matcher),
            'ratio': matcher.ratio(),
            'len_longest_substr': matcher.find_longest_match(0, len(str1), 0, len(str2)).size
            }
            
def edit_distance(str1, str2, matcher=None, distance_type="levenshtein"):
    if matcher is None or matcher.a != str1 or matcher.b != str2:
    
        matcher = SequenceMatcher(a=str1, b=str2, autojunk=True)
        if matcher.a != str1 or matcher.b != str2:
            print(r"WARNING: strings don't match the matcher. str1:{str1}, matcher.a:{matcher.a}, str2:{str2}, matcher.b:{matcher.b}")

    opcodes = matcher.get_opcodes()

    distance = 0
    for op in opcodes:
        if op[0] == 'replace':
            if distance_type == "levenshtein":
                distance += max(op[2] - op[1], op[4] - op[3])
            if distance_type == "LCS":
                distance += op[2] - op[1]
                distance += op[4] - op[3]
        if op[0] == 'insert':
            distance += op[4] - op[3]
        if op[0] == 'delete':
            distance += op[2] - op[1]
        if op[0] == 'equal':
            pass

    return distance

def levenshtein_distance(str1, str2, matcher = None):
    return edit_distance(str1, str2, matcher = matcher, distance_type="levenshtein")

def lcs_distance(str1, str2, matcher = None):
    return edit_distance(str1, str2, matcher = matcher, distance_type="LCS")

#This intends to calculate the editing distances between fandom and subreddit columns

def main (table_date = None, lines = None):
    filter_data = pd.read_csv('top_mentioned_cleaning.csv')
    
    str_fan = filter_data['fandom']
    str_sub = filter_data['subreddit']
    
    str_fan = list(map( str, (str_fan ) ) )
    str_sub = list(map( str, (str_sub ) ) )
 
    str_features = starmap(get_string_similarity_features, zip(str_fan, str_sub))

    str_features = pd.DataFrame(str_features)
    filter_data = pd.concat([filter_data, str_features],axis='columns')
   
    filter_data.to_csv('subred_fandom_features.csv', mode = "w", index = False)

if __name__ == '__main__':
    main()
