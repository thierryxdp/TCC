def repetidos(list_num):
    '''funçao que recebe como entrada um lista de numeros, e retorna
o numero de vezes que um elemnto da lista é igual ao elemnto anterior.
list -> int'''
    contador=0
    repetidos=0
    quant=len(list_num)
    while contador< quant:
        if list_num[contador]==list_num[contador-1] and contador>0:
            repetidos+=1
        contador+=1
    return repetidos