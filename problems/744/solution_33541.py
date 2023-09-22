def hashtag(s):
    '''Insere o caractere # no inicio, meio e final da string recebida;
    str-> str'''
    if len(s)%2 == 0:
        return '#' + s[:(len(s)/2)+1] + '#' + s[len(s)/2+1:] + '#'
    else:
        return '#' + s[:(len(s)+1)/2] + '#' + s[(len(s)+1)/2:] + '#'