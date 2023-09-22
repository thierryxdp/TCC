def posLetra(string, letra, o):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada e retorna em que posição da string a ocorrência da letra está.
    Caso exista menos ocorrências da letra do que  a ocorrência pedida, a função retorna -1.
    Use str, str, int -> ("mariana come banana", 'a', 3) -> int"""
    #Em que indice está a o° letra ?
    indice = ocorrencia = 0
    #Estrutura de repetição.
    while indice < len(string):
        #Condicional para cada letra da frase com o parâmetro (letra) da função e somando + 1 se for true..
        if string[indice] == letra:
            ocorrencia+=1
            #Condicional para o contador de ocorrência com o parâmetro (o) da função e retornando o index da letra.
            if ocorrencia == o:
                return string.index(string[indice], indice)
        indice+=1
    else:
        return -1