def lingua_p(string):
    '''funcao que dada uma palavra, retorna a palavra traduzida para a lingua do P, que é quando apos cada vogal da
       palavra original eh inserida a sequencia de letras 'p' mais a vogal original
       string -> string'''
    traducao = ''
    for i in range(len(string)):
        if string[i] in 'bcdfghjklmnpqrstvxwyz':
            traducao = traducao + string[i]
        else:
            traducao = traducao + string[i] + 'p' + string[i]
    return str.lower(traducao)