#retorna um nº de frases em um texto
#str-->int
def conta_frases(a):
    	y=a.count("!")
        z=a.count("?")
        b=a.count("...")
        x=a.count(".")-b*3
        return x+y+z+b