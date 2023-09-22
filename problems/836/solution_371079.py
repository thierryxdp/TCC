def busca (setor,matriz):
    ''' str, list -> list '''
    funcionario= []
    contador= 0
    while setor in matriz[contador][2]:
        list.append (funcionario,matriz[contador])
    contador+=1
    
    contatosBuscados= [funionario[0] + funcionario[1] + funcionario [3]]

    return contatosBuscados