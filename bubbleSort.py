Lista=[7,-1,4,3,12,8,-2,0,2,-4]
fim=len(Lista) #quantidade de elementos da lista
while fim>1: #verificar se a variável fim é mais que 1, pois precisamos de pelo menos dois elementos na lista
  trocou=False # para indicar que o elemento foi trocado de posição
  x=0 # é usado como índice
  while x<(fim-1):# isso faz com que a condição de saída (x) seja anterior ao último elemento 
    if Lista[x]>Lista[x+1]: #comparação onde x é a posição atual e o próximo elemento x+1
      trocou=True
      var_temp=Lista[x]
      Lista[x]=Lista[x+1]
      Lista[x+1]=var_temp
      
    x=x+1
  if not trocou:
    break
  fim=fim-1

for elemento in Lista:
  #print(elemento)
  print(elemento, end=" ")
