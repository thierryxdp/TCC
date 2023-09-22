# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Essa função recebe uma string e retorna uma # no meio 
    dela mesma, no inicio e no fim, str,str"""
    x = len(s)//2 
    s1 = s[:x]
    s2 = s[x:]
    return "#"+str(s1)+"#"+str(s2)+"#"