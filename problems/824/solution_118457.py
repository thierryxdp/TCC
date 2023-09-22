def consoantes_maiusculas(frase):
    lowercase = 'bcçdfghjklmnpqrstvwxyz'
    uppercase = 'BCÇDFGHJKLMNPQRSTVWXYZ'
    tabela = str.maketrans(lowercase, uppercase) 
    return frase.translate(tabela)