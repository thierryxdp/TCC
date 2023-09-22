def consoantes_maiusculas(frase):
    lowercase = 'bcçdfghjklmnpqrstvwxyz'         #Mapa de consoantes minúsculos com 'ç'.
    uppercase = 'BCÇDFGHJKLMNPQRSTVWXYZ'         #Mapa de consoantes maiúsculas com 'Ç'.
    tabela = str.maketrans(lowercase, uppercase) #Cria a tabela de tradução de caracteres.
    return frase.translate(tabela)