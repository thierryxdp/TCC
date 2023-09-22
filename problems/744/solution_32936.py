def hashtag(s):
    '''A variável s receberá '#' anterior a primeira posição da string,anterior 
    a posição central e após a última posição '''
    '''str => str'''
    s = "#" + s[0:len(s)//2] + "#" + s[len(s)//2:] + "#"
	return s