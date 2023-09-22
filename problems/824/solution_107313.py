def uppCons(self):
    self.lower()
    frase=""
    vogal=["a","e","i","o","u"]
    for letra in string:
        if letra in vogal:
            frase=frase+letra.lower()
            else:
                frase=frase+letra.upper()
                return frase