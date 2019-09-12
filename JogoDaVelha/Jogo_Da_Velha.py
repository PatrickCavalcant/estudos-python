L1C1 = []
L1C2 = []
L1C3 = []
L2C1 = []
L2C2 = []
L2C3 = []
L3C1 = []
L3C2 = []
L3C3 = []
X = "X"
O = "O"
X1 = 0
X2 = 0
X3 = 0
X4 = 0
X5 = 0
X6 = 0
X7 = 0
X8 = 0
X9 = 0
O1 = 0
O2 = 0
O3 = 0
O4 = 0
O5 = 0
O6 = 0
ERRO = 0
O8 = 0
O9 = 0
A = ""
B = ""
D = ""
E = ""
F = ""
G = ""
H = ""
P = ""
R = ""

while (((X1 + X2 + X3 < 3) and (O1 + O2 + O3 < 3)) and ((X4 + X5 + X6 <3) and (O4 + O5 + O6 < 3)) and((X7 + X8 + X9 < 3) and (ERRO + O8 + O9 < 3)) and(( X1 + X5 + X9 < 3) and (O1 + O5 + O9 < 3))and((X7+ X5+ X3 < 3 )and(ERRO + O5 + O3 < 3))and((X1 + X4 + X7 < 3) and (O1+O4+ERRO <3)) and ((X2 + X5 + X8 < 3)and(O2 + O5 + O8<3))and((X3 + X6 + X9 < 3) and (O3 +O6 + O9 <3) )):
   print ("")
   print ("|-----------------|")
   print ("   " ,A,"   "  ,B, "   " ,D)
   print ("|-----|-----|-----|")
   print ("   " ,E,"   "  ,F, "   " ,G)
   print ("|-----|-----|-----|")
   print ("   " ,H,"   "  ,P, "   " , R )
   print ("|-----------------|")
   print ("")
   print ("0 Para Sair ")


   L = int(input("Digite o número da linha: "))
   

   if (L == 1):
      C = int(input("Dígite o número da coluna: "))
      
      if(C ==1):
         print("")
         XO = input("Digite X ou O: ")
         L1C1.append(XO)
         
         if (L1C1[0] == X):
            X1 += 1
            A = X
         
         elif (L1C1[0] == O):
            O1 += 1
            A = O
                
         else:
            print("SOMENTE X OU O.")
            break
       
      elif(C==2):
         print("")
         XO = input("Digite X ou O: ")
         L1C2.append (XO)
         
         if (L1C2[0] == X):
            X2 += 1
            B = X
            
         elif (L1C2[0] == O):
            O2 += 1
            B = O
            
         else:
            print("SOMENTE X OU O.")
            break
            
      elif(C==3):
         print("")
         XO = input("Digite X ou O: ")
         L1C3.append(XO)
         
         if (L1C3[0] == X):
            X3 += 1
            D = X
            
         elif (L1C3[0] == O):
            O3 += 1
            D = O
            
         else:
            print("SOMENTE X OU O.")
            break
      else:
         print("VALOR INVALIDO.")
         
   elif (L == 2):
      C2 = int(input("Dígite o número da coluna: "))
      
      if(C2 ==1):
         print("")
         XO = input("Digite X ou O: ")
         L2C1.append(XO)
         
         if (L2C1[0] == X):
            X4 += 1
            E = X
            
         elif (L2C1[0] == O):
            O4 += 1
            E = O
                
         else:
            print("SOMENTE X OU O.")
            break
     
      elif(C2==2):
         print("")
         XO = input("Digite X ou O: ")
         L2C2.append(XO)
         
         if (L2C2[0] == X):
            X5 += 1
            F = X
            
         elif (L2C2[0] == O):
            O5 += 1
            F = O
                
         else:
            print("SOMENTE X OU O. ")
            break
         
      elif(C2 == 3):
         print("")
         XO = input("Digite X ou O: ")
         L2C3.append(XO)
         
         if (L2C3[0] == X):
            X6 += 1
            G = X
            
         elif (L2C3[0] == O):
            O6 += 1
            G = O
                
         else:
            print("SOMENTE X OU O.")
            break
         
      else:
         print("VALOR INVALIDO.")
         
   elif (L == 3):
      C3 = int(input("Dígite o número da coluna: "))
      
      if(C3 == 1):
         print("")
         XO = input("Digite X ou O: ")
         L3C1.append(XO)
         
         if (L3C1[0] == X):
            X7 += 1
            H = X
            
         elif (L3C1[0] == O):
            ERRO += 1
            H = O
            
         else:
            print("SOMENTE X OU O.")
            break
     
      elif(C3 == 2):
         print("")
         XO = input("Digite X ou O: ")
         L3C2.append(XO)
         
         if (L3C2[0] == X):
            X8 += 1
            P = X
            
         elif (L3C2[0] == O):
            O8 += 1
            P = O
               
         else:
            print("SOMENTE X OU O.")
            break
         
         
      elif(C3 == 3):
         print("")
         XO = input("Digite X ou O: ")
         L3C3.append(XO)
         
         if (L3C3[0] == X):
            X9 += 1
            R = X
           
            
         elif (L3C3[0] == O):
            O9 += 1
            R = O
                
         else:
            print("SOMENTE X OU O.")
            break
         
      else:
         print("VALOR INVALIDO.")
               
   elif L == 0 :
      
      break
   
                     
   else:
      print("VALOR INVALIDO.")
print("")
print("Parabéns!!!")
print("Você Ganhou!!!")
  
      
  
