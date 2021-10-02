# Reverse an array
A = [1, 2, 3, 4, 5, 6]
B = []


# 1 with extra array space O(n)
def reverse(arr):
    for i in range ( len ( arr ) ):
        print ( arr[-i] )
        B.append ( arr[-i] )


# reverse(A)
# print(B)

# 2 inplace reverse

def reverse(arr):
    start = 0
    end = len ( arr ) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print ( arr )


reverse ( A )
print ( len ( A ) )
