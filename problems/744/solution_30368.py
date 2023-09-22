# Coloque um comentário dizendo o que a função f
# str-> str
def hashtag(s):
    '''funcao que insira '#' no inicio, meio e final dela '''
    s="#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    return (s)