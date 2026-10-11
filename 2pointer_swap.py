def reverse(n):
    arr, i, j = list(range(1, n+1)), 0, n-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i] 
        i += 1; j -=1
    return arr

input("reverse(n) builds [1..n] and flips it end-to-end using 2 pointers. Press enter")
print("reverse(4) =", reverse(4)) 
n = int(input("Enter list size: "))
print(f"reverse({str(n)}) = {reverse(n)}")