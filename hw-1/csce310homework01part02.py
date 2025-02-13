def isAnagram(word01, word02):
    word01_frequency = {}
    word02_frequency = {}

    for char in word01:
        if char in word01_frequency:
            word01_frequency[char] = word01_frequency[char] + 1
        else:
            word01_frequency[char] = 1

    for char in word02:
        if char in word02_frequency:
            word02_frequency[char] = word02_frequency[char] + 1
        else:
            word02_frequency[char] = 1

    return word01_frequency == word02_frequency


if __name__ == "__main__":
    word01 = input()
    word02 = input()
    if isAnagram(word01, word02):
        print("{} and {} are anagrams.".format(word01, word02))
    else:
        print("{} and {} are not anagrams.".format(word01, word02))
