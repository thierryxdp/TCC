def qtd_divisores(numero):
    tamanho= numero +1
    lista=[]
    for divisores in range(tamanho):
        if numero%divisores==0:
            lista= lista.append(divisores)
    return len(lista)