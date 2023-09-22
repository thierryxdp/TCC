# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funçao que retorna a string inserida com caractere # 
    no inicio, no meio e no final dela; str->str"""
    a=int(len(str(s))/2)
    return str('#')+ str(s[0:a]) +str('#')+ str(s[a:])+str('#')