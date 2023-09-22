#str,str,int->int
def posLetra(frase,letra,numero):
    "Função que recebe uma frase,uma letra e um numero que indica a ocorrencia desejada da letra."
    numeros=str.count(frase,letra)
    if numeros<numero:
        return -1
    else:
        x=str.replace(frase,letra,' ',numero-1)
        posicao=str.index(x,letra)
        return posicao