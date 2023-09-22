def qtd_divisores(numero):
    '''função que retorna a quantidade de divisores de um número
    valor de entrada: int
    valor de saída: int'''
    listadivisores=[]
    for divisores in numero:
        if numero%divisores == 0:
            listadivisores.append(divisores)
    return len(listadivisores)