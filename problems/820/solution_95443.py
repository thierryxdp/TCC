def posLetra(frase,letra,ocorrencia):
"""Ao fornecer uma string, uma letra e um número de ocorrência,
retorna o índice dessa ocorrência. Caso a ocorrência fornecida seja
maior que a oferta de letras correspondentes na string, retorna -1.

str,str,int -> int"""

    indice = 0
    contador = 0

    while indice < len(frase):
                
        if contador == ocorrencia:
            return indice-1       
                
        if frase[indice] == letra:       
            contador += 1

        if contador < ocorrencia:
            return -1
            
        indice = indice + 1