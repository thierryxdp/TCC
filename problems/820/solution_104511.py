def posletra(string, letra, numero):
    '''dada uma string, uma letra e um numero, retorne a posiçao da string aquela ocorrencia da letra
    :param string: str->str
    :param letra: str->str
    :param numero: int->int
    :return: int->int
    '''
    contador=0
    indice=0
    ocorrencia=0
    lista = lista(string)
        while contador <len(lista):
            if lista[indice] == letra:
                ocorrencia+=1
                if ocorrencia == numero:
                    return indice
                contador +=1
                indice +=1
                
            return -1