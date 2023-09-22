def uppCons(frase):
    '''Função que recebe uma frase e a retorna com todas as suas consoantes em maiúsculo; str->str'''
    contador=0
    while contador<len(frase):
        if frase[contador] not in [A,E,I,O,U,a,e,i,o,u]:
            return str.replace(frase,frase[contador],str.upper(frase[contador]),str.index(frase,frase[contador],contador,len(frase)))
        contador = contador + 1
    return frase