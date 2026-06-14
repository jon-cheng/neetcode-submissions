class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_freq(s)==self.get_freq(t)

    def get_freq(self,word):
        freq_dict = {}
        for letter in word:
            if letter not in freq_dict:
                freq_dict[letter] = 1
            else:
                freq_dict[letter] += 1
        return freq_dict
    

        