data = input()
arr = []
for i in range(len(data)):
    arr.append(data[i])
count = 1
for i in range(int(len(arr)/2) + 1):
    if arr[i] == arr[-i-1]:
        pass
    else:
        count = 0
        print("Not a Palindrome")
        break
if count == 1:
    print("It is a Palindrome")
