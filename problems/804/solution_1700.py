def filtra_pares(n1,n2,n3,n4):
    #Queridos professor e monitor. Vejo que o metodo de como eu fiz esse exercício ainda está adiantado na sua matéria.
    #Aonde venho estudando por fora vem de vídeos de cursos gratuitos no youtube do canal " Curso em Vídeo ".
    #Aprecio um código inteligente e sem muitas repetiçoes textuais, porém me sinto limitado no que diz respeito a  matéria da semana
    #Meu intuido é apenas melhorar meus códigos e estudar para que isso aconteça
    lista_valores = [n1,n2,n3,n4]
    lista_pares = []

    for contador in range(0, len(lista_valores)):
        if(lista_valores[contador]%2 == 0):
            lista_pares.append(lista_valores[contador])

    return lista_pares