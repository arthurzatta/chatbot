from pathlib import Path


class LexicalAnalyser:
    def __init__(self):
        self.stopwords = []

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

if __name__ == '__main__':
    analyser = LexicalAnalyser()
    analyser.stream_reader()
