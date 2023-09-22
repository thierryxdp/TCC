def hashtag(s):
    # str-> str
   a = len(s)//2 
    return '#'+ s[:a] + '#' + s[(a+1):]