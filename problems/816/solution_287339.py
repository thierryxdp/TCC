def maiorRecusrsao(lista, n, index):
    """Verifica todos os numeros de uma referecia de lista  se eles sao maiores que n
    atraves de recursao e o index tem de ser o tamanho da lista;
    lista<float>[???], float, int --> Void"""

    if index > 0:
        index -= 1
        
        if lista[index] < n:
            # Verifica se o numero e menor 
            
            list.remove(lista, lista[index])

        maiorRecusrsao(lista, n, index)

def maiores(lista_numero, n):
    """Recebe um referencia de um lista de numeros soma todos com o numero escolhido;
    list<float>[???], float --> Void"""

    maiorRecusrsao(lista_numero, n, len(lista_numero))
    list.sort(lista_numero)
    
    return lista_numero