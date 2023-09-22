def lingua_p(palavra):
    """Cálculo de uma função que recebe como entrada uma palavra em português 
       e retorna esta traduzida para a lingua do P. 
    
       Parameters:
       palavra: palavra, em português, que será traduzida para a lingua do P
       
       Returns:
       Retorna a palavra de entrada traduzida para a lingua do P, dado que:
       str -> str."""
    vogais='aeiou'
    for i in range(len(palavra)):
        if i in vogais:
            k='p'+vogais
        k=k+1
    return k