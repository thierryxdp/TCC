def pontos_por_time(x):
    lista1,lista2=x
    pontoscormengo=0
    pontosflamrinthians=0
    if (lista1[2])[0]>(lista1[2])[1]:
        pontoscormengo=pontoscormengo+3
    if(lista1[2])[0]<(lista1[2])[1]:
        pontosflamrinthians=pontosflamrinthians+3
    if(lista1[2])[0]==(lista1[2])[1]:
        pontosflamrinthians=pontosflamrinthians+1
        pontoscormengo=pontoscormengo+1
    if(lista2[2])[0]>(lista2[2])[1]:
        pontosflamrinthians=pontosflamrinthians+3
    if(lista2[2])[0]<(lista2[2])[1]:
        pontoscormengo=pontoscormengo+3
    if(lista2[2])[0]==(lista2[2])[1]:
        pontoscormengo=pontoscormengo+1
        pontosflamrinthians=pontosflamrinthians+1
        return {lista1[0]:pontoscormengo,lista2[0]:pontosflamrinthians}