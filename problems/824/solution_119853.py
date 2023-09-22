def uppCons(frase):
        """
        """
        frase1 = frase
        for i in frase:
            if i in "aeiou":
                frase1 = farse1.replace(frase[i], frase1.upper())