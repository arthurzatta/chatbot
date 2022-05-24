from pathlib import Path


class Reader:
    @staticmethod
    def read_stopwords():
        try:
            stopwords = []
            stopwords_file = Path('./assets/out_stopwords.txt')
            if stopwords_file.exists():
                with stopwords_file.open() as file:
                    for read_word in file:
                        strip_word = read_word.strip()
                        stopwords.append(strip_word)
            return stopwords
        except Exception:
            print('File out_stoprwords.txt not found')