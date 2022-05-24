## Enunciado
Forneça para a disciplina de Compiladores a sua definição gramatical (em gramática formal BNF, por qualquer notação) a sua linguagem natural mobilizada pelo usuário para envio ao chatbot.

Sua linguagem basicamente precisa ter regras gramaticais para perguntas (formas em que o usuário pede ajuda ao chatbot) e para respostas/atribuições/definições, em que ele responde ao chatbot sobre características sobre seus equipamentos/dispositivos/softwares/problemas e que ajudem o chatbot a tomar decisões.

Neste momento, sua gramática precisa fornecer pelo menos cinco regras gramaticais para perguntas e pelo menos dez regras gramaticais para atribuição.

Exemplos de perguntas:
Qual é o produto adequado para fazer X?
Estou com problemas no produto Y.

Exemplos de atribuição:
O modelo é XYZ.
Comprei no dia 15/05/2021.

## Estrutura BNF

<pergunta> := <indagacao><atribuicao> | <indagacao><negacao><atribuicao>

<atribuicao> := <verbo><substantivo>
| <substantivo><verbo><adjetivo>
| <substantivo><adjetivo>
| <substantivo>

<substantivo> := <dispositivos> | <fabricante> | <dispositivo><substantivo> | <fabricante><substantivo>

<adjetivos> := quebrado|aquecido|lento|rápido|barulho|barulhento|travando|travado|defeito|problema|tela azul 

<verbo> := é|são|está|estão|fica|ficam|faz|faço

<dispositivos> := notebook|computador|impressora|pc|memória|armazenamento|hd|disco rígido|placa de vídeo|hdmi|internet|cooler|bateria|ram|carregador|usb|linux|windows|fone de ouvido|headset|headphone|tela 

<fabricante> := dell|samsung|acer|asus|lenovo|razer|aoc|nvidia|microsoft|sony 

<indagacao> := O que|Qual|Quais|Como|Onde|Porque

<negacao> := não|nunca|sem

<stopwords> := qualquer palavra não definida

### Perguntas
1. Qual é o tipo de memória ram do meu computador? 
2. Como faço para trocar a bateria do meu notebook dell? 
3. Meu dispositivo samsung está fazendo barulhos estranhos, o que devo fazer? 
4. Onde ficam as entradas usb do meu notebook asus modelo XXXYY? 
5. Porque meu fone sony modelo ZZZAAA não sai som? 
6. Como faço para meu mouse funcionar no meu computador da marca acer? 
7. Meu computador deu tela azul, como solucionar esse problema? 

## Atribuições

1. Meu computador está com problemas
2. Como consertar meu computador que está aquecendo?
3. Notebook Dell com problema de memória
4. Quero saber o que aconteceu com meu notebook que está dando tela azul
5. É da dell
6. Está travando
7. Não liga
8. Meu asus está fazendo barulho
9. Telas
quebrado|aquecido|lento|rápido|barulho|barulhento|travando|travado|defeito|problema|tela azul|é|são|está|estão|fica|ficam|faz|faço|notebook|computador|impressora|pc|memória|armazenamento|hd|disco rígido|placa de vídeo|hdmi|internet|cooler|bateria|ram|carregador|usb|linux|windows|fone de ouvido|headset|headphone|tela|dell|samsung|acer|asus|lenovo|razer|aoc|nvidia|microsoft|sony| O que|Qual|Quais|Como|Onde|Porque|não|nunca|sem 
 
