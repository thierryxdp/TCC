def uppCons(frase):
    """
    Função recebe como entrada uma frase e retorna a frase com todas as suas
    consoantes em maiúsculas ( e os demais caracteres exatamente como estavam
    na frase original ).
    str -> str
    """
    vogais=("a","e","i","o","u","A","E","I","O","U","á","é","í","ó","ú","ã","õ","â","Á","É","Í","Ó","Ú","Ã","Õ","Â")
    i=0
    frasefinal=""
    while i<len(frase):
        if frase[i] in vogais:
            frasefinal+=frase[i]
        	i+=1
        else:
        	frasefinal+=str.upper(frase[i])
        	i+=1
    return frasefinal