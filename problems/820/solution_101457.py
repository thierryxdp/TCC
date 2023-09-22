def posLetra(frase,letra,numero):
    """Dada uma frase(string), uma letra e um número, a função irá checar
    se a ocorrência da letra na frase, coincide com o número(podendo também ser superior). 
    Caso sim, a função irá retornar qual a posição dessa última letra na frase.
    Caso a quantidade de ocorrência seja menor do que o número, a função irá retornar -1.
    Tipo da variável frase: string
    Tipo da variável letra: string
    Tipo da variável numero: int
    Tipo da saída: int"""
    contador = 0
    ocorrencia = 0
    lista = []
    while contador < len(frase):
        if frase[contador] == letra:
            ocorrencia = ocorrencia + 1
            list.append(lista, contador)
        contador = contador + 1
    if ocorrencia == numero:  
        return lista[-1]
    if ocorrencia > numero:
        return lista[numero-1]
    else:
        return -1