def filtraMultiplos(Lista, Numero):
    Contador = 0
    ListaFinal = []  
    while Contador < len(Lista):  
    divisao = Lista[Contador]%Numero 
        if divisao == 0:
            list.append(ListaFinal, Lista[Contador])
            Contador = Contador + 1
        if divisao != 0: 
            Contador = Contador + 1
    return ListaFinal