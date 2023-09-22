def posLetra(texto,letra,n):
    """Dado um texto qualquer, uma letra e um número n, retorna a posição n da ocorrência
    da letra indicada, caso não ocorra, retorna -1:
    str,str,int-->int"""
    letras=len(texto)
    texto=texto.replace(letra,' ',n-1)
    i=0
    return texto.find(letra)