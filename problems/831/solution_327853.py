def lingua_p (p):
    """função que recebe uma palavra de entrada (p) e que deve mudá-la
    para a língua do p. Para isso, é procurado uma vogal e é adicionado
    a letra 'p' depois da vogal, mais a vogal de entrada. E deve retornar
    a nova palavra com as modificações informadas;
    str->str"""
    sequencia = range(len(p))
    p_nova = p
    for i in sequencia:
        if p[i] in 'AEIOUaeiouíú':
            p_nova = str.replace(p_nova,p[i],(p[i]+'p'+p[i]))
    return p_nova