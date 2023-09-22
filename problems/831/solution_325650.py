def lingua_p (palavra):
    """Função que recebe uma palavra e traduz para a lingua do P;
       str -> str."""
    palavra = str.lower (palavra)
    palavra_nova = " "
    lista = str.split (palavra)
    for i in palavra:
        palavra_nova= palavra_nova + i
        if i in "aáeéiíoóuú":
            palavra_nova = palavra_nova + "p" + i
    return palavra_nova