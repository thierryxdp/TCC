def uppCons(frase):
    qtd_consoantes=0
    i=0
    while i<len(frase):
        if frase[i]in 'BCDFGHJKLMNPQRSTWXYZbcdfghjklmnpqrstwxz':
          qtd_consoantes=qtd_consoantes+1
           i=i+1
    str.upper(qtd_consoantes)       
    return qtd_consoantes