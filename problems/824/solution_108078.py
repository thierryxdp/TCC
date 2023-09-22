def uppCons (frase):
    """Função que retorna todas as consoantes da frase maiúsculas;
       str -> str."""
    i= 0
    frasenova= ""
    while i < len (frase):
        if frase [i]  in "BCDFGHJKLMNPQRSTWXYZbcdfghjklmnpqrstwxyz":
            frasenova = frasenova + str.upper (frase [i])
        else: 
            frasenova= frasenova + frase [i]
        i= i+1
    return frasenova