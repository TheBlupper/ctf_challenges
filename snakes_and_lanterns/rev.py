arr=[38,51,7,6,5,37,13,65,89,69,64,18,33,0,38,52,24,54,78,53,55,40,55,96,8,39,95,1,56,28,21,1,9,91,53,11,13,42,29,61,86,61,92,40,48,52,87,68,93,35,58,94,5,12,48,90,9,14,26,35,89,85,1,67]
inp = input().encode()
assert len(inp) == 64
assert all(ch>32 for ch in inp)

for i in range(8):
    for j in range(8):
        k = inp[8*i+j]-32
        arr[8*i+j] += k
        if i > 0:
            arr[8*(i-1)+j] += k
        if i < 8-1:
            arr[8*(i+1)+j] += k
        if j > 0:
            arr[8*i+j-1] += k
        if j < 8-1:
            arr[8*i+j+1] += k
        arr = [x%97 for x in arr]
if all(x==0 for x in arr):
    print('nice job :)')
else:
    print('bad job >:(')