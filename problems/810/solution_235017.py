def inverte(frase:str) -> str:
    """Modifica a frase dada para todas as letras em minusculo, sem pontuação
       e na ordem inversa
       
       Parameters:
       frase: frase a ser modificada
       
       Returns:
       frase modificada sem pontuação, em minusculo e invertida
       
       Passos:
       1 - retirar todas as pontuações
       2 - colocar tudo em minusculo
       3 - separar em uma lista as palavas da frase
       4 - inverter a lista
       5 - juntar a lista invertida em uma string separada por ' '
    """
    #pontuacao
    reticencias = str.replace(frase, '...', '{}')
    ponto = str.replace(reticencias, '.', '{}')
    exclamacao = str.replace(ponto, '!', '{}')
    interrogacao = str.replace(exclamacao, '?', '{}')
    travessao = str.replace(interrogacao, '-', '{}')
    virgula = str.replace(travessao, ',', '{}')
    doispontos = str.replace(virgula, ':', '{}')
    pontovirgula = str.replace(doispontos, ';', '{}')
    sempontos = str.replace(pontovirgula, '{}', ' ')
    
    #minusculo
    minusculo = str.lower(sempontos)
    
    #separacao e juncao
    lista = str.split(minusculo)
    listainvertida = lista[::-1]
    novafrase = str.join(' ',listainvertida)
    
    return novafrase