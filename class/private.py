class BagOfWords:
    def __init__(self):
        self.__words = {}

    def add(self, word):
        self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1

    def __getitem__(self, word):
        return self.__words.get(word.lower(), 0)

    def __setitem__(self, word, count):
        self.__words[word.lower()] = count

    def __len__(self):
        return len(self.__words)

    def __iter__(self):
        return iter(self.__words)


document = BagOfWords()
document.add("python")
document.add("python")
document.add("Python")

print(document._BagOfWords__words)
