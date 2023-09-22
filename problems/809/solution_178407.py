# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
    def intercala(lista1,lista2):
    """Ao fornecer duas listas, de tamanho três cad uma, tem-se como retorno uma terceira lista que intercala os valores de cada uma das listas fornecidas
parametro de entrada são list,list.
valor de retorno é list."""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]