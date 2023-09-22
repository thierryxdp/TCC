# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    # funcao que intercala duas listas de tamanho 3
    # em uma lista3, inicialmente vazia, e a retorna
    lista3 = [] 
    for i in range(3):
        # 
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        
    return lista3