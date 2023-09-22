def inverte(frase):
    
    pon1 = str.replace(frase,'-',' ')
    pon2 = str.replace(pon1,',',' ')
    pon3 = str.replace(pon2,':',' ')
    pon4 = str.replace(pon3,';',' ')
    pon5 = str.replace(pon4,'.',' ')
    pon6 = str.replace(pon5,'?',' ')
    pon7 = str.replace(pon6,'!',' ')
    
    minuscula = str.lower(pon7)
    lista = str.split(minuscula)
    inversa = lista[::-1]