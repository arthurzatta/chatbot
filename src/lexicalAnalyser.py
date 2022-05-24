import unidecode
import re
from typing import List
from nltk.stem import SnowballStemmer
from reader import Reader


class LexicalAnalyser:
    def __init__(self) -> None:
        self.adjetivos = ["quebrado", "aquecido", "lento", "rápido", "barulho",
                          "barulhento", "travando", "travado", "defeito", "problema", "tela azul", "funciona"]
        self.verbo = ['é', 'são', 'está', 'estão',
                      'fica', 'ficam', 'faz', 'faço']
        self.dispositivos = ['notebook', 'computador', 'impressora', 'pc', 'memória', 'armazenamento', 'hd', 'disco rígido', 'placa de vídeo',
                             'hdmi', 'internet', 'cooler', 'bateria', 'ram', 'carregador', 'usb', 'linux', 'windows', 'fone de ouvido', 'headset', 'headphone', 'tela']
        self.fabricante = ['dell', "samsung", "acer", "asus",
                           "lenovo", "razer", "aoc", "nvidia", "microsoft", "sony"]
        self.indagacao = ['que', 'qual', 'quais', 'como', 'onde', 'porque']
        self.negacao = ['não', 'nunca', 'sem']

        self.__normalize_reserved_words()

    def __remove_invalid_chars(self, sentence: str) -> str:
        return re.sub('[^a-záàâãéèêíóôõúçA-Z0-9 \n]', '', sentence, flags=re.IGNORECASE)

    def __remove_acentos(self, sentence: str) -> str:
        return unidecode.unidecode(sentence)

    def __normalize_reserved_words(self):

        def normalized_list(str_list: List[str]):
            return [unidecode.unidecode(word) for word in str_list]

        self.adjetivos = normalized_list(self.adjetivos)
        self.fabricante = normalized_list(self.fabricante)
        self.dispositivos = normalized_list(self.dispositivos)
        self.negacao = normalized_list(self.negacao)
        self.indagacao = normalized_list(self.indagacao)
        self.verbo = normalized_list(self.verbo)

    def normalization(self, sentence: str) -> str:
        sentence = sentence.lower()
        sentence = self.__remove_invalid_chars(sentence)
        sentence = self.__remove_acentos(sentence)
        return sentence.strip()

    def split(self, sentence: str):
        return sentence.split(" ")

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

    def get_lexeme(self, source_word: str) -> str:
        return SnowballStemmer('portuguese').stem(source_word)
