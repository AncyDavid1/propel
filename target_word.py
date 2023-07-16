
def find_word_positions(sentence, target_word):
    words = sentence.split()
    positions = []
    for i, word in enumerate(words, 0):
        if word == target_word:
            positions.append(i)
    if positions:
        return positions
    else:
        return False
sentence = input("Enter a string of words: ")
target_word = input("Enter the target word: ")
result = find_word_positions(sentence, target_word)

if result:
    print(result)
else:
    print(False)