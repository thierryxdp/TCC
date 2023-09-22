def hashtag(s):
    '''
	função recebe uma str e insere o caractere '#'no início, meio e final dela;
    str -> str
    '''
    return '#' + (s[:(len(s)//2)]) + '#' + (s[(len(s)//2)]:) + '#''