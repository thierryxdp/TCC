def posLetra(frase,letra,n):
    res = [i for i in range(len(frase)) if frase.startswith(letra, i)]
    if n>len(res):
        return-1
    else: 
        return res[n-1]
from collections import Counter
def repetidos(lista):
    contador = Counter(lista)

    repetidos = [
    item for item, quantidade in contador.items() 
            if quantidade > 1
    ]

    quantidade_repetidos = len(repetidos)
    return(repetidos)
def faltante(lista_inteiros):
    lista_inteiros.sort(reverse=True)
    max_int = lista_inteiros[0]
    nao_pertence = []
    for i in range(0,  max_int):
        print(max_int,i)
        if i not in lista_inteiros:
            nao_pertence.append(i)
    return nao_pertence[0]