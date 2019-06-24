import re

class Preper():
    """
    Does preprocessing of text in Farsi (Persian) language
    """
    
    #THIS IS WHERE YOU READ STOP WORDS LIST
    with open('stopwords.txt' , 'r', encoding = 'utf-8') as f:
        stopwords_text = f.read()
    stopwords = stopwords_text.split()

    def __init__(self,text):
        self.text = text

    def stem_word(self,word):
        """ 
        Finds Farsi (Persian) words stem
        """

        # It is assumed that the stem has at least three letters.
        # Also, the biggest Persian suffix has four letters
        if len(word)<=3:
            remove_suffix = False
            remained_letters = []
        else:
            remove_suffix = True
            remained_letters = list(word[3:])

        while remove_suffix:
            sufflen = 0
            suff_letters = ['','','','']
            for i in range(min(4,len(remained_letters))):
                suff_letters[3-i] = remained_letters[-i-1]

            #Sufixes: بر، تر، گر، دار، بار، گیر
            if suff_letters[-1] == 'ر':
                if suff_letters[-2] in ['ب','گ','ت']:
                    sufflen = 2
                elif suff_letters[-2] == 'ا':
                    if suff_letters[-3] in ['ب','د']:
                        sufflen = 3
                elif suff_letters[-2] == 'ی':
                    if suff_letters[-3] == 'گ':
                        sufflen = 3
            #Sufixes: haa, aasaa
            elif suff_letters[-1] == 'ا':
                if suff_letters[-2] == 'ه':
                    sufflen = 2
                elif suff_letters[-2] == 'س':
                    if suff_letters[-3] == 'ا':
                        sufflen = 3

            #Sufixes: eem, yim, m, am
            elif suff_letters[-1] == 'م':
                if suff_letters[-2] == 'ا':
                    sufflen = 2
                elif suff_letters[-2] == 'ی':
                    if suff_letters[-3] in ['ا','ی']:
                        sufflen = 3
                    else:
                        sufflen = 2
                else:
                    sufflen = 1

            #Suffixes: t, st, eet, aat
            elif suff_letters[-1] == 'ت':
                if suff_letters[-2] in ['ا','ی','س']:
                    sufflen = 2
                else:
                    sufflen = 1
            #Suffixes: ee, yee, gee
            elif suff_letters[-1] == 'ی':
                if suff_letters[-2] in ['ا','ی']:
                    sufflen = 2
                elif suff_letters[-2] == 'گ':
                    sufflen=2
                    #Persian exception: add letter "he" to main word
                    remained_letters = remained_letters[:-2] + ['ه'] + remained_letters[-2:]
                else:
                    sufflen = 1
            #Suffixes: sh, ash, yash
            elif suff_letters[-1] == 'ش':
                if suff_letters[-2] in ['ا','ی']:
                    sufflen = 2
                else:
                    sufflen = 1
            #Suffixes: n, aan, een, saan, gaan
            elif suff_letters[-1] == 'ن':
                if suff_letters[-2] == 'ی':
                    sufflen = 2
                elif suff_letters[-2] == 'ا':
                    if suff_letters[-3] == 'س':
                        sufflen = 3
                    elif suff_letters[-3] == 'گ':
                        sufflen = 3
                        remained_letters = remained_letters[:-3] + ['ه'] + remained_letters[-3:]
                    else:
                        sufflen = 2
                else:
                    sufflen = 1
            #Suffixes: nad, eed, yand, eed, and, abad
            elif suff_letters[-1] == 'د':
                if suff_letters[-2] in ['ی','ن']:
                    if suff_letters[-3] in ['ا','ی']:
                        sufflen = 3
                    else:
                        sufflen = 2
                elif suff_letters[-2] =='ا':
                    if suff_letters[-3] == 'ب':
                        if suff_letters[-4] == 'ا':
                            sufflen = 4
            #Suffixes: k, naak
            elif suff_letters[-1] == 'ک': 
                if suff_letters[-2] == 'ا':
                    if suff_letters[-3] == 'ن':
                        sufflen = 3
                else:
                    sufflen = 1
            #Suffixes: baareh, gaaneh, gaah
            elif suff_letters[-1] == 'ه':
                if suff_letters[-2] == 'ر':
                    if suff_letters[-3] == 'ا':
                        if suff_letters[-4] == 'ب':
                            sufflen = 4
                elif suff_letters[-2] == 'ا':
                    if suff_letters[-3] == 'گ':
                        sufflen = 3
                elif suff_letters[-2] == 'ن':
                    if suff_letters[-3] == 'ا':
                        if suff_letters[-4] == 'گ':
                            sufflen = 4

            if sufflen != 0:
                remained_letters = remained_letters[:-sufflen]

            if len(remained_letters) == 0 or sufflen == 0:
                remove_suffix = False

        word = word[:3] + ''.join(remained_letters)
     
        #Remove prefix
        if len(word) <= 3:
            remove_prefix = False
            remained_letters = []
        else:
            remove_prefix = True
            remained_letters = list(word[:-3])

        while remove_prefix:
            prelen = 0
            pre_letters = ['','','']
            for i in range(min(len(remained_letters),3)):
                pre_letters[i] = remained_letters[i]
            #prefixes: ba, bar, baa
            if pre_letters[0] == 'ب':
                if pre_letters[1] in ['ا','ر']:
                    prelen = 2
                else:
                    prelen = 1
            #prefixes: na, naa
            if pre_letters[0] == 'ن': 
                if pre_letters[1] == 'ا':
                    prelen=2
                else:
                    prelen = 1
            #prefixes: pish
            if pre_letters[0] == 'پ':
                if pre_letters[1] == 'ی':
                    if pre_letters[2] == 'ش':
                        prelen = 3
            #prefixes: ham
            if pre_letters[0] == 'ه':
                if pre_letters[1] == 'م':
                    prelen = 2
            #prefixes: mee
            if pre_letters[0] == 'م':
                if pre_letters[1] == 'ی':
                    prelen = 2

            if prelen != 0:
                remained_letters = remained_letters[prelen:]

            if len(remained_letters) == 0 or prelen == 0:
                remove_prefix = False

        word = ''.join(remained_letters) + word[-3:]
        return word

    def remove_noise(self):
        """
        Removes digits, punctuations, and non-Arabic letters characters from the text
        """
        self.text = re.sub('\W+',' ',self.text)
        self.text = re.sub('[a-zA-Z0-9]', ' ', self.text)
        words = self.text.split()
        #remove stop words and stemming words
        words = list(filter(lambda word: word not in Preper.stopwords, words))
        return words

    def normalise_letter(self):
        """
        Normalises the text by mapping diffrent glyphs of same letter to one glyph (the most common glyph).
        """
    
        #Normalises letter ا"
        self.text = re.sub('[ﭑآأإٱٲٳٵﭐ]','ا',self.text)
        #Normalising letter "ت"
        self.text = re.sub('[ةٹٺټٽۃ]','ت',self.text)
        #Normalises letter "ک"
        self.text = re.sub('[ػؼكڪګڬڭڮ]','ک',self.text)
        #Normalises letter "گ"
        self.text = re.sub('[ڰڱڲڳڴ]','گ',self.text)
        #Normalises letter "و"
        self.text = re.sub('[ۇؤٶ]','و',self.text)
        #Normalises letter "ه"   
        self.text = re.sub('[ھہەﻫ]','ه',self.text)
        #Normalises letter "ی"
        self.text = re.sub('[ىي]','ی',self.text)