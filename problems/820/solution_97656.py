def posLetra(s,l,o):
    """Retorna em que posição da string aquela ocorrência da letra está.
    string, string, int --> int."""
    
    s_lista = list(s)
    lista_letras =[]
    i = 0
    
    while i < len(s_lista):
        if s_lista[i] == l:
            list.append(lista_letras, i)
        i = i + 1
    
    index = o - 1
   
	return lista_letras[index]