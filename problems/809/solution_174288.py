# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Pega 2 lista e gera uma terceira lista intercalando os numeros da lista"""
    lista=[]
    for i in range(3):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return(lista)