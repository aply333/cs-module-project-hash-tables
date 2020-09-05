def word_count(s):
    splitted = s.split(" ")
    for x in splitted:
        if x 

    return splitted
    # Your code here

test_string = "This is a test, to work with and is containing double double."

print(word_count(test_string))

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))