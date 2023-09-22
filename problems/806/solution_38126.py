#Start your python function here
def colisao(ret1,ret2):
    x_ret1 = ret1[:1]
    y_ret1 = ret1[2:3]
    ret1_width = ret1[4:5]
    ret1_height = ret1[6:7]

    x_ret2 = ret2[:1]
    y_ret2 = ret2[2:3]
    ret2_width = ret2[4:5]
    ret2_height = ret2[6:7]

    if (x_ret1 < x_ret2 + ret2_width and
        x_ret1 +  ret1_width > x_ret2 and
        y_ret1 < y_ret2  + ret2_height and
        y_ret1 + ret1_height > y_ret2):

        return True

    else:

        return False