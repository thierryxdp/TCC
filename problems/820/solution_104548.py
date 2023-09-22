def posLetra(string, indice, n):
   """funcao que recebe como uma string, uma letra, e um numero
   que indica a ocorrencia desejada da letra
   e retorna em que posicao da string aquela ocorrencia da letra esta;
   string,int,int-> int""" 
 posicao= string.find(indice)
    while posicao >= 0 and n > 1:
        posicao = string.find(indice, posicao+ 1)
        n= n -1
    return posicao