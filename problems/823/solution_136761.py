def faltante(lista):
    if (lista[-1]) < len(lista)+1:

        return lista[-1] + 1
    else:
    

        soma_pa = (len(lista)+1)*((lista[0]+lista[-1])) /2
    

        return int(soma_pa - sum(lista))