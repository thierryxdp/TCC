def lingua_p (palavra):
    resultado = ""
    for l in range (len(palavra)):
        if palavra [l] in "qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM":
            resultado = resultado + palavra [l]
        else:
            resultado = resultadop + palavra [l] + "p" + palavra [l]
        return resultado