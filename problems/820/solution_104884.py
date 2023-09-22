def posLetra(frase,x,i):
    """funcao que dada uma string frase, uma letra x e um numero i
que indica a ocorrencia desejada da letra, retorna em que posicao
da string aquela ocorrencia da letra esta. Em caso de ter menos
ocorrencias da letra do que a ocorrencia perdida, a funcao retorna
o valor de -1
str,str,int->int"""
    posicao = frase.find(x)
    while posicao >= 0 and i > 1:
        posicao = frase.find(x,posicao + 1)
        i = i - 1
    return posicao