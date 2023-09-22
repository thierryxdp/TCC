#Start your python function here
def filtra_pares(tupla: tuple) ->tuple:
    """ Receber uma tupla com quatro elementos inteiros e retornar uma nova tupla contendo apenas os elementos pares, na ordem na tupla original"""   

#Cria uma lista para adicionar os elementos pares

    nova_tupla = []
    
#Percorre os numeros presentes dentro da tupla

    for numero in tupla:
        
#Condicao: se o resto do numero, na divisao por 2, é 0 esse numero é par 
        if numero % 2 == 0:
        
            nova_tupla.append(numero)
            
        nova_tupla.sort()
        
    return tuple(nova_tupla)