def uppCons(frase):
    ''' Código que recebe uma frase e a retorna com as consoantes
    maiúsculas
    :frase ---> str:
    :return --> str:
    '''
    
    i=0
    upper= ''
    frase_maiusculo = ''
    while 1>len(frase):
        maiusculas = frase[i]
        if frase[i] in 'qwrtyipsdfghjklçzxcvbnm':
            upper= str.upper('qwrtyipsdfghjklçzxcvbnm')
            frase_maiusculo = frase + upper
                              
            i=i+1
        return