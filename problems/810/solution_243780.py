def inverte (frase):
    '''dada uma frase, retorna a frase na ordem inversa, sem letras maiusculas e sem pontuacao
       : str -> str
    '''
    f_pon = retira_pontuacao(frase)
    f_min = f_pon.lower()
    f_sep = f_min.split()
    f_rev = f_sep[::-1]
    f_nova = str.join(' ',f_rev)
    return f_nova