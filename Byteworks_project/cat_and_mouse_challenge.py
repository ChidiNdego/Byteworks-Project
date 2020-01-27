def catAndMouse(x, y, z):
    dist_1 = abs(x - z)
    dist_2 = abs(y - z)
    if dist_1 < dist_2:
        print("Cat A")
    elif dist_2 < dist_1:
        print("Cat B")
    else:
        print("Mouse C")

#One-liner
# def catAndMouse(x, y, z):
#     a = abs(x-z)
#     b = abs(y-z)
    
#     return "Cat A" if a<b else "Cat B" if b<a else "Mouse C"
