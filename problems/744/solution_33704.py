def hashtag(s):
    '''
    função que recebe uma string e insere o caractere '#' no início, no meio e no final dela
    str -> str
    '''
    import math
    a = len(s)
    b = math.floor(a/2)
	if len(s)%2 == 0:
        return '#' + s[:b] + '#' + s[b:a] + '#'
    else:
        return '#' + s[:b] + '#' + s[b:a] + '#'