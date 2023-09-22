def posLetra(string,letra,numero):
    '''funcao que dada uma string retorna a posicao da string 
  , uma letra e um numero retorna a posicao da string aquela ocorrencia 
  da letra está
  str,int -> int'''
    contador = 0 
    indice = 0 
    ocorrencia = 0 
    lista = list(string)
    while contador <len(lista):
        if lista[indice]==letra:
            ocorrencia=ocorrencia+1
        	if ocorrencia == numero:
                return indice 
        contador= contador+1
        indice = indice+1
        return -1