def computeLPS(str, lps):
    n = len(str)

    i = 0 
    temp = 0 

    while i < n:
        if  str[i] == str[temp]