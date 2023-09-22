def insere(lista,n):
    """essa função recebe como entrada uma lista de números crescentes e um número inteiro 
    e retorna a mesma lista, porém como esse número inserido na mesma
    de forma que ela continue crescente;
    list,int-->list"""
    lista = lista + [n]
    list.sort(lista)
    return lista