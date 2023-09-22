# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna a string s com uma # inserida em seu comeco, uma em 
       seu meio e uma em seu final"""
    return "#" + s[0:len(s)//2] + "#" + s[len(s)//2:] + "#"