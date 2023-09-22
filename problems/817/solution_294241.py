def maiores(lista:list,n:int)->list:
    """ A funcao recebe uma lista de numeros inteiros, e um um numero inteiro.Ela retorna outra lista que contem todos os numeros da lista original, sendo eles maiores que n """
    list.append(lista,n)
    list.sort(lista)
    indice_n = list.index(lista,n)
   
    return  lista[indice_n+1:]