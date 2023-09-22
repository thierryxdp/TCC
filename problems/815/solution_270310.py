#1.Incluir n na lista
#2.Organizar a lista
#3.Retronar a lista organizada

def insere(lista:list,n:int)->list:
    """funcao que inclui n na lista e ordena em ordem crescente"""
    
    lista.append(n)
    list.sort(lista)
    
    return lista