def inverte(frase):
"""funcao que inverte uma determinada frase fornecida"""
    lista=frase.split()
    lista.reverse(input())
    return ' '.join(lista)