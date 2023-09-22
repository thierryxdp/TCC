def quant_palavras(frase):
    """Dada uma frase, a função calcula e retorna a quantidade
    de palavras dessa frase.
    Parametro de entrada: str
    Retorna: int"""
    
    listaAuxiliar= frase.split(' ')
    tamanhoFrase= len(listaAuxiliar)

    if listaAuxiliar[0]=='':
        tamanhoFrase= tamanhoFrase - 1
    if listaAuxiliar[len(listaAuxiliar)-1]== '':
        tamanhoFrase= tamanhoFrase - 1
    return tamanhoFrase