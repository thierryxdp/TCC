def bigger_than(decreacing_list, num):
    full_list = insert_sort_des(decreacing_list, num)
#    sub_list = [ elem if not elem == num break for elem in full_list]
#    sub_list = [ val = elem if not elem == num break for elem in full_list]
    sub_list = [ elem for elem in full_list if elem > num ]
    return sub_list


def acima_da_media(qualif):
    sum = 0
    for note in qualif:
        sum += note
        
    mean = sum / len(qualif)
    acima_da_media = bigger_than(qualif, mean)
    
    return mean, acima_da_media