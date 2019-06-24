# preper
A Persian (Farsi) Preprocessing Python Module

## About the project
This Python module was developed as part of my Persian text mining project in 2010. It was because I felt lack of a Persian text preprocessing tool/library back then. 

The main operations of this module are:

* Normalise the Letters: maps all glyphs of each letter to one representative glyph
* Remove noises: removes any non-Arabic character, digits, and stop words
* Stem the words: It is an affi stemmers and developed using finite state machine model 

## Built With
Python 3.6 and its built-in modules was used to develop **preper**. `Python 3.*` fully supports unicode characters. So, there is no need to change the characters to
their unicode code point; i.e. `\uxxxx` format. 

# Getting Started

## Prerequisites
There is no third-party library or dependency that you need to install separately.

## Installation
There is no need to install anything. You just need to copy `preper.py` module file into your project folder.

# Usage
The file `use_module.py` is a sample file to help you to understand how to use `preper`. But, basically there is only one thing that should be noticed. The stop words list is already provided in `stopwords.txt` file in the module folder. Should you wish, please feel free to modify/update it.

# Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# License
Distributed under the MIT License. See `LICENSE` for more information.

# Contact
Ali Hosseini on https://twitter.com/a1iie62 or aliie62@yahoo.com

Project Link: https://github.com/aliie62/preper

# Acknowledgements
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* [persian-stopwords](https://github.com/kharazi/persian-stopwords)
