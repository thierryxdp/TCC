def lingua_p (palavra):
    '''
        Função que converte uma palavra para a lingua do P, que insere um p antes das vogais da palavra original, alem de retornar a palavra toda minuscula.
        str->str
    '''
    npalavra=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            npalavra = npalavra +(palavra[i] + 'p' + palavra[i])
        else:
            npalavra = npalavra + palavra[i]
        
    return npalavra