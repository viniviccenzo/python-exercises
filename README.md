# Exercícios básicos de Python

## Exercício 1 - Par ou Ímpar

Peça ao usuário um número. Retorne a ele se o número é par ou impar.

### Discussão

Conceitos trabalhados:

* Entrada de dados (comando `input`)
* Aritmética modular (oparador módulo `%`)
* Condicionais (cláusulas `if`)
* Verificar igualdade (operador `==`)

### Entrada de dados

Para obter a entrada do usuário em python, usamos o comando `input`. Podemos armazenar o resultado em uma variável. A resposta de um `input` sempre será uma `string`.

```python
name = input("Diga o seu nome: ")
print("Seu nome é " + name)
```

### Aritmética modular (operador módulo)

O operador módulo nada mais é que o resto da divisão. Por exemplo, dividindo 5 por 3 o resto é 2. Podemos ler essa operação como: "5 módulo 3 é 2". Em python:

```
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

### Condicionais

Em python, a sintaxe de uma cláusula `if` não difere tanto de outras linguagens. A principal diferença é a ausência de parênteses na condição e o fato de que os blocos não possuem nenhum marcador, como chaves {}. Ao invés disso, são marcados por uma identação (por padrão, 4 espaços).

```python
if age > 17:
    print("Pode ver um filme R-rated")
elif age < 17 and age > 12:
    print("Pode ver um filme PG-13")
else:
    print("Só pode ver filmes PG")
```

### Verificando igualdade

Em python, verificamos igualdade com operadores como `==` igual e `!=` diferente. Podemos usar esses operadores com inteiros, strings, floats, etc.

```python
if a == 3:
    print("A variável tem o valor 3")
elif a != 3:
    print("A variável não tem o valor 3")
```

Note que aqui, a condição de `elif` é completamente desnecessária, uma vez que se a não for igual a 3, obviamente será diferente de 3. Poderíamos reescrever o código acima desta forma:

```python
if a == 3:
    print("A variável tem o valor 3")
else:
    print("A variável não tem o valor 3")
```
---

## Exercício 2 - Palíndromos

Peça uma string qualquer ao usuário e informe a ele se a string é um palíndromo ou não. (um palíndromo é uma string que pode ser lida da mesma forma, da esquerda para a direita ou vice-versa. Ex.: *omo*).

### Discussão

Conceitos trabalhados:

* Indexação de listas
* Strings são listas

### Indexação de listas

Em python, assim como C e Java, o primeiro índice de uma string é `0`. Assim, quando queremos pegar um elemento da lista:
```
>>> a = [5, 10, 15, 20, 25]
>>> a[3]
20
>>> a[0]
5
```

Também conseguimos pegar sublistas entre 2 índices:
```
>>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:4]
[10, 15, 20]
>>> a[6:]
[35, 40]
>>> a[:-1]
[5, 10, 15, 20, 25, 30, 35]
```

O primeiro número é o "índice inicial", o último número é o "índice final" (não incluso na lista final)

### Strings são listas

Como strings são listas, podemos fazer com strings tudo que podemos fazer com listas. Por exemplo, podemos iterar por elas:

```python
string = "exemplo"
for c in string:
    print("Uma letra: " + c)
```

Terá como resultado:
```
Uma letra: e
Uma letra: x
Uma letra: e
Uma letra: m
Uma letra: p
Uma letra: l
Uma letra: o
```

Também podemos obter substrings:
```
>>> string = "exemplo"
>>> s = string[0:5]
>>> s
exemp
```
---

# Exercício 3 - Pedra, Papel, Tesoura

Faça um jogo de *pedra, papel ou tesoura* de dois jogadores. (Dica: peça as jogadas ao usuário - usando `input` - compare-os, imprima uma mensagem parabenizando o vencedor e pergunte ao usuário se quer continuar jogando).

Lembrando as regras:

* Pedra vence tesoura
* Tesoura vence papel
* Papel vence pedra

### Discussão

Conceitos trabalhados:

* Laços `while`
* Laços infinitos
* Cláusulas `break`

### Laços `while`

Um laço `while` em Python possui comportamento similar ao de outras linguagens:

```python
a = 5
while (a > 0):
    print(a)
    a -= 1
```

A saída seria:

```
5
4
3
2
1
```

Uma forma útil de usar um laço `while` seria verificar se a entrada do usuário está correta, por exemplo:
```python
quit = input('Digite "sair" para sair: ')
while quit != "sair":
    quit = input('Digite "sair" para sair: ')
```

### Laços infinitos

Um laço infinito é um laço que nunca para. Ou seja, a condição no início do laço `while` vai ser sempre verdadeira.

Por exemplo:
```python
i = 5
while > 0:
    print("Dentro do laço")
```

O que ocorre aqui é que o laço vai imprimir a frase "dentro do laço" para sempre. Se executar esse trecho de código, você vai precisar matar o programa, para pará-lo. Neste caso em particular, provavelmente seria um erro de programação, mas por vezes você quer mesmo executar um laço infinito.


### Cláusulas `break`

Uma cláusula `break` pára a execução de um laço antes que a condição original seja atendida. É importante notar que seu uso é bastante controverso, mas por vezes pode ser útil.
Por exemplo:

```python
while True:
    command = input("Digite um comando: ")
    if command == "quit":
        break
    else:
        print("Você digitou " + command)
```

Neste caso o `break` é usado para sair do "laço infinito".

---
## Exercício 4 - Jogo da adivinhação

Gere um número aleatório entre 1 e 9 (incluindo 1 e 9).
Peça ao usuário para adivinhar o número, e então diga se a tentativa foi menor, maior ou correta. (Dica: lembre-se de usar o `input` dos exercícios anteriores). Mantenha o jogo executando até que o usuário digite "sair".

### Discussão

Conceitos trabalhados:

* Pacotes
* Números aleatórios
* Entrada do usuário


### Números aleatórios (e pacotes)

Para este exercício, vamos precisar implrtar um pacote de biblioteca (também chamados de módulos). Vamos usar aqui o pacote `random`, que gera números aleatórios.

Para importar um pacote, no início do arquivo, fazemos:
```python
import random
```

Assim, trazemos para o *namespace* todas classes, métodos e funções do pacote `random`. Para gerar um número inteiro aleatório, fazemos:
```python
a = random.randint(2, 6)
```

Aqui, a variável `a` conterá um número aleatório entre 2 e 6 (incluindo 2 e 6). A documentação do pacote `random` está [aqui](https://docs.python.org/3.11/library/random.html).

---
## Exercício 5 - Remover duplicatas

Escreva um programa que receba uma lista e retorne uma nova lista que contenha todos os elementos da primeira lista, menos as duplicadas.

### Discussão
Conceitos:

* Conjuntos

---
### Conjuntos

Em matemática, um conjunto é uma coleção de elementos na qual nenhum elemento é duplicado. É útil porque se você sabe que seus dados estão armazenados em um conjunto, você tem a garantia de possuir elementos sem repetição.

#### Características dos conjuntos
* Não são ordenados. Ou seja, não há um "primeiro elemento", ou um "último elemento". Há apenas "elementos". Não é possível pedir a um conjunto por seu "próximo elemento".
* Não há elementos repetidos em um conjunto.
* É possível converter entre conjuntos e listas facilmente.

#### Conjuntos em python
Em python, fazemos um conjunto com a palavra-chave `set()` ou definindo uma lista entre chaves `{}`.

```python
names = set()
names.add("Michele")
names.add("Ronaldo")
names.add("Michele")
print(names)
```
A saída será:
```
set(['Michele', 'Ronaldo'])
```

É possível fazer com um conjunto quase tudo que se pode fazer com uma lista (exceto coisas como pedir pelo "terceiro elemento"). Pode-se converder de lista para conjunto (e vice-versa) facilmente:

```python
names = ["Michele", "Ronaldo", "Sara", "Michele"]
names = set(names)
names = list(names)
print(names)
```

E o resultado:
```
['Michele', 'Robin', 'Sara']
```

---
## Exercício 6 - Gerador de Senhas

Escreva um gerador de senhas em python. Seja criativo com a forma de gerar senhas - senhas fortes possuem uma mistura de letras minúsculas, maiúsculas, números e símbolos. As senhas devem ser aleatórioas, gerando uma nova senha a cada vez que o usuário executar o programa.

### Discussão

Não há tópicos novos, mas você vai precisar usar o 
[módulo random do python](https://docs.python.org/3.11/library/random.html).

---
## Exercício 7 - Leitura de arquivos

Dado um arquivo `.txt` que contem uma lista de nomes, conte quantas vezes cada nome aparece no arquivo e imprima os resultados na tela. Um arquivo `nomes.txt` é fornecido junto a esse repositório.

### Discussão

Conceitos:

* Leitura de um arquivo
* Dicionários

### Leitura de arquivos

Ler um arquivo é simples. Vamos tratar aqui, mas você pode sempre acompanhar a [documentação oficial](https://docs.python.org/3.11/tutorial/inputoutput.html#reading-and-writing-files).

Para ler um arquivo, são dois passos:
1. Abrir o arquivo para leitura
1. Ler.

Para abrir o arquivo para leitura, basta fazer:
```python
with open("arquivo.txt", "r", encoding="utf-8") as open_file:
    all_text = open_file.read()
```

Repare que a flag `r` significa *read* (ler). O código acima carrega todo o `open_file` na variável `all_text`. Isso significa que agora todo o arquivo está em `all_text` como uma grande *string* que pode ser manipulada em python usando métodos de string comuns.

Também podemos ler arquivos linha-a-linha:
```python
with open("arquivo.txt", "r", encoding="utf-8") as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = open_file.readline()
```

Ao invés de `print(line)` pode-se fazer qualquer coisa com a linha do texto. 

### Dicionários

Dicionários são tipos de dado em python que permitem associar dois outros tipos de dados. Mais detalhes na [documentação oficial](https://docs.python.org/3.3/tutorial/datastructures.html#dictionaries).

```python
student_scores = {"Marcelo": 100, "Pedro": 75, "Apolo": 80, "Agamenon": 90}
```

As strings, ou qualquer coisa que esteja à esquerda do sinal de `:`, são as chaves (*keys*). Para acessar os valores (*values*), o que vem depois do sinal `:`, usamos a chave entre colchetes `[]`:

```python
marcelo_score = student_scores["Marcelo"]
```

É possível motificar as notas e armazená-las novamente no dicionário:

```python
marcelo_score = student_scores["Marcelo"]
marcelo_score += 100
student_scores["Marcelo"] = marcelo_score
```

É possível acessar as chaves e os valores como listas:

```python
all_scores = student_scores.values()
all_names = student_scores.keys()
```

É possível usar a palavra-chave `in`, assim como nas listas, para iterar por itens (chave, valor) em um dicionário:

```python
for pair in student_scores.items():
    print(pair)
```

Esse trecho imprime os pares de chave valor como `(Marcelo, 100)`.

Note que os dicionários não são ordenados, então iterar por eles não garante nenhuma ordem de chave/valor.

---
## Exercício 8

Use os pacotes `BeautifulSoup` e `requests` para imprimir uma lista de todos os títulos de artigos do [New York Times](http://www.nytimes.com/).

### Discussão

Conceitos:

* Bibliotecas
* `requests`
* `BeautifulSoup`

### Bibliotecas

Python possui diversas bibliotecas que não vêm com a *standard lib* do Python (por exemplo a biliboteca `random` que usamos anteriormente). Essas bibliotecas estendem a funcionalidade padrão do python.

De maneira geral, para usar uma biblioteca, é preciso ter em mente:
1. É preciso instalá-las.
1. É preciso importá-las com o comando `import`. Por exemplo `import requests`.
1. É importante ler a documentação, para saber exatamente como utilizar a biblioteca.

### Requests

A biblioteca [requests](https://docs.python-requests.org/en/latest/) é bastante útil, por facilitar a execução de requisições HTTP no Python.
Ela faz requisições HTTP e busca as informações através dos diversos verbos HTTP. Neste exercício, o objetivo é buscar o conteúdo de uma página HTML.

Na [documentação](https://docs.python-requests.org/en/latest/) você pode encontrar mais detalhes, conforme for necessário. De forma geral, o que você precisa para buscar o HTML de uma página é:

```python
import requests
url = "http://github.com"
r = requests.get(url)
raw_html = r.text
```

Agora, na variável `raw_html` temos o HTML da página como uma string. Fazer o *parse* dessa string pode ser feito manualmente, ou usando uma outra biblioteca (a seguir).

### BeautifulSoup

Para resolver o problema do *parse* (ler, interpretar) a string HTML obtida com o `requests`, usamos a biblioteca [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/).

A biblioteca nos fornece uma estrutura hierárquica do HTML. Como `BeautifulSoup` interpreta o HTML, podemos fazer algo como: "forneça todos os itens com uma tag `<p>`" ou "encontre o elemento 'pai' do elemento `<title>`.

O código pode ser algo assim:
```python
from bs4 import BeautifulSoup

# o código do request para obter raw_html

soup = BeautifulSoup(raw_html)
title = soup.find("title").string
```

Este código retornaria o título da página, por exemplo. É possível fazer diversas coisas com o `BeautifulSoup`. Explore a documentação para entender como resolver o exercício.

---

## Exercício 9 - Gravar um arquivo

Pegue o código do exercício anterior e ao invés de imprimir os resultados na tela, escreva-os em um arquivo txt. No seu código você
pode deixar o nome do arquivo *hard-coded*.

### Discussão

Conceitos:
* Escrever em um arquivo
* Detalhes a atentar

### Escrever em um arquivo

Escrever em um arquivo em python é relativamente fácil. Existem várias opções para fazê-lo, mas utilizaremos aqui a forma mais simples, escrevendo em um arquivo texto. O código é algo assim:

```python
with open("arquivo.txt", "w") as open_file:
    open_file.write("Uma string a gravar no arquivo")
```

Uma forma alternativa de escrever o mesmo código seria algo como:
```python
open_file = open("arquivo.txt", "w")
open_file.write("Uma string a gravar no arquivo")
open_file.close()
```

A primeira forma é considerada uma prática melhor, mas em alguns casos, a segunda forma pode parecer mais clara.

A primeira linha cria um bloco de código que abre o arquivo e atribui o *file handle* para a variável `open_file`. O comando `open` recebe o nome do arquivo e a flag com o tipo `w` aqui, indicando escrita (*write*). 

Quando abrimos um arquivo, neste caso, o python procurará o arquivo no mesmo diretório em que o script se encontra. Caso deseje gravá-lo em outro lugar, deve passar o caminho completo para o tal.

Quando o programa termina o bloco `with` (quando termina a identação), o `close` é automaticamente chamado, gravando o arquivo no disco, sem que precisemos fazê-lo explicitamente.

O `write` é simples. Passando uma string para ele, ele escreverá essa string no final do arquivo.

### Detalhes a atentar

O exercício é simples, mas devemos atentar para alguns detalhes:
1. Certifique-se de sempre fechar o arquivo. Usando o `with` garante que isso acontecerá.
1. Abrir um arquivo com `w` vai sobrescrever (apagar) qualquer arquivo que já exista com o mesmo nome.
1. Você pode escrever *qualquer* tipo de objeto para qualquer arquivo usando python, desde que você especifique o formato correto. A forma mais simples é gravar strings em um arquivo texto. Mas lembre-se de que você deve converter números ou objetos em strings antes de poder gravá-los em um arquivo.