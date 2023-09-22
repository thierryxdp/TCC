def hashtag(s):
    '''Colocar palavra entre aspas e botar palavra entre aspas. str->str'''
    j = s[0:math.floor(len(s)/2]
    k = s[math.floor(len(s)/2):len(s)] 
    return '#'+j+'#"+k+'#"