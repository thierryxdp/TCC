def uppCons(frase):
    minusculo = 'bcçdfghjklmnpqrstvwxyz'         #Mapa de consoantes minúsculos com 'ç'.
    maiusculo = 'BCÇDFGHJKLMNPQRSTVWXYZ'         #Mapa de consoantes maiúsculas com 'Ç'.
    tabela = str.maketrans(minusculo, maiusculo) #Cria a tabela de tradução de caracteres.
    return frase.translate(tabela)