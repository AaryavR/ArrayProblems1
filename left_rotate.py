def left_rotate(n):
    arr = [1, 2, 3, 4, 5]
    n = n % len(arr)
    return arr[n:] + arr[:n]

input("left rotate(n) shifts [1, 2, 3 , 4, 5] left by n positions. Press enter")
print("Left rotate(1) =  ", left_rotate(1))

n = int(input("rotate by how many?: "))

print(f"left_rotate({str(n)}) = {left_rotate(n)}")
