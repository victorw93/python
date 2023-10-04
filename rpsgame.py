import random

def play():
    user = input("Qual a sua escolha? 'r' para pedra, 'p' para papel, 't' para tesoura \n")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return f'Empate! A escolha foi {computer}'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return f'Venceu! A escolha foi {computer}'
    
    return f'Perdeu! A escolha foi {computer}'


def is_win(player, opponent):
    # se retornar true o player ganha
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    

print(play())