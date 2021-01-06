# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c,h,o):
    water = co2 = methane = 0
    if h >= 2 and o >= 1:
        if 2 * o >= h:
            water = h // 2
            o -= water
            h -= 2*water
        else:
            water = o
            o -= water
            h -= 2 * water

    if o >= 2 and c >= 1:
        if 2 * c >= o:
            co2 = o // 2
            c -= co2
            o -= co2*2
        else:
            co2 = c
            c -= co2
            o -= co2 * 2
    if c >= 1 and h >= 4:
        if c * 4 >= h:
            methane = h // 4
        else:
            methane = c

    return water, co2, methane
