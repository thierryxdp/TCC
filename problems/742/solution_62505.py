# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s, x, i):
    i = len(s) if i > len(s) else i #Se i for maior que o tamanho da string, substituimos o último char.
    j = list(s) #Convertemos s em uma lista de chars.
    j[i] = x #Substituimos o iésimo char por x.
    k = ""; #Declarando uma string vazia.
    for l in j: #E transformamos a lista de volta em uma string.
        k += l
    return k #Retornamos a string final.