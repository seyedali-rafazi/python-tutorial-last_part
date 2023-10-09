class BagOfWords:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1

    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)

    def __setitem__(self, word, count):
        self.words[word.lower()] = count

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        return iter(self.words)


document = BagOfWords()
document.add("python")
document.add("python")
document.add("Python")
document.add("c#")
document["python"]
document["python"] = 10

print(document.words)
print(document["python"])
print(len(document))
for word in document:
    print(word)
