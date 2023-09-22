def acima_da_media(lista_notas):
 def maiores(lista,inteiro_n): 
    lista2= []

    for i in lista_notas:
      if i >inteiro_n:
        lista2.append(i)
    lista2.sort()
    media=sum(lista2)/len(lista2)
    x=len(lista2)
    y=list.index(lista2,media)
    return lista2[y+1:x]