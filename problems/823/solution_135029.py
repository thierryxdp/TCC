def faltante(lista):
    list.sort(lista)
    indice=0
    if len(lista)==1:
        return 2
    
    while indice < len(lista):
        if len(lista)== frase[len(lista)-1):
           return
       
        
       if lista[indice] == indice +1:
           list.sort(lista)
       else:
           return lista[indice] -1
       indice=indice +1