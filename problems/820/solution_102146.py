def posLetra(string, letra, numero):
    ''' Função que - dada uma string, um numero e uma letra -, retorna a posição que essa letra está de acordo com sua ocorrência.
    str,str,int -> int'''
    
    i = 0
    indice = 0
    ocorrencia = 0
    lista = list(string)
    while i < len(lista):
        if lista[indice] == letra:
            ocorrencia += 1
            if ocorrencia == numero:
                return indice

        i += 1
        indice += 1

    return -1