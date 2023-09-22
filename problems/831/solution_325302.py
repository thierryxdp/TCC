def lingua_p(palavra):
    """Recebe como entrada uma palavra e a cada vogal desta palavra
    é acrescentada após esta vogal a letra "p" mais esta vogal, em seguida.
    Exemplos:
    "exemplo"->epexepemplopo
    "lucas"->lupucapas
    "luis"->lupuipis;
    
    Entrada:str
    Saída:str
    
    """
    s=""
    for letra in palavra:
        if letra in "áéíóúaeiouÁÉÍÓÚAEIOU":
            l=letra
            letra+="p"
            letra+=l
        s+=letra
    return s