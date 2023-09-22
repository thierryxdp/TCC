def conta_frases(frase):
    valor1=str.count(frase,'. ')
    valor2=str.count(frase,'!')
    valor3=str.count(frase,'?')
    valor4=str.count(frase,'.')
    valor5=str.count(frase,'...')
    A=valor2+valor3
    B=valor4-(valor5*3)
    if valor4>1:
        return valor1+A+1
    else:
        return valor1+valor4+A