def retira_pontuacao(frase):
    """Essa funcao retira a pontuacao de uma frase"""
    t_frase = str.replace(frase,'-',' ')
    v_frase = str.replace(t_frase,',',' ')
    d_frase = str.replace(v_frase,':',' ')
    pv_frase = str.replace(d_frase,';',' ')
    p_frase = str.replace(pv_frase,'.',' ')
    e_frase = str.replace(p_frase, '!',' ')
    return p_frase