def lingua_p(frase):
    '''funcao que retorna a palavra traduzida para a lingua do P,ou seja,
    A cada vogal da frase original é inserida a letra P mais a vogal 
    list->str'''
    resultado=''
    for palavra in frase:
        if palavra in 'bcdfghjklmnpqrstvwxyz':
            minuscula=str.lower(palavra)
            resultado=resultado+minuscula
        if palavra not in 'bcdfghjklmnpqrstvwxyz':
            minuscula=str.lower(palavra)
            resultado=resultado+ x+str('p')+minuscula
    return resultado