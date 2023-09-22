# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    o = int(len(s)/2)
    "Pega a string antes da metade"
    primeira_parte = s[:o]
    "Pega a string depois da metade (o), excluindo o caracter na posição"
    ultima_parte = s[o:]
    "# + primeira parte + # + a ultima parte + #"
    hasta = "#"+primeira_parte + "#" + ultima_parte + "#"
    return hasta