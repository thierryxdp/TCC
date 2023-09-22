def posLetra(string, letra, numero):
    """Função que retorna o a localização do elemento desejado na ocorrência desejada; str,str,int->int """
    i=0
    contador=0
    while i< len(string)-1:
        if string[i]==letra:
            contador+=1
        if contador==numero:
            return i
        i+=1
    return -1