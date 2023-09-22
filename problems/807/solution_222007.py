def conta_frases(periodo):
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
    valor1=str.count(periodo,'. ')
    valor2=str.count(periodo,'!')
    valor3=str.count(periodo,'?')
    valor4=str.count(periodo,'.')
    return ((valor1+valor2+valor3)+(valor4//3))