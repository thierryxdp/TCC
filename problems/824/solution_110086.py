#Entrada: Uma frase 
#Precisamos analisar cada letra da frase
#Ao encontrar as consoantes, passamos para maiúsculo
def uppCons(frase:str)->str:
    """Recebe uma frase e retorna a mesma
    com todas as consoantes em maiúsculo"""
	listaFrase=list(frase)
    tamanho=len(listaFrase) 
    lista=[]
    i=0
    while i < tamanho:
        if str.lower(listaFrase[i]) in "bcdfghjklmnpqrstvxywzç":
            lista.append(str.upper(listaFrase[i]))         
        else:
            lista.append(listaFrase[i])
        i+=1
    return str.join("",lista)