def inverte(frase):
    f1=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'?',' '),'.',' '),'-',' '),',',' '),';',' '),':',' ')
    f2=str.lower(f1)
    f3=str.split(f2)
    f4=f3[::-1]
    f5=str.join(', ',f4)