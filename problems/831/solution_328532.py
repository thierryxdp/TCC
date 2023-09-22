def ligua_p(palavra):
    """Recebe uma palavra e a retorna na lingua do p com um p posicionado apos cada vogal"""
    palavra1=palavra.replace('e','ep')
    palavra2=palavra1.replace('a','ap')
    palavra3=palavra2.replace('i','ip')
    palavra4=palavra3.replace('o','op')
    palavra5=palavra4.replace('u','up')
    return palavra5