#URI 1001
"""A = int (input("Digite NUM 1: "))
B = int (input("Digite NUM 2: "))

X = (A + B)

print("X = ", X)
"""


#OPERADORES
"""a=5
b=15
c=20

print("a == b AND b > c : ", a==b and b>c)
print("a < b OR b > c : ", a<b or b>c)
print("NOT a == b : ", not a==b)"""


#ESTRUTURA DE DECISAO
"""idade=int (input("Digite a idade da pessoa: "))
if idade > 18:
    print("\nmaior idade")"""


#TESTE 2
"""a = input("Informe um valor para a variável A: ")
b = input("Informe um valor para a variável B: ")

if (a>b):
    aux=a;
    a=b;
    b=aux;
print("O valor da variável A agora é : ", a);
print("O valor da variável B agora é : ", b);"""


#TESTE 3
"""idade=int (input("Digite a idade da pessoa: "))
if idade > 18:
    print("\nMaior idade")
else:
    print("\nMenor idade")"""


#IF/ELIF/ELSE
#ELIF = se existir mais de uma condição alternativa que precise ser verificada, utilizamos a condição elif, pois ela avalia as expressões intermediárias antes do comando else
"""idade=int (input("Digite a idade da pessoa: "))
if idade > 18:
    print("\nMaior Idade");
elif idade > 16:
    print("\nInfanto Juvenil");
else:
    print("\nMenor Idade");"""



#REPETIÇÂO FOR + RANGE
    #RANGE = Uma vez que n é menor do que 10 (condição), o comando print é executado
"""for n in range(10):
    print(n)"""

#RANGE DEFINIDO COM VALOR INICIAL E FINAL = RANGE(NUM_IN, NUM_FIN)
"""for n in range(5, 16):
    print(n)"""

#RANGE DEFINIDO COM VALOR INICIAL, FINAL E DECREMENTO = RANGE(NUM_IN, NUM_FIN)
"""for n in range(16, 0, -1):
    print(n)"""

#WHILE = executa um determinado conjunto de instruções, enquanto a condição verificada no início permanecer verdadeira
"""x=1;

while x<=15:
    print(x);
    x=x+1"""


#FUNÇOES
"""def lernotas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n


def resultado(n1,n2):
    media=(n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a=lernotas()
b=lernotas()
resultado(a,b)"""


#MANIPULACAO DE ARQUIVOS
    #OPEN()
        """Sua sintaxe é: 
        
        arquivo = open(‘arquivo.txt’, ‘w’)
        
        necessita de dois parâmetros: 
        primeiramente o nome do arquivo e, depois, o modo como estamos abrindo esse arquivo."""

    #WRITE()
        """A função write() é utilizada para gravar

informações em um arquivo existente.


Sua síntaxe é:

arquivo.write (‘Curso Python n’)

arquivo.write (‘Aula Prática’)"""

    #READ()
        """A função read() realiza a leitura

de todo conteúdo do arquivo.


Sua sintaxe é:

leitura=open(‘arquivo.txt, ‘r’)

print leitura.read()

leitura.close()"""

   
    #MODOS DE LEITURA DO ARQUIVO

   
    """r	Abre o arquivo somente para leitura.
O arquivo deve já existir.

r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir.
A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.

w	Abre o arquivo somente para escrita, no início do arquivo.
Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.

w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.

a	Abre o arquivo para escrita no final do arquivo.
Não apaga o conteúdo preexistente.

a+	Abre o arquivo para escrita no final do arquivo e leitura."""






