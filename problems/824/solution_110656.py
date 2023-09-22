def uppCons(frase:str):
    '''funcao que recebe como parametro uma frase e retorna a frase com todas as
    suas consoantes em maiúsculas
    str->str'''
    posicao=0
    frase1=frase
    while posicao<len(frase):
    	if str.lower(frase1[posicao]) in "bcdfghjklmnpqrstvwxyz"
        	frase1=str.replace(frase1,frase1[posicao],str.upper(frase1[posicao]))
         posicao=posicao+1
 	return frase1