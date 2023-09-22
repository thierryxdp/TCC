def busca(setor,matriz):
    '''Recebe uma matriz como a do exemplo e busca a ficha de 
    funcionarios por setor e retorna os dados de todos os 
    funcionarios daquele setor;
    str, list -> list'''
    lista=[]
    for m in matriz:
        for n in m:
            if n == setor:
                m=x
                lista.append((list.remove(x,setor))