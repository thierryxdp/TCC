def substitui(s,x,i):
    """Retorna uma string s, substituindo o elemento de posição
    i pelo caractere x
    string, str, int -> string"""
  	return s[0:i] + x + s[i+1:]

# Casos de teste:
# substitui("Oi","H",0) == "Hi"
# substitui("Maria","e",4) == "Marie"
# substitui("Tudo bem.","?",8) == "Tudo bem?"