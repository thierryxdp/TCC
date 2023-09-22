def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com todas as suas
    consoantes em maiúsculas; str-->str'''
    
    consoantes='bcdfghjklmnpqrstvwxyz'
    proximo=0
    
    while proximo<22:
        frase=str.replace(frase,consoantes[proximo],str.upper(consoantes[proximo]))
        proximo=proximo+1
		
    return frase