def hashtag (s):
    '''função que dada uma string, insere o caractere "#" no início, no meio
e no final delaa
    str - > str'''
    metade = int(len(s)/2)

    return "#" + str(s[:(metade)])+"#"+s[metade:]+"#"