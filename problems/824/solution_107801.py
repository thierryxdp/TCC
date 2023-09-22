def uppCons(frase):
    """ A funçao uppCons recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas (e os demais caracteres exatamente como estavam na frase original).
        
        Parameters:
            frase = frase a ser modificada

        Testes:
            uppCons("") = ""
            uppCons("") = ""
            uppCons("") = ""
            
        Returns:
            lista contendo todos os elementos da lista original que forem divisíveis por n.
            str --> str
    """
    frase = str.upper(frase)
    frase = str.replace(frase,"A","a")
    frase = str.replace(frase,"E","e")
    frase = str.replace(frase,"I","i")
    frase = str.replace(frase,"O","o")
    frase = str.replace(frase,"U","u")
    return frase