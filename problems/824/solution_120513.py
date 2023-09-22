def uppCons(string):
    """Recebe uma frase e retorna a mesma com as consoantes em letras maiúsculas, mantendo o
    restante na forma original.
    assinatura: str --> str
    casos de teste:
    uppCons('belo dia para nadar')==(BeLo Dia PaRa NaDaR)
    """
    vog=['a', 'e', 'i', 'o', 'u']
    
    for let in string:
        if let not in vog:
          final.append(let.upper())
        else:
            final.append(let)
        return final
        
       
        
    
    
    """Strings são imutáveis, importante lembrete..."""