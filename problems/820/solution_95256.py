def posLetra(frase,letra,n):
    """ essa função ia retornar em qual posição estara a ocorrencia dada pelo valor n, na frase. caso n tenha ocorrencia, irá retornar por -1
entrada -> str,str,int
saida -> int """
    return str.find(frase,letra,n)