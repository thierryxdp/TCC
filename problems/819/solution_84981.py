def filtraMultiplos (lista, numero):
    """Retorna os elementos da lista que são divisíveis pelo número fornecido na entrada; lista, float-> lista"""
    resposta = []
    x=0
    while x<len(lista):
        if lista[x]% numero == 0:
            resposta = resposta + lista[x]
            x = x+1
    return resposta