def filtraMultiplos(Lista, Numero):
    Contador = 0
    ListaFinal = []
    divisao = (Lista[Contador])%(Numero)    
    while 0 < len(Lista):        
        if divisao == 0:
            list.append(ListaFinal, Lista[Contador])
            Contador = Contador + 1
        else: 
            Contador = Contador + 1
    return divisao