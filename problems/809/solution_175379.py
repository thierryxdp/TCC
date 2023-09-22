def intercala(lista1, lista2):
    """Esta função, dada duas listas(L1 e L2, de tamanho 3),
    gera uma lista L3 que é a formada intercalando elementos
    de L1 e L2.
    list,list -> list"""
    
    lista3 = lista1+lista2
    
    num1=(lista3[0])
    num2=(lista3[1])
    num3=(lista3[2])
    num4=(lista3[3])
    num5=(lista3[4])
    num6=(lista3[5])
    
    lista_base=[1,2,3,4,5,6]
    
    lista_base[0]=num1
    lista_base[1]=num4
    lista_base[2]=num2
    lista_base[3]=num5
    lista_base[4]=num3
    lista_base[5]=num6
    
    return lista_base