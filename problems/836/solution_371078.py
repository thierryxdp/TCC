def busca (setor,matriz):
    ''' str, list -> list '''
    contatosBuscados= []
    contador= 0
    while str.lower(setor) in str.lower (matriz[contador][2]):
        list.append (contatosBuscados,matriz[contador])
    contador+=1

    return contatosBuscados