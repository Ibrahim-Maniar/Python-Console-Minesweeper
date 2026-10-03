def format(coordinates,height,width):
    lcoords = list(str(coordinates))

    focussed_alphanums = []

    for i in lcoords:
        if i.isalpha() or i.isdigit():
            focussed_alphanums.append(i)

    if len(focussed_alphanums) < 2:
        return -1
 
    if not focussed_alphanums[0].isalpha():
        return -1

    if not focussed_alphanums[-1].isdigit():
        return -1

    if len(focussed_alphanums) > 3:
        return -1

    if not "".join(focussed_alphanums[1:]).isdigit():
        return -1


    numvals = []
    numvals.append(ord(focussed_alphanums[0].upper())-65)

    numvals.append((int("".join(focussed_alphanums[1:])))-1)

    if numvals[0] >= height:
        return -1
    if numvals[0] < 0:
        return -1
    if numvals[1] >= width:
        return -1
    if numvals[1] < 0:
        return -1

    

    return numvals