def hashtag(s):
    '''Insere o caractere # no inicio, meio e final da string recebida;
    str-> str'''
    if len(s)%2 == 0:
        return '#' + s[:int((len(s)/2)+1)] + '#' + s[int(len(s)/2+1):] + '#'
    else:
        return '#' + s[:int((len(s)+1)/2)] + '#' + s[int((len(s)+1)/2):] + '#'