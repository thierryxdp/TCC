def inverte(frase):
    nova_frase = str.replace(frase,'-',' ')
    nova_frase1 = str.replace(nova_frase,',',' ')
    nova_frase2 = str.replace(nova_frase1,':',' ')
    nova_frase3 = str.replace(nova_frase2,';',' ')
    nova_frase4 = str.replace(nova_frase3,nova_frase[-1],' ')    
    nova_frase5 = str.lower(nova_frase4)
    nova_frase6 = list(reversed(str.split(nova_frase5)))
    nova_frase7 = str.join(" ",nova_frase6)
    return nova_frase7