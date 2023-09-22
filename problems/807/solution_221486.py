def conta_frases(frase):
    """docstring""" 
    frase1= str.split("frase.")
    frase2= str.split("frase!")
    frase3= str.split("frase?")
    frase4= str.split("frase...")
    frase5= str.split("frase")
    frase= frase1, frase2, frase3, frase4, frase5
    return  len ( frase )