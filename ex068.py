import random
count = 0
print(":)"*15)
print('Vamos jogar par ou impar')
print(":)"*15)
while True:
    n = int(input('Digite um número(0 - 10):'))
    pi = str(input('Par ou Ímpar:')).lower()
    NComp = random.randrange(1,10)
    soma = NComp+n
    if pi == 'par' and soma%2==0:
        print("-"*30)
        print(f'Parabéns, você venceu. Eu escolhi o número {NComp} e a soma deu {soma}. Vamos jogar denovo!')
        print("-"*30)
        count+=1
    elif pi == 'par' and soma%2!=0: 
        print("-"*30)
        print(f'Eu escolhi o número {NComp} e a soma deu {soma}, logo, eu venci.')
        print("-"*30)
        break
    elif pi == 'impar' and soma%2!=0:
        print("-"*30)
        print(f'Parabéns, você venceu. Eu escolhi o número {NComp} e a soma deu {soma}. Vamos jogar denovo!')
        print("-"*30)
        count+=1
    elif pi == 'impar' and soma%2==0:
        print("-"*30)
        print(f'Eu escolhi o número {NComp} e a soma deu {soma}, logo, eu venci.')
        print("-"*30) 
        break
if count == 0:
    
    print('Você é bem ruim hein? Teve 0 vitórias')
    print("-"*30)
else:
    
    print(f'Você perdeu, porém teve um total de {count} vitórias consecutivas')
    print("-"*30)