def sub(txt):
    k=str.split(txt,'-')
    frase1=str.join(' ',k)
    frase2=str.split(frase1,'...')
    frase3=str.join('',frase2)
    frase4=str.split(frase3,',')
    frase5=str.join('',frase4)
    frase6=str.split(frase5,'.')
    frase7=str.join('',frase6)
    frase8=str.split(frase7,':')
    frase9=str.join('',frase8)
    frase10=str.split(frase9,'!')
    frase11=str.join('',frase10)
    frase12=str.split(frase11,'?')
    frase13=str.join('',frase12)
    frase14=str.split(frase13,';')
    fraseF=str.join('',frase14)
    return fraseF
def inverte(frase):
    normal=str.split(sub(frase),' ')
    invertida=normal[::-1]
    invtxt=str.join(' ',invertida)
    return invtxt