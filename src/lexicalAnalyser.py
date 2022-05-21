import re
from typing import List, Tuple
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from reader import Reader


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

        self.symbol_table: List[Tuple(str, str)] = []

    def start(self, sentence: str) -> List[Tuple[str, str]]:
        pass

    def remove_invalid_chars(self, sentence: str) -> str:
        return re.sub('[^a-záàâãéèêíóôõúçA-Z0-9 \n]', '', sentence, flags=re.IGNORECASE).lower()

    def remove_stopwords(self, sentence: List[str]):
        stopwords = Reader().read_stopwords()
        sentence_without_sw = []
        for word in sentence:
            if(not word in stopwords):
                sentence_without_sw.append(word)
        return sentence_without_sw

    def check_keyword(self, word: str):
        if(word in self.verbo or word in self.indagacao):
            return True
        return False

    def check_lexeme(self, keywords: List[str], lexeme: str):
        is_keyword = False
        for keyword in keywords:
            regex_pattern = r'({})+'.format(lexeme)
            regex_match = re.search(
                regex_pattern, keyword, flags=re.IGNORECASE)
            if(regex_match != None):
                is_keyword = True
                break
        return is_keyword

    def get_lexeme(self, source_word: str) -> List[Tuple[str, int]]:
        return SnowballStemmer('portuguese').stem(source_word)

    def search_repeated_words(self, word: str):
        repeat = False
        for symbol in self.symbol_table:
            if(symbol[0] == word):
                repeat = True
        return repeat

    def insert_symbol(self, keywords: List[str], word: str, type_token: str):
        lexeme = self.get_lexeme(word)
        if(self.check_lexeme(keywords, lexeme)):
            if(not self.search_repeated_words(word)):
                self.symbol_table.append((word, type_token))

    def create_symbol_table(self, sentence) -> List[Tuple[str, str]]:
        sentence = self.remove_invalid_chars(sentence).split(" ")
        sentence_without_sw = self.remove_stopwords(sentence)

        for word in sentence_without_sw:
            if(not self.check_keyword(word)):
                self.insert_symbol(self.dispositivos, word, 'dipositivo')
                self.insert_symbol(self.adjetivos, word, 'adjetivo')
                self.insert_symbol(self.fabricante, word, 'fabricante')
                # self.insert_symbol(self.negacao, word, 'negacao')
