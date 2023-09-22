def substitui(s,x,i):
    """Retorna uma string s, substituindo o elemento de posição
    i pelo caractere x
    string, int, int -> string"""
  	return s[0:i] + str(x) + s[i+1:]

# Casos de teste:
# substitui("Oi",2,0) == "2i"
# substitui("Maria",3,4) == "Mari3"
# substitui("Tudo bem?",0,3) == "Tud0 bem?"