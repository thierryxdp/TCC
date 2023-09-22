# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que recebe uma string s e insere o caractere '#' no inicio, no meio 
    e no fim da string; str->str"""
    #=str(#)
    return #+str(s)[:len(s)//2]+#+str(s)[len(s)//2:]