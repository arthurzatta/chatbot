from typing import Union
from pathlib import Path
import re as Regex

class LexicalAnalyser:
    def __init__(self):
        self.stopwords = []
        self.stream_reader()

    def stream_reader(self):
        try:
            stopwords_file = Path('./assets/out_stopwords.txt')
            if stopwords_file.exists():
                with stopwords_file.open() as file:
                    for read_word in file:
                        strip_word = read_word.strip()
                        self.stopwords.append(strip_word)
        except Exception:
            print('File out_stoprwords.txt not found')

    def get_stopwords(self):
        return self.stopwords

    def check_invalid_chars(self, input_string: str):
        regex = Regex.compile(
            '''^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?´]+(\s[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?´]+)*''')
        return regex.match(input_string)

