def hashtag(s):
    '''recebe uma string e insere um "#" no inicio dela, no meio e no final. Como em:
    abcd --> #ab#cd#
    str --> str'''
    if len(s) % 2 == 0:
        metade = int(len(s)/2)
        return '#' + s[:metade] + '#' + s[metade:] + '#'
    else:
        metade = int(len(s)/2)
        metade2 = int(len(s)) - metade - 1
        return '#' + s[:metade] + '#' + s[metade2:] + '#'