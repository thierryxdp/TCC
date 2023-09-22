def uppCons(frase):
    """recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas e as vogais da mesma forma como estavam"""
    entrada = frase.split(' ')
    contador = 0
    
    while contador<len(entrada):
        if entrada[contador] in 'AEIOU' or entrada[contador] in 'aeiou':
        	contador +=1
        else:
        	entrada[contador]= str.upper(entrada[contador])
       		contador +=1
            
   	return entrada