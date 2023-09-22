def lingua_p(palavra):
    """dada uma palavra em portugûes, a função retorna essa palavra convertida para
    a língua do P. Para isso, após cada vogal, é adicionada a letra p seguida da vogal.
    Por exemplo: a entrada 'então' retornaria 'epentapaopo'.
    str-->str
    
    Parâmetros
    palavra: palavra em português, entre "", que será convertida para a língua do p."""
    nova=""
    for letra in palavra:
        if letra in "AEIOUaáeéiíoóuúàâêô":
            nova=nova+letra+"p"+letra
        else:
            nova=nova+letra
    return str.lower(nova)