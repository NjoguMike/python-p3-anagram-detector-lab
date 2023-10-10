# your code goes here!
# anagram_list = ['enlists', 'google', 'inlets', 'banana']
class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,anagram_list):
        anagram_word = ''.join(sorted(self.word))
        sorted_list = [''.join(sorted(lett)) for lett in anagram_list]
        matches = []
        for word in anagram_list:
            if ''.join(sorted(word)) in sorted_list and ''.join(sorted(word)) == anagram_word:
                matches.append(word)
        return matches 

    
# ana = Anagram("lisen")
# print(ana.match(anagram_list))