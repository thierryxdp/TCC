def posLetra(frase, letra, numero):
    '''Retorna a posicao da letra em um string, dada uma frase, uma 
       letra e o numero que indica a ocorrencia da letra desejada;
       str,str,int=>int '''
    palavras = list(frase)
    contador = 0
    qtd = 0
    while len(palavras) > contador:
        if letra in palavras[contador]:
            qtd = qtd + 1
            if qtd == numero:
               return contador
        contador = contador + 1

    if qtd < numero:
          return -1
    else:
          return qtd