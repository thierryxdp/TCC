def lingua_p (palavra):
    '''
        Função que converte uma palavra para a lingua do P, que insere um p antes das vogais da palavra original, alem de retornar a palavra toda minuscula.
        str->str
    '''
    npalavra=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            npalavra = palavra.replace(palavra[i],(palavra[i] + 'p' + palavra[i]))
    return str.lower(npalavra)