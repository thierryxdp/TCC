def hashtag(s):
    """recebe uma string e insere o caractere # no inicio, meio e final dela    
str-> str"""
    y=len(s)//2
    palavrahashtag='#'+s[0:y]+'#'+s[y:]+'#'
    return palavrahashtag