def faltante(lista):
    'função que encontra um numero(int) faltando em uma lista de numeros que não repetem'
    contador=0
    soma=0
    tamanho=len(lista)
    soma_pa=((1+len(lista)+1)*(len(lista)+1)/2)
    while contador < tamanho:
        soma+=lista[contador]
        contador+=1
    return abs(int(soma_pa-soma))