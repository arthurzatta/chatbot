import re
from typing import List, Tuple
from nltk.stem import SnowballStemmer

class LexicalAnalyser:
    def __init__(self) -> None:
        self.adjetivos = ["quebrado", "aquecido", "lento", "rápido", "barulho",
                          "barulhento", "travando", "travado", "defeito", "problema", "tela azul"]
        self.verbo = ['é', 'são', 'está', 'estão',
                      'fica', 'ficam', 'faz', 'faço']
        self.dispositivos = ['notebook', 'computador', 'impressora', 'pc', 'memória', 'armazenamento', 'hd', 'disco rígido', 'placa de vídeo',
                             'hdmi', 'internet', 'cooler', 'bateria', 'ram', 'carregador', 'usb', 'linux', 'windows', 'fone de ouvido', 'headset', 'headphone', 'tela']
        self.fabricante = ['dell', "samsung", "acer", "asus",
                           "lenovo", "razer", "aoc", "nvidia", "microsoft", "sony"]
        self.indagacao = ['o que', 'qual', 'quais', 'como', 'onde', 'porque']
        self.negacao = ['não', 'nunca', 'sem']

        self.symbol_table = []

    def start(self, sentence: str) -> List[Tuple[str, str]]:
        pass

    def remove_invalid_chars(self, sentence: str) -> str:
        return re.sub('[^a-záàâãéèêíóôõúçA-Z0-9 \n]', '', sentence, flags=re.IGNORECASE)

    def check_keyword(self, keywords: List[str], word: str,):
        is_keyword = False

        for keyword in keywords:
            if (keyword == word):  # talvez precise ser feito com uma regex
                is_keyword = True
        print(is_keyword, word)
        return is_keyword

    def check_lexeme(self, keywords: List[str], lexeme: str):
        is_keyword = True

        for keyword in keywords:
            regex_pattern = '({})+'.format(keyword)
            if(re.search(regex_pattern, lexeme, flags=re.IGNORECASE) == None):
                is_keyword = False
        return is_keyword

    def get_lexeme(self, source_word: str) -> List[Tuple[str, int]]:
        return SnowballStemmer('portuguese').stem(source_word)

    def insert_symbol(self, keywords: List[str], word: str, type_token: str):
        if(not self.check_keyword(keywords, word)):
            lexeme = self.get_lexeme(word)
            if(self.check_lexeme(keywords, lexeme)):
                self.symbol_table.append(Tuple(word, type_token))

    def create_symbol_table(self, sentence) -> List[Tuple[str, str]]:
        split_sentence = self.remove_invalid_chars(sentence).split(' ')

        for word in split_sentence:
            self.insert_symbol(self.adjetivos, word, 'adjetivo')
            self.insert_symbol(self.verbo, word, 'verbo')
            self.insert_symbol(self.dispositivos, word, 'dipositivo')
            self.insert_symbol(self.fabricante, word, 'fabricante')
            self.insert_symbol(self.indagacao, word, 'indagacao')
            self.insert_symbol(self.negacao, word, 'negacao')
