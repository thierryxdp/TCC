def posLetra(str_recebida,letra_inserida,ocorrencia_desejada):
    """Recebe uma string, uma letra, e um número que indica a ocorrência desejada da letra(1 para a primeira,
    2 para segunda,etc.). A função retorna em que posição da string aquela ocorrência da letra está. A função
    retorna o valor -1 caso existam menos ocorrências da letra do que a ocorrência pedida
    (str,str,int --> int)""" """A função não funciona se for inserido um dado numérico diferente de int """
    aparicoes_da_letra = [] #cria-se o acumulador, a lista que conterá os números de posição da letra inserida
    i = 0 #define-se o contador
    while i < len(str_recebida): #repete-se os comandos da linha 9 a 11 enquanto i for menor que o comprimento de str_recebida, ou seja, o processo será repetido para todos as posições da str_recebida
        if str_recebida[i] == letra_inserida : #verifica-se se a posição i da str_recebida é uma ocorrência da letra_inserida
            aparicoes_da_letra = aparicoes_da_letra + [i] #caso a posição i seja uma ocorrência da letra_inserida, será adicionada ao acumulador o número da posição dessa ocorrência
        i = i+1 #aqui se aumenta o valor do contador para repetir o processo com a próxima posição da str_recebida
    if len(aparicoes_da_letra) < ocorrencia_desejada :  #aqui checa-se se o número de ocorrências é inferior ao valor da ocorrência desejada
        return -1  #caso existam menos ocorrências da letra do que a ocorrência pedida, a função retornará o valor -1
    else:
        return aparicoes_da_letra[ocorrencia_desejada-1] #caso contrário, será retornado em que posição da string aquela ocorrência da letra está