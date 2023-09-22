#Entrada: Uma frase 
#Precisamos analisar cada letra da frase
#Ao encontrar as consoantes, passamos para maiúsculo
def uppCons(frase:str)->str:
	listaFrase=list(frase)
    tamanho=len(listaFrase) 
    lista=[]
    i=0
    while i < tamanho:
        if str.lower(listaFrase[i]) in "aeiou":
            lista.append(listaFrase[i])
        else:
            lista.append(str.upper(listaFrase[i]))
   	    i+=1
    return lista