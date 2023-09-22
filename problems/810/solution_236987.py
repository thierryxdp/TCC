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
    frase2 = frase1.split()  #divide a frase e seapra em uma lista
    frase3 = frase2[::-1]    #faz a lista ser invertida
    lista_separados = ['.',',',':','"','?','!',';','-']
    for i, j in enumerate(frase3):
        frase3[i] = j[0].replace(',','').replace('!','').replace('.','')
    frase4 = ' '.join(frase3)
    return frase4