def conta_frases(frase):
x1 = frase.split(".")
x2 = frase.split("; ")
x3 = frase.split("!")
x4 = frase.split("?")
x5 = frase.split("...")
return len(x1) + len(x2) + len(x3) + len(x4) + len(x5)