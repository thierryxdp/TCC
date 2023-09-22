# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Funcao insere uma # no inicio, no meio e no final da string: s """
    inicio = s[0:len(s)//2]
    final = s[len(s)//2:]
    
    return "#"+inicio+"#"+final+"#"