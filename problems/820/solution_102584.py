def posLetra(frase,letra,n):
    """recebe uma frase, letra e um numero e retorna a posicao da string aquela ocorrencia da letra está
    str,str,int->int"""
    i = 0
    contador = 0
  
    while i < len(frase):
        if letra == frase[i]:
            contador+=1
        if contador == n:
            return i
        i+=1