def posLetra(frase,letra,ocorrencia):
    """Retorna em qual posição da frase está a ocorrencia da letra.
       Caso exista menos ocorrências do que a pedida, a função retorna -1;
       str,str,int->int
       Parâmetros:
       frase: frase qualquer
       letra: letra a ser procurada na frase
       ocorrencia: ocorrencia da letra na frase
    """
    if ocorrencia<=str.count(frase,letra):
        i=0
        vezes=0
        while vezes<ocorrencia:
            posicao=str.index(frase,letra,i)
            vezes=vezes+1
            i=posicao+1
        return posicao
    else:
        return -1