def inverte (frase:str) -> str:
	'''Recebe uma frase e retorna uma string com a ordem das palavras ao contrario'''
    
 	#Preparação da frase
    fraseA = frase.lower()
    
    fraseA = fraseA.replace("..."," ")
    fraseA = fraseA.replace("."," ")
    fraseA = fraseA.replace("?"," ")
    fraseA = fraseA.replace("!"," ")
    fraseA = fraseA.replace(","," ")
    fraseA = fraseA.replace("-"," ")
    fraseA = fraseA.replace(":"," ")
    fraseA = fraseA.replace(";"," ")
    
    listaA = fraseA.split()
    listaA = listaA[::-1]
    
    fraseA = str.join(" ", listaA)
    
    return fraseA