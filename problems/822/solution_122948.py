def repetidos(lista):
    '''A funcao recebe uma lista de numeros, e retorna o numero de vezes
    que um elemento na lista é igual ao elemento anterior
    list -> int'''
    i = 0
    lista_nova = []
    while i<len(lista):
        if lista[i] == lista[i-1]:
            lista_nova.append(1)
        i = i + 1
    
    return len(lista_nova)
#Primeira coisa se fazer foi criar a função repetidos e por lista como parametro
# Defini minha lista nova como o []
#While fez minhas condições serem executadas
#Condições essas plotadas na forma de propiedades como o if 
#e a str append adiciona um item no final da lista
#Por fim retorno a minha nova lista com o len contando os caracteres