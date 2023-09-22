def eh_quadrada(M):
    """dada uma matriz, função identifica se ela é quadrada. Se for quadrada,
       função retorna True, se não, False. list->bool"""
    for i in range(len(M)):
        for j  in range(len(M[0])):
            if M[i][j] != M[j][i]:
                return False
    return True