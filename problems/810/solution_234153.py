def inverte(frase):
    """essa funcao recebe uma frase e retorna essa mesma frase invertida
    string -> string
    """
    t_frase = str.replace(frase,'-',' ')
    v_frase = str.replace(t_frase,',',' ')
    d_frase = str.replace(v_frase,':',' ')
    pv_frase = str.replace(d_frase,';',' ')
    p_frase = str.replace(pv_frase,'.',' ')
    e_frase = str.replace(p_frase, '!',' ')
    i_frase = str.replace(e_frase,'?', ' ')
    frase_minuscula = str.lower(i_frase)
    frase_separada = str.split(frase_minuscula)
    frase_invertida = frase_separada[::-1]
    frase_nova = str.join(' ',frase_invertida)
    return frase_nova