def inverte(frase):
    '''função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
    entrada:string
    saída: string'''
    var1= str.join(' ',(str.split(frase,'...')))
    var2= str.join(' ',(str.split(var1,'.')))
    var3= str.join(' ',(str.split(var2,';')))
    var4= str.join(' ',(str.split(var3,':')))
    var5= str.join(' ',(str.split(var4,'?')))
    var6= str.join(' ',(str.split(var5,'-')))
    var7= str.join(' ',(str.split(var6,'!')))
    var8= str.join(' ',(str.split(var7,',')))
    var9= str.lower(var8)
    var10= str.split(var9,' ')
    var11= var10[-1:0:-1]
    var12= str.join(' ',var11)
    return var12