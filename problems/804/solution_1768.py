def filtra_pares(n1,n2,n3,n4):
    #Queridos professor e monitor. Vejo que o metodo de como eu fiz esse exercício ainda está adiantado na sua matéria.
    #Aonde venho estudando por fora vem de vídeos de cursos gratuitos no youtube do canal " Curso em Vídeo ".
    #Aprecio um código inteligente e sem muitas repetiçoes textuais, porém me sinto limitado no que diz respeito a  matéria da semana
    #Meu intuido é apenas melhorar meus códigos e estudar para que isso aconteça

    #inteiros

    int_n1 = int(n1)
    int_n2 = int(n2)
    int_n3 = int(n3)
    int_n4 = int(n4)

    #string

    str_n1 = str(n1)
    str_n2 = str(n2)
    str_n3 = str(n3)
    str_n4 = str(n4)

    lista_valores = [int_n1,int_n2,int_n3,int_n4]
    lista_pares = []

    for contador in range(0, len(lista_valores)):
        if(lista_valores[contador]%2 == 0):
            lista_pares.append(lista_valores[contador])

    if (len(lista_pares) == 0):
        return 'Sem Numeros Pares'

    if (len(lista_pares) == 1):
        n1 = lista_pares[0]
        return n1

    if (len(lista_pares) == 2):
        n1 = lista_pares[0]
        n2 = lista_pares[1]

        return n1,n2

    if (len(lista_pares) == 3):
        n1 = lista_pares[0]
        n2 = lista_pares[1]
        n3 = lista_pares[2]

        return n1,n2,n3

    if (len(lista_pares) == 4):
        n1 = lista_pares[0]
        n2 = lista_pares[1]
        n3 = lista_pares[2]
        n4 = lista_pares[3]
        return n1,n2,n3,n4