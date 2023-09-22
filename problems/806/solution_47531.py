egunda etapa - calculo do resultado
    if x_sup_dir1 <x_inf_esq2 or x_sup_dir2< x_inf_esq1 :
        return False
    elif y_sup_dir1 <y_inf_esq2 or y_sup_dir2 <y_inf_esq1:
        return False
    else:
        return True