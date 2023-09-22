def uppCons (frase):
    """Função que retorna todas as consoantes da frase maiúsculas;
       str -> str."""
    i= 0
    frasenova= " "
    while i < len (frase):
        if frase [i] is not "AEIOUaeiou":
            frasenova = str.upper (frase [i])
        i= i+1
    return frasenova