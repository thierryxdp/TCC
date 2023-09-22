def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com todas as suas
    consoantes em maiúsculas; str-->str'''
    
    consoantes='bcdfghjklmnpqrstvwxyz'
    proximo=0
    while proximo<len(frase):
        if frase[proximo] in consoantes:
            frase=str.replace(frase,frase[proximo],str.upper(frase[proximo]))
	    proximo=proximo+1
    return frase