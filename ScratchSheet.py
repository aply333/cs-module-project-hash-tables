test_arr = ["book", "worm", "cookie", "milk"]
test_dict = {}

for i in test_arr:
    test_dict[i] = [i]

print(test_dict)

# no Dups ScratchWork:

test_dupes = "that thing is that there thing"
test_dupes2 = "test test test test"

def Scr_dupes(s):
    arr = s.split(" ")
    storage = {}
    new_arr = []
    for x in arr:
        if x not in storage:
            new_arr.append(x)
        storage[x] = x
    print(storage)
    print(" ".join(new_arr))

Scr_dupes(test_dupes)
Scr_dupes(test_dupes2)