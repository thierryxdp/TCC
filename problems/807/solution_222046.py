def conta_frases(frase):
        ''' função que recebe uma string "periodo" de entrada, e retorna 
    número de frases contidas nessa string'''
    '''str -> int'''
    #Casos de teste:
    '''conta_frases('Meu deus! tenho que estudar pra prova...')
    -> 2
       conta_frases('python! é uma ótima linguagem. muito desafiadora!')
    -> 3
       conta_frases('Eu sou! claramente um ótimo. Programador?')
    -> 3 '''
    valor1=str.count(frase,'. ')
    valor2=str.count(frase,'!')
    valor3=str.count(frase,'?')
    valor4=str.count(frase,'.')
    valor5=str.count(frase,'...')
    A=valor2+valor3
    B=valor4-(valor5*3)
    if valor4>1:
        return valor1+A+1
    if valor1==1:
        return valor1+valor4+A-1
    else:
        return valor1+valor4+A