# Code-OTSU-Thresholding
Demonstração do método de OTSU em código 

Formula Geral

![image](https://user-images.githubusercontent.com/32250409/63232740-26030a00-c201-11e9-88a6-973be1ffb626.png)


Histograma

![image](https://user-images.githubusercontent.com/32250409/63232609-d40db480-c1ff-11e9-88d5-87225aa53ecd.png)

Para este histograma temos:

```
quantidade = [8,7,2,6,9,4]
intensidade = [0,1,2,3,4,5]
```
Agora Calculando o Wa

![image](https://user-images.githubusercontent.com/32250409/63232656-6f068e80-c200-11e9-84af-ab5d33028e10.png)

```
############### Wa Calculo ###############
somaWA = 0
for i in intensidade[:l]:
  somaWA += quantidade[i]

wa = somaWA / sum(quantidade)
wa = round(wa,4)
```
Logo em seguida, calculando o Mi A

![image](https://user-images.githubusercontent.com/32250409/63232695-d3295280-c200-11e9-85fc-b0418461c5ec.png)

```
############### Mi A Calculo ###############
somaUA = 0
for i in intensidade[:l]:
  somaUA += (i * quantidade[i])

if (l != 0):
  miA = somaUA / sum(quantidade[:l])
else:
  miA = 0
  
miA = round(miA,4)
```
Calculo do Sigma A

![image](https://user-images.githubusercontent.com/32250409/63232921-aaa25800-c202-11e9-9097-cbb2eec5cef1.png)

```
############### Sigma A Calculo ###############
somaSigmaA = 0
for i in intensidade[:l]:
  somaSigmaA += ((i - miA)**2) * quantidade[i]

if (l != 0):
  sigmaA = somaSigmaA / sum(quantidade[:l])
else:
  sigmaA = 0

sigmaA = round(sigmaA,4)
```


Agora Calculando o Wb

OBS: Perceba que só mudei a forma de pegar os dados ( antes [:l], agora [l:] )

![image](https://user-images.githubusercontent.com/32250409/63232753-4763f600-c201-11e9-8c70-a0ee6eaa7c28.png)

```
############### Wb Calculo ###############
somaWB = 0
for i in intensidade[l:]:
  somaWB += quantidade[i]

wb = somaWB / sum(quantidade)
wb = round(wb,4)
```
Agora calculando o Mi B

![image](https://user-images.githubusercontent.com/32250409/63232798-b17c9b00-c201-11e9-8a29-e5e31606eb35.png)

```
############### Mi B Caluculo #############
somaUB = 0
for i in intensidade[l:]:
  somaUB += (i * quantidade[i])

miB = somaUB / sum(quantidade[l:])
miB = round(miB,4)
```

Calculando o Sigma B

![image](https://user-images.githubusercontent.com/32250409/63232866-4089b300-c202-11e9-99b9-d8bcb7953b0c.png)

```
############### Sigma B Calculo ###############
somaSigmaB = 0
for i in intensidade[l:]:
  somaSigmaB += ((i - miB)**2) * quantidade[i]

sigmaB = somaSigmaB / sum(quantidade[l:])
sigmaB = round(sigmaB,4)
```

Agora com os valores calculados, podemos encontrar o Sigma W

![image](https://user-images.githubusercontent.com/32250409/63232740-26030a00-c201-11e9-88a6-973be1ffb626.png)

```
############### Sigma W ###############
sigmaW = (wa*sigmaA) + (wb * sigmaB)
sigmaW = round(sigmaW,4)

print("L = ", l)
print("Sigma W = ", sigmaW)
```


