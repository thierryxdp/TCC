def hashtag(s):
    '''
    '''
    if len(s)//2:
    	return '#' + s[0:len(s)/2] + '#' + s[len(s)/2:] + '#'
    else:
        return '#' + s[0:(len(s)/2)-1] + '#' + s[(len(s)/2-1):] + '#'