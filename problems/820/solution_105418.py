def posLetra(frase,letra,n):
    "função que recebe uma string, uma letra e um número n e retorna"
    "posição n da ocorrência da letra ou -1 se a quantidade for menor"
    "que o n"
    resultado=frase.find(letra)
    while resultado>=0 and n>1:
        resultado=frase.find(letra,resultado+1)
        n-=1
    return resultado