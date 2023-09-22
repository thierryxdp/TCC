# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string igual a s, exceto que o elemento da posiçao i deve ser substituído pelo caractere x"""
    """ str, str , int -> str """
    
    return str(s)[0:(i)] + str(x) + str(s)[(i):len(str(s))]