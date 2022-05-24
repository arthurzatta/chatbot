from typing import List
import re
from lexicalAnalyser import LexicalAnalyser
from chatToken import Token

class Main:
    def __init__(self) -> None:
        self.symbol_table = []
        self.lexicalAnalyser = LexicalAnalyser()

    def search_repeated_words(self, word: str):
        repeat = False
        for symbol in self.symbol_table:
            if(symbol.get_synonymous() == word):
                repeat = True
        return repeat

    def check_lexeme(self, list_words: List[str], lexeme: str) -> str:
        match_str = ''
        regex_pattern = r'({})+'.format(lexeme)

        for word in list_words:
            regex_match = re.search(
                regex_pattern, word, flags=re.IGNORECASE)
            if(regex_match != None):
                match_str = word

        return match_str

    def insert_symbol(self, keywords: List[str], word: str, type_token: str):
        lexeme = self.lexicalAnalyser.get_lexeme(word)
        synonymous = self.check_lexeme(keywords, lexeme)
        if(synonymous != ''):
            if(not self.search_repeated_words(synonymous)):
                self.symbol_table.append(Token(lexeme, synonymous, type_token))

    def create_symbol_table(self, sentence: str):
        sentence_normalized = self.lexicalAnalyser.normalization(sentence)
        sentence_without_sw = self.lexicalAnalyser.remove_stopwords(
            self.lexicalAnalyser.split(sentence_normalized))
        if(sentence_without_sw != []):
            for word in sentence_without_sw:
                if(not self.lexicalAnalyser.check_keyword(word)):
                    self.insert_symbol(
                        self.lexicalAnalyser.adjetivos, word, 'adjetivo')
                    self.insert_symbol(
                        self.lexicalAnalyser.dispositivos, word, 'dipositivo')
                    self.insert_symbol(
                        self.lexicalAnalyser.fabricante, word, 'fabricante')
                    self.insert_symbol(self.lexicalAnalyser.negacao, word, 'negacao')


if __name__ == '__main__':
    SENTENCE = 'Meu computador dell está sem vídeo nvidia'
    main = Main()
    main.create_symbol_table(SENTENCE)
    for token in main.symbol_table:
        print(token)