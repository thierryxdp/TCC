def uppCons(frase: str)-> str:
    """ Função que receba como entrada uma frase e retorne a frase com todas as suas consoantes
    em maiuscukas(e os demais caracteres exatamente da forma como estavam na frase original)"""
    frase_modificada=list()
    i=0
    
    while(i<len(frase)):
        if(str.lower(frase[i]) in "bcdfghjklmnpqrstvxwyz"
           list.append(frase_modificada, str.upper(frase[i]))
        else:
           list.append(frase_modificada, frase[i])
        i +=1
     
     return str.join("", frase_modificada)