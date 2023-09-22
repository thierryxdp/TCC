def lingua_p (p):
    """função que recebe uma palavra de entrada (p) e que deve mudá-la
    para a língua do p. Para isso, é procurado uma vogal e é adicionado
    a letra 'p' depois da vogal, mais a vogal de entrada. E deve retornar
    a nova palavra com as modificações informadas;
    str->str"""
    sequencia = range(len(p))
    p_nova = p
    p_final = str.lower('')
    for i in sequencia:
        if not p[i] in 'AÁEÉIÍOÓUÚaáeéíoóuú':
            p_final = p_final+p[i]
        elif p[i] in 'AÁEÉIÍOÓUÚaáeéíoóuú':
            p_final = p_final+p[i]+'p'+p[i]
    return p_final