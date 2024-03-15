capacidade_atual, aumento_percentual = map(int, input().split())
aumento_teraflops = capacidade_atual * aumento_percentual / 100 

nova_capacidade = capacidade_atual + aumento_teraflops 

print(int(nova_capacidade)) 