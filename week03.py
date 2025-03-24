def myZip(l1, l2):
    l12 = 0
    if(len(l1) > len(l2)):
        l12 = len(l2)
    else:
        l12 = len(l1)

    l3 = list()
    for i in range(l12):
        l3.append((l1[i], l2[i]))
    return l3

group = ['BlackPink', 'Hot', 'Seventeen', 'NJZ']
ratings = [1,2]
#ratings = [1,2,4,3,100]

group_rating = myZip(group,ratings)
print(group_rating)