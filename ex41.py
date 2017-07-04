def digit_sum(n):
    strn = str(n)

    charlist = []

    for char in strn:
        charlist.append(char)

    int_list = []

    for num in charlist:
        intn = int(num)
        int_list.append(intn)

    numsum = 0

    for i in int_list:
        numsum += i

    return numsum

print digit_sum(1234)
