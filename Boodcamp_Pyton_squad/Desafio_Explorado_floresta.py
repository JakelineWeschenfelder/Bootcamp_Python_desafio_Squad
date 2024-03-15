quantidade_passos = int(input())
if quantidade_passos <= 0: 
    print("Nenhum passo dado na floresta.") 
else:
  
    for passo in range(1, quantidade_passos + 1): 
      if passo == 1:
        print(f"Explorador: {passo} passo") 
      else: 
        print(f"Explorador: {passo} passos")  

