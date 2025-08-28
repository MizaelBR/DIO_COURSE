### BANK SYSTEM
### GOAL ###
### MAKE A BANK SYSTEM WITH THE OPERATIONS:
### WITHDRAW; DEPOSIT; VIEW STATEMENT.

### WITHDRAW:
### O SISTEMA DEVE PERMITIR REALIZAR 3 SAQUES DIARIOS COM LIMITE MÁXIMO DE 500 REAIS POR SAQUE.
### CASO O USUÁRIO NÃO TENHA SALDO EM CONTA, O SISTEMA DEVE EXIBIR UMA MENSAGEM INFORMANDO QUE NÃO SERÁ POSSÍVEL SACAR O DINEHRIO POR FALTA DE SALDO.
### TODOS OS SAQUES DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO.

### DEPOSIT:
### TODOS OS DEPOSITOS DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO

### VIEW STATEMENT:
### LISTAR TODOS OS DEPOSITOS E SAQUES REALIZADOS NA CONTA.
### NO FINAL DA LISTA EXIBIR O SALDO ATUAL.
### SE O EXTRATO ESTIVER EM BRANCO EXIBIR: NÃO FORAM REALIZADAS MOVIMENTAÇÕES.
### FORAMTO DA MOEDA: R$ 1000.00

from os import *
from time import *

menu = '''
 MY BANK SYSTEM
 [1] DEPOSIT
 [2] WITHDRAW
 [3] VIEW
 [0] EXIT
'''

valor = 0
extrato = []
sacar = 0

def clear():
    system('cls')

while True:
    clear()
    system('color 70')

    print(menu)
    try:
        chooce = int(input("CHOOCE: "))

        if chooce == 0:
            break
        
        if chooce == 1:
            clear()
            system('color 27')
            print(f"\n SALDO R${valor:.2f}")
            print(' [0] CANCELAR\n')
            num1 = int(input(" VALOR A DEPOSITAR: "))
            if num1 == 0:
                continue
            else:
                valor += num1
                extrato.append(num1)

        elif chooce == 2:
            clear()
            system('color 47')
            print(f"\n SALDO R${valor:.2f}")
            print(' [0] CANCELAR\n')
            if valor <=0:
                print(" NÃO TEM SALDO PARA SAQUE")
                sleep(5)
            else:
                if sacar == 3:
                    print(" NÃO PODE MAIS SACAR HOJE")
                    sleep(5)
                else:
                    sacar += 1
                    num2 = int(input(" VALOR A SACAR: "))
                    if num2 == 0:
                        continue
                    else:
                        valor -= num2
                        extrato.append(num2*(-1))
        elif chooce == 3:
            clear()
            system('color 57')
            print(' EXTRATO:')
            for i in extrato:
                if i > 0:
                    print(f' DEPOSITO: R${i:.2f}\n')
                elif i < 0:
                    print(f' SAQUE: R${i:.2f}\n')
            if len(extrato) == 0:
                print(' << SEM EXTRATO >>')
            print(f' SALDO ATUAL: R${valor:.2f}')
            sleep(10)
        
    except:
        clear()
        continue

system('color 07')
clear()
    

