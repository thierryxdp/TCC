def fatorial(numero):
    'Dado um número, calcula e retorna o fatorial. Entrada: int. Saída: int.'
    pos=0
    resultados=1
    lista=list(range(1,numero+1))
    while pos<len(lista):
        resultado=lista[pos]*resultado
        pos=pos+1
    return resultado