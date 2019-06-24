"""
Configurations: Down here in line 9, you should set your main text file path; otherwise you can just provide
                   a string variable which contains the text
"""
from preper import Preper

if __name__ == '__main__':
    # THIS IS WHERE YOU READ THE TEXT FILE/SET TEXT VARIABLE THAT YOU WANT TO PROCESS
    with open('[YOUR TEXT FILE PATH]', 'r',encoding = 'utf-8') as f:
        file_content = f.read()

    preper = Preper(file_content)
    preper.normalise_letter()
    words = preper.remove_noise()
    words_stemmed = list(map(preper.stem_word,words))
