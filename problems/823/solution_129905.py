def faltante(lista):
    proximo = 0
    while proximo<len(lista):
        completo = list(range(1,len(lista)+2))
        soma = sum(completo)
        return soma