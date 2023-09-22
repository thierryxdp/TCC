def conta_frases(texto1):
    '''função que conte o número de frases que aparecem neste texto.
    entrada: string
    saída: inteiro'''
    var1= str.join('*',(str.split(texto1,'...')))
    var2= str.join('*',(str.split(var1,'... ')))
    var3= str.join('*',(str.split(var2,'.')))
    var4= str.join('*',(str.split(var3,'. ')))
    var5= str.join('*',(str.split(var4,'!')))
    var6= str.join('*',(str.split(var5,'?')))
    return str.count(var6,'*')