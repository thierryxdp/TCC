def inverte(frase):
    '''
      funçao que dada 1 frase retorna a frase ao contrario
      
      Paramentro:
            Entradas:
                frase: str
                    valor da frase fornecida
           	Retorna:
                Uma nova frase que e a frase original invertida
     '''
	frase1 = frase.lower()   #Transforma a frase em letras minusculas
    frase2 = frase1.replace('!','').replace('.','').replace(',','').replace(';','').replace(':','').replace('?','').replace('-',' ')
    frase3 = frase2.split()  #divide a frase e seapra em uma lista
   	frase4 = frase3[::-1]    #faz a lista ser invertida
    frase5 = ' '.join(frase4)
    return frase5