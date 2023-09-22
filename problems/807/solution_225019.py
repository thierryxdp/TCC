def conta_frases(s):
for line in textContent:
    pontofinal += line.count(".")
    interrogacao += line.count("?")
    exclamacao += line.count("!")
    reticencias += line.count("...")
    

frases = pontofinal + interrogacao + exclamacao + reticencias
return frases