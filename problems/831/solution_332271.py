def lingua_p(palavra):
    '''Função que retorna a palavra inserida na língua do p, dado a palavra;str->str'''
    minuscula=str.lower(palavra)
    traducao=''
    for a in minuscula:
        if a in 'aeiouáéíóúâêîôûãõ':
            traducao=traducao+a+'p'+a
        elif a not in 'aeiou':
            traducao=traducao+a
    return traducao