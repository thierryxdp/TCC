def lingua_p(palavra):
    """Dada uma palavra(em português), a função vai retornar a mesma palavra
    na língua do P. A língua P introduz, após cada vogal da palavra, uma letra 
    P mais a vogal anterior.
       A palavra deve ser escrita entre aspas e vai ser retornada em letra minúscula.
       Exemplo--> (entao) --> (epentapaopo);
       str --> str"""
    palavra = str.lower(palavra)
    palavra_nova = ""
    for indice in palavra:
        if indice in "AEIOUaeiouÁÉÍÓÚáéíóú":
            palavra_nova = palavra_nova + indice + "p" + indice
        else:
            palavra_nova = palavra_nova + indice
    return palavra_nova