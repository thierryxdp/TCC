def filtraMultiplos(list_num,num):
    """Esta função recebe uma lista de números e um número inteiro e retorna os números da lista que são multiplos do número que foi fornecido
    list,int -> list"""
    multiplos = []
    for i in list_num:
        if i%num == 0:
            multiplos.append(i)
    return multiplos