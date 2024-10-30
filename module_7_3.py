import string


class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = ''.join(char for char in line if char not in string.punctuation)
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


# finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
# print(finder.file_names)  # ['file1.txt', 'file2.txt', 'file3.txt']


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего