# Code-OTSU-Thresholding
Demonstração do método de OTSU em código 

Histograma

![image](https://user-images.githubusercontent.com/32250409/63232609-d40db480-c1ff-11e9-88d5-87225aa53ecd.png)

Para este histograma temos:
```
quantidade = [8,7,2,6,9,4]
intensidade = [0,1,2,3,4,5]
```
Agora Calculamos o Wa

![image](https://user-images.githubusercontent.com/32250409/63232656-6f068e80-c200-11e9-84af-ab5d33028e10.png)

```
############### Wa Calculo ###############
somaWA = 0
for i in intensidade[:l]:
  somaWA += quantidade[i]
  print( "            | ",i, "-->", quantidade[i], "|" )

wa = somaWA / sum(quantidade)
wa = round(wa,4)
print()
print("Wa = ", wa)
```
