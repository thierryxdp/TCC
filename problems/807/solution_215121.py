def conta_frases(texto):
    quantidade1= len(texto.split('.'))
    quatidade2= len(texto.split('!'))
    quatidade3= len(texto.split('?'))
    quatidade4= len(texto.split('...'))
    return quantidade1+quantidade2+quantidade3+quantidade4