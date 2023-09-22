def  busca(setor,matriz):
    '''recebe um setor e uma matriz e retorna
    as informaçoes dos funcionarios que trabalham
    naquele setor'''
    lista=[]
    contador=0
    for i in matriz:
        if i[2]==setor:
            del(i[2])
            lista.append(i)
            contador+=1
    return lista