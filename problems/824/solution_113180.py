def uppCons(frase):
    '''
Função que recebe uma frase e retorna  a frase com todas as consoantes
em maiúscula e as demais permanecem iguais. 
str-->str
    '''
    cons=''
    i=0
    while i<len(frase):
        if frase[i]in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxzç':
            cons=cons+str.upper(frase[i])
        else:
            cons=cons+frase[i]
        i=i+1     
    return cons