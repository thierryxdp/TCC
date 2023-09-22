# Função que da a lista das notas acima da média
# lista_de_notas e n um inteiro qualquer 
#list,int->list
def maiores(lista_de_numeros,n):
    """Função que dada uma lista de entrada retorna uma outra lista que contém os números
    maiores do que a entrada n"""
    """lista_de_numeros e n(um número qualquer"""
    """list,int->list"""
    lista_de_numeros.append(n)
    lista_de_numeros.sort()
    return lista_de_numeros[lista_de_numeros.index(n)+1:]
def acima_da_media(lista_de_notas):
    """Função que retorna uma lista com as notas que foram acima da média"""
    """list->list"""
    media=sum(lista_de_notas)/len(lista_de_notas)
    return maiores(lista_de_notas,media)