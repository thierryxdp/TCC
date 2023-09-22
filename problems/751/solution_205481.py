import str.rsplit from str
def quant_palavras(frase: st) -> int:
    """Conta a quantidade de palavras em uma dada frase

       Parameters:
       frase: frase a ser analisada

       Returns:
       Quantidade de palavras da frase

       Passos:
       1) Separar os espaços vazios das palavras
       2) Listar apenas as palavras
       3) Contar quantas palavras ficaram na lista
    """
    return len(str.split(frase))