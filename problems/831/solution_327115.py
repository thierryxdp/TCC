def lingua_p(palavra):
    """Cálculo de uma função que recebe como entrada uma palavra em português 
       e retorna esta traduzida para a lingua do P. 
    
       Parameters:
       palavra: palavra, em português, que será traduzida para a lingua do P
       
       Returns:
       Retorna a palavra de entrada traduzida para a lingua do P, dado que:
       str -> str."""
    k=str.split(palavra)
    p=str.join('p',k)
    soma=0
    for i in k:
        if i in p:
            p=p+k
        soma=soma+1
    return p