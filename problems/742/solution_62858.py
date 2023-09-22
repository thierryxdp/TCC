# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    a função pega a string <s>
    transforma ela em uma lista
    agoro, como lista, podemos alterar o elemento [i]
    depois reconstruimos a lista em forma de string com <retorno>
    e retorna o <retorno>
    '''
    
    letras = list(s)
    letras[i] = x
    retorno = ""
    for j in range(len(letras)):
        retorno += letras[j]
    
    return retorno