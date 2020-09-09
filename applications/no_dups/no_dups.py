def no_dups(s):
    # Your code here
    array = s.split(" ")
    storage = {}
    new_arr=[]
    for x in array:
        if x not in storage:
            new_arr.append(x)
        storage[x]=x
    return " ".join(new_arr)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))