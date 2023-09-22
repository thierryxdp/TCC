def acima_da_media(*notas):
    """Essa função retorna uma lista com as notas que ficaram acima da média. 
    list -> list"""
    media_notas = sum(notas[0])//len(notas[0])
    nota_maior = []
    for maior in notas [0]:
        if maior > media_notas:
            nota_maior.append(maior)
            return sorted(nota_maior)