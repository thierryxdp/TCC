def posLetra(string,letra,ocorrencia):
    '''Essa função retorna em que posição da string aquela ocorrência da letra está;
    Recebe como entrada uma str, uma letra e um número.
    Retorna a posição que a ocrrencia da letra está.
    str,str,int->int'''
    letraanalisada = 1
    while not letraanalisada == ocorrencia:
        pos = str.find(string,letra)
        if pos == -1:
            return -1
        string = string[:pos:]+string[pos+1:]
        letraanalisada = letraanalisada + 1
    return str.find(string,letra) + letraanalisada - 1
#Essa função retorna em que posição da string aquela ocorrência da letra está, recebendo como entrada uma str, uma letra e um número