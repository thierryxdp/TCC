def intercala(lista1, lista2):
    '''Calcule e retorne uma função dadas duas listas de tamanho 3, retorna a concatanacao intercalando as lista1 e lista2, gerando a lista3
    O paramentro de entrada sao list , list.
    O valor de retorno e list.
    Casos de teste:
    lista1=[1,3,5]
    lista2=[2,4,6]
    lista3= lista1 + lista2'''
    
    
    return (lista1 + lista2) + [::2]