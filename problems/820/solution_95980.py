def posLetra(str, letra, n):
    ''' funcao que dada uma string, letra e numero de ocrrencias retorna posição e ocorrencia da letra desejada'''
    conta = 0
    i = 0
    posic = 0
    while(i < len(str)):
        if(str[i] == letra and conta < n):
            conta += 1
            posic = str.find(str, letra, i)
            i += 1
        else:
            i += 1
    if(conta == n):
        return posicao
    else:
        return -1