def lingua_p(palavra):
    """Função que retorna uma palavra dada no retorno para a língua do p,
    lista-->lista"""
    p=''
    for x in palavra:
        if x in 'aeiouáàãâéèêóòõôú':
            p=p+x+'p'+x
        elif x in 'bcdfghjklmnpqrstvwxyz':
            p=p+x
    return str.lower(p)