# Owen Kroeger
# My Own Work

def Collatz():

    
    flag = "" # flag to test for another pass

    # Collatz sequence
    while (flag != "n"):

        c0 = 0
        c0 = int(input("Enter a number to test: "))

        count = 1
        cn = c0
        cn1 = 0

        # Collatz sequence - update cn1, then set cn = cn1
        while(cn != 1):

            # cn is even
            if(cn % 2 == 0):
                cn1 = cn/2

            # cn is odd
            else:
                cn1 = 3*cn + 1

            cn = cn1
            count += 1

        print(f'C[0] = {c0} has {count} terms.')
        
        flag = input("Test another number (y/n)?: ")
        print()
    

Collatz()