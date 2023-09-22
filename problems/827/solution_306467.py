def qtd_divisores(n_1:int)->int:
    # Salva o sinal do número
    signal_numb = abs(n_1)//n_1
    def is_divisor(n_2:int)->bool:
        return True if n_1%n_2 == 0 else False
    return len(list(filter(is_divisor,range(signal_numb*1,signal_numb*(n_1//2+1),signal_numb))))+1