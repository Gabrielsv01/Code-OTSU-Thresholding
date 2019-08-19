
quantidade = [8,7,2,6,9,4]
intensidade = [0,1,2,3,4,5]
l = 0

print( "Intensidade | -------- | Quantidade" )

############### Wa Calculo ###############
somaWA = 0
for i in intensidade[:l]:
  somaWA += quantidade[i]
  print( "            | ",i, "-->", quantidade[i], "|" )

wa = somaWA / sum(quantidade)
wa = round(wa,4)
print()
print("Wa = ", wa)

############### Mi Calculo ###############
somaUA = 0

for i in intensidade[:l]:
  somaUA += (i * quantidade[i])

if (l != 0):
  miA = somaUA / sum(quantidade[:l])
else:
  miA = 0

miA = round(miA,4)
print("Mi A = ", miA)

############### Sigma A Calculo ###############

somaSigmaA = 0
for i in intensidade[:l]:
  somaSigmaA += ((i - miA)**2) * quantidade[i]

if (l != 0):
  sigmaA = somaSigmaA / sum(quantidade[:l])
else:
  sigmaA = 0

sigmaA = round(sigmaA,4)
print("Sigma A = ", sigmaA)
print()

############### Wb Calculo ###############
print( "Intensidade | -------- | Quantidade" )

somaWB = 0
for i in intensidade[l:]:
  somaWB += quantidade[i]
  print( "            | ",i, "-->", quantidade[i], "|" )

print()
wb = somaWB / sum(quantidade)
wb = round(wb,4)
print("Wb = ", wb)
############### Mi B Caluculo #############

somaUB = 0
for i in intensidade[l:]:
  somaUB += (i * quantidade[i])

miB = somaUB / sum(quantidade[l:])
miB = round(miB,4)
print("Mi B = ", miB)

############### Sigma B Calculo ###############

somaSigmaB = 0
for i in intensidade[l:]:
  somaSigmaB += ((i - miB)**2) * quantidade[i]

sigmaB = somaSigmaB / sum(quantidade[l:])
sigmaB = round(sigmaB,4)
print("Sigma B = ", sigmaB)
print("\n------------------\n")

############### Sigma W ###############
sigmaW = (wa*sigmaA) + (wb * sigmaB)
sigmaW = round(sigmaW,4)

print("L = ", l)
print("Sigma W = ", sigmaW)
