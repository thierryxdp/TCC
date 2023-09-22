def uppCons(frase):
    ''' Código que recebe uma frase e a retorna com as consoantes
    maiúsculas
    :frase ---> str:
    :return --> str:
    '''
    maiuscula= str.upper(frase[1])
    i=0
    while 1>len(frase):
        if frase[i] in 'qwrtyipsdfghjklçzxcvbnm':
            upper= str.upper('qwrtyipsdfghjklçzxcvbnm')
            maiuscula= ''
            
            
        
        i=i+1
        return  maiuscula= frase[i]