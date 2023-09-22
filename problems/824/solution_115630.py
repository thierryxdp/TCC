def uppCons(frase):
    '''Função que recebe uma frase como entrada e retorna a frase com todas
    as consoantes em maiúsculas. Os demais caracteres são retornados exatamente
    como estavam na frase original; str->str'''
    vogais= 'AEIOUaeiou'
    i=0
    consoantes=[]
    while i<len(frase):
        if frase[i] not in vogais:
            frase= str.replace(frase,frase[i],str.upper(frase[i]))
        i+=1
    return frase