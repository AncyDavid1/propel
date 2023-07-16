my_sentence = input("Enter a string: ")
l_count = 0
d_count = 0

for i in my_sentence:
    if i.isalpha():
        l_count += 1
    elif i.isdigit():
        d_count += 1
print("LETTERS", l_count)
print("DIGITS", d_count)