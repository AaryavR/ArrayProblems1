def group_reverse(n):
    arr = [1, 2, 3, 4, 5, 6]
    for i in range(0, 6, n):
        arr[i:i+n] = arr[i:i+n][::-1]
    return arr

input("group_reverse(n) reverse [1,2,3,4,5,6] in chunks of n. Press enter")
print("group_reverse(3) = ", group_reverse(3))

n = int(input("Group size: "))
print(f"group_reverse({str(n)}) = {group_reverse(n)}")

