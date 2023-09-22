def hashtag(s):
    '''função que insere o caractere '#' no início, meio e final de uma string s
    str -> str'''
    s=str(s)
    metade=len(s)//2
    nova_string= ('#'+s[0:metade]+'#'+s[metade:]+'#')
    return nova_string