def uppCons(frase):
    """Cálculo de uma função que recebe uma frase como entrada e retorna a 
    frase com todas as suas consoantes maiusculas e os demais caracteres exatamente
    como estavam na frase original.
       
       Paramenters:
       frase: frase que será analisada e modificada
       
       Returns:
       Retorna uma frase contendo todas as consoantes em letra maiuscula e as que não são
       da mesma forma que estavam na frase original, dado que:
       str -> str."""
    frase_tratada=''
    i=0
    while i< len(frase):
        caractere=frase[i]
        if caractere in 'çbcdfghjklmnpqrstvxwyz':
            caractere=str.upper(caractere)
        frase_tratada=frase_tratada + caractere
        i=i+1
    return frase_tratada