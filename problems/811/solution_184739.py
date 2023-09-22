# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''a partir da entrada de uma lista contendo as medidas do colchao
    no 1 arg no tipo lista, sendo as medidas inseridas na ordem crescente
    no segundo arg deve ser colocada a altura da porta e no terceiro, sua
    largura
    todas as medidas devem ser em cm
    list , int , int -> bool'''

    menor = medidas[0]
    media = medidas[1]
    maior = medidas[2]

    if menor <= H and media <= L or media <= L and menor <= H:

        return True

    else:
        return False