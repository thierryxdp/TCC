def pos(frase,letra,n_ocorrencia):
    '''função que retorna qual posição da string a ocorrencia da letra esta. caso nao tenha numero suficiente
de ocorrencias retornará -1. str,str,int-->int'''
    numero_letras=0
    contador=0
    while contador<len(frase):
        if frase[contador]==letra:
            numero_letras= numero_letras+1
        elif numero_letras==num:
            return contador-1
        contador = contador+1
    return -1