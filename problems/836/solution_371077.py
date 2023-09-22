def busca (setor,matriz):
    ''' str, list -> list '''
    contatosBuscados= []
    contador= 0
    while str.lower(setor) in str.lower (contatos[contador][2]):
        list.append (contatosBuscados,contatos[contador])
    contador+=1

    return contatosBuscados