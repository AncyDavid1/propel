def count_word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        contained_word = frequency.get(word, 0) + 1
        frequency[word]=contained_word

    return frequency
sentence = input("Enter some words: ")
word_frequency = count_word_frequency(sentence)

for word, count in word_frequency.items():
    print(word.capitalize(), "-", count)