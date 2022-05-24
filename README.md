A etapa de análise léxica inclui as seguintes atividades para confecção do seu tradutor/compilador/chatbot:

1) Verificação léxica, com avaliação do alfabeto usado. Basicamente aceite letras de A-Z, a-z, 0-9, caracteres de pontuação e caracteres especiais presentes no teclado. Ignore caracteres especiais, visíveis ou invisíveis.

2) Como se trata de linguagem natural, providencie uma lista de stopwords que possa ser mobilizada em seu chatbot. A lista pode ser obtida na Internet, de qualquer fonte (indique a fonte). Observe que as palavras-chaves usadas em seu trabalho anterior podem exigir a mudança da lista de stopwords. Altere-a.

3) Geração de lexemas é a redução de palavras encontradas no texto do seu usuário. Nosso chatbot usa Português Brasileiro. Você pode usar um método pronto de geração de lexemas. Obtenha um (indique a fonte) ou crie um.

4) Todas as palavras presentes no texto do seu usuário que não sejam palavras-chaves e stopwords devem ser incluídos em uma estrutura de dados do tipo lista, sua Tabela de Símbolos. Implemente sua Tabela de Símbolos preliminar.

Link regex: regexr.com/6lpb4


## ToDo

- [x] Take off from the stopword file the keywords
- [x] Read stopword file
- [x] Check the input text structure and identify invalid characters 
  - [] **Almost done needs to check the regex again and look if it matches with all invalid chars**
- [] Generate lexemes based on word in the text
- [] Create a symbol table with words different from keywords

- [] Entrar com as palavras
- [x] Remover pontuações das frases
- [x] Verificar se existem keywords
  - [] Caso exista remover elas
  - [x] Caso não existam
      - [x] Gerar lexemas e verificar se são compativeis com os tipos das keywords
        - [x] Guardar as palavras correlatas na lista de simbolos -> (palavra, tipo)
  - [x] Verificar palavras repetidas
  - [] Manter espaço em palavras chaves especificas