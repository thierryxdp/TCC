def posLetra(string, letra, numero):
    '''Função que retorna a posição da string de ocorrência, str, str, int -> int'''
    x = 0
    lugar = str.find(string, letra)
    while lugar>0 or  numero>1:
        if letra != string:
            posicao = str.find(string, letra, lugar + 1) 
        x = x + 1
    return lugar