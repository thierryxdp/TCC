def conta_frases(texto):
    '''Recebe uma string texto e calcula o se número de frases com 
    base nas pontuações do texto.
    Assinatura: string -> int'''
    lista = texto.split("! ")
    return lista