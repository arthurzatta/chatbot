class Token:
    def __init__(self, lexeme: str, synonymous: str, type_token: str) -> None:
        self.__lexeme = lexeme
        self.__synonymous = synonymous
        self.__type = type_token

    def get_lexeme(self):
        return self.__lexeme

    def get_synonymous(self):
        return self.__synonymous

    def get_type(self):
        return self.__type

    def __str__(self) -> str:
        return "word='{}' lexema='{}' type=<{}>".format(self.__synonymous ,self.__lexeme, self.__type)
        