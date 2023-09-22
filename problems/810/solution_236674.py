def inverte(frase):
    frase_filter1 = str.replace(frase,'-',' ')
    frase_filter2 = str.replace(frase_filter1,',',' ')
    frase_filter3 = str.replace(frase_filter2,'...','.')
    frase_filter4 = str.replace(frase_filter3,'.',' ')
    frase_filter5 = str.replace(frase_filter4,'!',' ')
    frase_filter6 = str.replace(frase_filter5,'?',' ')
    frase_filter7 = str.replace(frase_filter6,';',' ')
    frase_filter8 = str.replace(frase_filter7,':',' ')
    frase_minusculo = str.lower(frase_filter8)
    lista_frase = str.split(frase_minusculo)
    lista_frase_inversa = lista_frase[::-1]
    frase_inversa_pronta = str.join(' ',lista_frase_inversa)
    
    return frase_inversa_pronta