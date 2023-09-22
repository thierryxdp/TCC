def posLetra(s,l,n):
    '''Recebe uma string s e retorna em que posição o caractere l aparece pela n-ésima vez; str->int '''
    posicao=-1
    ocorrencia=0
    if str.count(s,l)>=n:
        while posicao<len(s)-1 and ocorrencia<n:
            posicao=posicao+1
            if s[posicao]==l:
                ocorrencia=ocorrencia+1
    return posicao