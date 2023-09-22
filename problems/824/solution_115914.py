def uppCons(frase):
    """ A funçao uppCons recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas (e os demais caracteres exatamente como estavam na frase original).
        
        Parameters:
            frase = frase a ser modificada

        Testes:
            uppCons("serviço militar") = "SeRViÇo MiLiTaR"
            uppCons("comida boa e gostosa") = "CoMiDa Boa e GoSToSa"
            uppCons("tudo tranquilo?") = "TuDo TRaNQuiLo?"
            
        Returns:
            frase com todas as suas consoantes em maiúsculas (e os demais caracteres exatamente como estavam na frase original).
            str --> str
    """
    i=0
    Lista_min = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","ç"]
    Lista_con = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","Ç"]
    while i <= len(Lista_con):
        frase = str.replace(frase,Lista_min[i],Lista_con[i])
        i = i+1
    
    return frase