def lingua_p(palavra):
    palavra=palavra.lower()
    palavra=palavra.replace("a", "apa")
    palavra=palavra.replace("e", "epe")
    palavra=palavra.replace("i", "ipi")
    palavra=palavra.replace("o", "opo")
    palavra=palavra.replace("u", "upu")
    palavra=palavra.replace("í", "ípí")
    palavra=palavra.replace("á", "ápá")
    palavra=palavra.replace("ú", "úpú")
    return palavra