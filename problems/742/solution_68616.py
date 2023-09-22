def substitui(s,	#Texto
              x,	#Caractere
              i		#Comprimento
             ):
    ''' Essa função concatena uma string substituindo uma letra
    dado o texto string, posição do caracter e a letra a ser substituida  '''
    
    s1 = s[:i]
    s2 = s[i+1:]
    return s1+x+s2