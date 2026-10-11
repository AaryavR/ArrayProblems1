
score = int(input("Enter score: "))
def reverse(score):
    arr, i, j = list(range(1, score+1)), 0, score-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i] 
        i += 1; j -=1
    return arr

def group_reverse(score):
    arr = [1, 2, 3, 4, 5, 6]
    for i in range(0, 6, score):
        arr[i:i+score] = arr[i:i+score][::-1]
    return arr

def left_rotate(score):
    arr = [1, 2, 3, 4, 5]
    score = score % len(arr)
    return arr[score:] + arr[:score]


print(f"reverse({str(score)}) = {reverse(score)}")
print(f"group_reverse({str(score)}) = {group_reverse(score)}")
print(f"left_rotate({str(score)}) = {left_rotate(score)}")
