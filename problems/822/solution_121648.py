def repetidos(lista):
    '''Função que recebe como entrada uma lista de números de retorna o númerode vezes que um elemento da lista é igual ao anterior.
       parâmetro de entrada:list
       valor de retorno:int'''
    bloco=[]
    contador=0
    while contador < len(lista):
        anterior=contador-1
        if lista[contador]==lista[anterior]:
            bloco=bloco+[lista[contador]]
        contador=contador+1
    return (len(bloco))