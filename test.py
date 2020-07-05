def check_result(values,x,squared,jacobi,bits,n,whois):
    count1 = 0
    countother = 0
    i = 0
    while(i < len(x)):
        temp = (x[i]**2) % n
        if(str(temp) != str(squared[i])):
            return False
        i += 1
    i = 0
    while(i < len(x)):
        j = 0
        found = False
        while(j < len(values)):
            if(x[i] == values[j]):
                found = True
                if(jacobi[j] == bits[i]):
                    count1 += 1
                else:
                    countother += 1
            j += 1
        if(not found):
            return found
        i += 1
    print(whois," ",count1," ",countother)
    if(whois == "Alice"):
        if(countother > count1):
            return "Won"
        else:
            return "Lost"
    else:
        if(countother > count1):
            return "Lost"
        else:
            return "Won"

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 36, 45, 49, 62, 63, 64, 66, 68]
jacobi = [1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
bits = [-1,1,1,1,-1,1,-1,-1,1,-1,-1]
res = [10,25,15,9,45,68,14,3,63,35,66]
xsq = [100,625,225,81,904,140,196,9,606,104,993]
n = 1121
print(check_result(values,res,xsq,jacobi,bits,n,"Bob"))