def uppCons(self):
    #equalizando todas as letras
    self.lower()
    #criando uma nova string para serem depositadas as alterações
    frase = ""
    #Definindo as vogais e consoantes
    vogal = ["a", "e", "i", "o", "u"]
    for letra in self:
        #Deixando todas as vogais em minúsculo
        if letra in vogal:
            frase = frase + letra.lower()
        #Deixando todas as consoantes em maiúsculo
        else:
            frase = frase + letra.upper()
    return frase