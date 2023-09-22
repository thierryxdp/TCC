def hashtag(s):
    """Dado a string(s), retorna outra string com o caractere #
    no início, no meio e no final dela.
    A string dado como parâmetro deve ser colocada entre aspas;
    str -> str"""
    meio = len(s)//2
    return "#"+s[:meio]+"#"+s[meio:]+"#"