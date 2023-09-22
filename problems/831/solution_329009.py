def lingua_p(palavra):
    """dada uma palavra, a função insere, após cada vogal da palavra, a letra p mais a
    a vogal original;
    str->str"""
    p_minuscula=str.lower(palavra)
    p_nova=''
    for letra in p_minuscula:
        if letra in 'aeiou':
            p_nova=p_nova+str(letra)+'p'+str(letra)
        else:
            p_nova=p_nova+letra
    return p_nova