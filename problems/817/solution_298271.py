#Função que atraves da lista calcula a media das notas.
   def acima_da_media(lista):
    a = []
    n=sum(lista)/len(lista)
    for elemento in lista:
        if elemento >= n:
            a.append(elemento)
            a.sort()
    return a
#Retorna as notas que ficaram acima da média