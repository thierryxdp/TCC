# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funçao que retorna a string da entrada com "#" no início, no meio e no fim, dado uma string s;str->str'''
    numDeTermos=len(s)
    metade=numDeTermos/2
    m=round(metade)
    return "#"+s[0:m]+"#"+s[m:]+"#"