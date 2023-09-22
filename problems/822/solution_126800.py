def repetidos(lista):
    ''' função chamada repetidos que receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista é igual ao 
    elemento anterior.
    Exemplo: repetidos([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]) Resposta: 6
    list->int'''
    i=0
    qtd=0
    while i<len(lista):
        a=lista[i]
        i+=1
        if(i==len(lista)):
            return qtd
        if (a==lista[i]):
            qtd+=1