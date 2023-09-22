def posLetra(frase,letra,num):
    '''Função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra e retorna em que posição da string aquela ocorrência da letra está; str, str, int -> str'''
    i=0
    ocorrencia=''
    while i<len(frase):
        if letra in frase:
            ocorrencia=frase[i]
        i=i+1
    return ocorrencia