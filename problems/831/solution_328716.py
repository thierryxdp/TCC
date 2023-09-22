def lingua_p(palavra):
    """ Função que recebe como um parâmetro uma palavra(em português) e retorna a palavra traduzida para a língua do P 
    str -> str"""
    
    novapalavra = []
    palavra = palavra.lower()
    
    for i in range(0,len(palavra)+1):
        
        exceto = "aáãâeéiíoóõôuú"

        for i in palavra:

            if i in exceto:
                palavrap = i + "p" + i
                
                novapalavra.append(palavrap)

            else: 
                novapalavra.append(i)
                
        return "".join(novapalavra)