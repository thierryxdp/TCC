def inverte(frases):
    '''Função que retorna uma frase de maneira invertida sem letras maiusculas e sem pontuação'''
    'str --> str'
    novafrase  = str.replace(frases,"-"," ")
    novafraseA = str.split(novafrase," ")
    novafrase0 = novafraseA[::-1]
    novafrase1 = str(novafrase0)
    novafrase2 = str.replace(novafrase1,"[","")
    novafrase3 = str.replace(novafrase2,']','')
    novafrase4 = str.replace(novafrase3,"'",'')
    novafrase5 = str.replace(novafrase4,'.','')
    novafrase6 = str.replace(novafrase5,',','')
    novafrase7 = str.replace(novafrase6,'!','')
    novafrase8 = str.replace(novafrase7,'-',' ')
    novafrase9 = str.replace(novafrase8,'?','')
    
    novafrase10 = str.lower(novafrase9)
    
    
   
   
    return novafrase10