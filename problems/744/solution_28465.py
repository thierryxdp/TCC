# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que retorna uma '#' no inicio, meio e no fim da string s
    Parametro:
    s :str
    Saida:
    str'''
    i=int(len(s)/2)
    return #+s[0:i]+#+s[i:]+#