from scipy import linalg
import numpy as np
from numpy import loadtxt
import math
from Dtreefunc import *

def first_infoCal():  
    f=open("irisds\output.txt","r")
    X=f.readlines()
    N=3 #row
    M=4 #col
    sepL = np.zeros(3)
    sepLCI=[[0 for i in range(M)] for j in range(N)]
    sepW = np.zeros(3)
    sepWCI=[[0 for i in range(M)] for j in range(N)]
    petL = np.zeros(3) 
    petLCI=[[0 for i in range(M)] for j in range(N)]
    petW = np.zeros(3)
    petWCI=[[0 for i in range(M)] for j in range(N)]

    species = np.zeros(3)

    for i in range(0,150):
        
        if(X[i].count("sl_lower")==1):
            sepL[0]+=1
            if((X[i].count('sl_lower')==1)) and (X[i].count('Iris-setosa')==1):
                sepLCI[0][0]+=1
            elif((X[i].count('sl_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[0][1]+=1
            elif((X[i].count('sl_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[0][2]+=1
        elif(X[i].count("sl_mid")==1): 
            sepL[1]+=1
            if((X[i].count('sl_mid')==1)) and (X[i].count('Iris-setosa')==1):
                sepLCI[1][0]+=1
            elif((X[i].count('sl_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[1][1]+=1
            elif((X[i].count('sl_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[1][2]+=1
        elif(X[i].count("sl_higher")==1): 
            sepL[2]+=1
            if((X[i].count('sl_higher')==1)) and (X[i].count('Iris-setosa')==1):
                sepLCI[2][0]+=1
            elif((X[i].count('sl_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[2][1]+=1
            elif((X[i].count('sl_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[2][2]+=1

        if(X[i].count("sw_lower")==1):
            sepW[0]+=1
            if((X[i].count('sw_lower')==1)) and (X[i].count('Iris-setosa')==1):
                sepWCI[0][0]+=1
            elif((X[i].count('sw_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[0][1]+=1
            elif((X[i].count('sw_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[0][2]+=1
        elif(X[i].count("sw_mid")==1): 
            sepW[1]+=1
            if((X[i].count('sw_mid')==1)) and (X[i].count('Iris-setosa')==1):
                sepWCI[1][0]+=1
            elif((X[i].count('sw_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[1][1]+=1
            elif((X[i].count('sw_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[1][2]+=1
        elif(X[i].count("sw_higher")==1): 
            sepW[2]+=1
            if((X[i].count('sw_higher')==1)) and (X[i].count('Iris-setosa')==1):
                sepWCI[2][0]+=1
            elif((X[i].count('sw_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[2][1]+=1
            elif((X[i].count('sw_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[2][2]+=1

        if(X[i].count("pl_lower")==1):
            petL[0]+=1
            if((X[i].count('pl_lower')==1)) and (X[i].count('Iris-setosa')==1):
                petLCI[0][0]+=1
            elif((X[i].count('pl_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                petLCI[0][1]+=1
            elif((X[i].count('pl_lower')==1)) and (X[i].count('Iris-virginica')==1):
                petLCI[0][2]+=1
        elif(X[i].count("pl_mid")==1): 
            petL[1]+=1
            if((X[i].count('pl_mid')==1)) and (X[i].count('Iris-setosa')==1):
                petLCI[1][0]+=1
            elif((X[i].count('pl_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                petLCI[1][1]+=1
            elif((X[i].count('pl_mid')==1)) and (X[i].count('Iris-virginica')==1):
                petLCI[1][2]+=1
        elif(X[i].count("pl_higher")==1): 
            petL[2]+=1
            if((X[i].count('pl_higher')==1)) and (X[i].count('Iris-setosa')==1):
                petLCI[2][0]+=1
            elif((X[i].count('pl_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                petLCI[2][1]+=1
            elif((X[i].count('pl_higher')==1)) and (X[i].count('Iris-virginica')==1):
                petLCI[2][2]+=1

        if(X[i].count("pw_lower")==1):
            petW[0]+=1
            if((X[i].count('pw_lower')==1)) and (X[i].count('Iris-setosa')==1):
                petWCI[0][0]+=1
            elif((X[i].count('pw_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                petWCI[0][1]+=1
            elif((X[i].count('pw_lower')==1)) and (X[i].count('Iris-virginica')==1):
                petWCI[0][2]+=1
        elif(X[i].count("pw_mid")==1): 
            petW[1]+=1
            if((X[i].count('pw_mid')==1)) and (X[i].count('Iris-setosa')==1):
                petWCI[1][0]+=1
            elif((X[i].count('pw_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                petWCI[1][1]+=1
            elif((X[i].count('pw_mid')==1)) and (X[i].count('Iris-virginica')==1):
                petWCI[1][2]+=1
        elif(X[i].count("pw_higher")==1): 
            petW[2]+=1
            if((X[i].count('pw_higher')==1)) and (X[i].count('Iris-setosa')==1):
                petWCI[2][0]+=1
            elif((X[i].count('pw_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                petWCI[2][1]+=1
            elif((X[i].count('pw_higher')==1)) and (X[i].count('Iris-virginica')==1):
                petWCI[2][2]+=1

        if (X[i].count('Iris-setosa')==1):
            species[0]+=1
        elif(X[i].count('Iris-versicolor')==1):
            species[1]+=1
        elif(X[i].count('Iris-virginica')==1):
            species[2]+=1

    info = np.zeros(4)
    InD=entropy(species[0],species[1],species[2])

    sepLCI[0][3]=entropy(sepLCI[0][0],sepLCI[0][1],sepLCI[0][2]) 
    sepLCI[1][3]=entropy(sepLCI[1][0],sepLCI[1][1],sepLCI[1][2])
    sepLCI[2][3]=entropy(sepLCI[2][0],sepLCI[2][1],sepLCI[2][2])

    sepWCI[0][3]=entropy(sepWCI[0][0],sepWCI[0][1],sepWCI[0][2]) 
    sepWCI[1][3]=entropy(sepWCI[1][0],sepWCI[1][1],sepWCI[1][2])
    sepWCI[2][3]=entropy(sepWCI[2][0],sepWCI[2][1],sepWCI[2][2])

    petLCI[0][3]=entropy(petLCI[0][0],petLCI[0][1],petLCI[0][2]) 
    petLCI[1][3]=entropy(petLCI[1][0],petLCI[1][1],petLCI[1][2])
    petLCI[2][3]=entropy(petLCI[2][0],petLCI[2][1],petLCI[2][2])

    petWCI[0][3]=entropy(petWCI[0][0],petWCI[0][1],petWCI[0][2]) 
    petWCI[1][3]=entropy(petWCI[1][0],petWCI[1][1],petWCI[1][2])
    petWCI[2][3]=entropy(petWCI[2][0],petWCI[2][1],petWCI[2][2])

    Info_sepL = inforD(sepL,[sepLCI[0][3],sepLCI[1][3],sepLCI[2][3]])
    Info_sepW = inforD(sepW,[sepWCI[0][3],sepWCI[1][3],sepWCI[2][3]])
    Info_petL = inforD(petL,[petLCI[0][3],petLCI[1][3],petLCI[2][3]])
    Info_petW = inforD(petW,[petWCI[0][3],petWCI[1][3],petWCI[2][3]])

    print("\n***Gain results of all dataset***")
    gainSepL=InD-Info_sepL
    print("Gain (sepal length) is %f"% gainSepL)
    gainSepW=InD-Info_sepW
    print("Gain (sepal width) is %f"% gainSepW)
    gainPetL=InD-Info_petL
    print("Gain (petal length) is %f"% gainPetL)
    gainPetW=InD-Info_petW
    print("Gain (petal width) is %f"% gainPetW)

    Result_All=[gainSepL,gainSepW,gainPetL,gainPetW]
    max_gain=max(Result_All)
    pos=np.argmax(Result_All)
    print("max gain of attb is %f" % max_gain,"position is",pos)

    print("\n\nsepLCI")
    print(sepLCI)
    print("\n\nsepWCI")
    print(sepWCI)
    print("\n\npetLCI")
    print(petLCI)
    print("\n\npetWCI")
    print(petWCI)

def second_infoCal():  
    f=open("irisds\output2.txt","r")
    X=f.readlines()
    N=3 #row
    M=3 #col
    sepL = np.zeros(3)
    sepLCI=[[0 for i in range(M)] for j in range(N)]
    sepW = np.zeros(3)
    sepWCI=[[0 for i in range(M)] for j in range(N)]
    petW = np.zeros(3)
    petWCI=[[0 for i in range(M)] for j in range(N)]

    species = np.zeros(2)

    for i in range(0,100):
        
        if(X[i].count("sl_lower")==1):
            sepL[0]+=1
            if((X[i].count('sl_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[0][0]+=1
            elif((X[i].count('sl_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[0][1]+=1
        elif(X[i].count("sl_mid")==1): 
            sepL[1]+=1
            if((X[i].count('sl_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[1][0]+=1
            elif((X[i].count('sl_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[1][1]+=1
        elif(X[i].count("sl_higher")==1): 
            sepL[2]+=1
            if((X[i].count('sl_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[2][0]+=1
            elif((X[i].count('sl_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[2][1]+=1

        if(X[i].count("sw_lower")==1):
            sepW[0]+=1
            if((X[i].count('sw_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[0][0]+=1
            elif((X[i].count('sw_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[0][1]+=1
        elif(X[i].count("sw_mid")==1): 
            sepW[1]+=1
            if((X[i].count('sw_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[1][0]+=1
            elif((X[i].count('sw_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[1][1]+=1
        elif(X[i].count("sw_higher")==1): 
            sepW[2]+=1
            if((X[i].count('sw_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[2][0]+=1
            elif((X[i].count('sw_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[2][1]+=1

        if(X[i].count("pw_lower")==1):
            petW[0]+=1
            if((X[i].count('pw_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                petWCI[0][0]+=1
            elif((X[i].count('pw_lower')==1)) and (X[i].count('Iris-virginica')==1):
                petWCI[0][1]+=1
        elif(X[i].count("pw_mid")==1): 
            petW[1]+=1
            if((X[i].count('pw_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                petWCI[1][0]+=1
            elif((X[i].count('pw_mid')==1)) and (X[i].count('Iris-virginica')==1):
                petWCI[1][1]+=1
        elif(X[i].count("pw_higher")==1): 
            petW[2]+=1
            if((X[i].count('pw_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                petWCI[2][0]+=1
            elif((X[i].count('pw_higher')==1)) and (X[i].count('Iris-virginica')==1):
                petWCI[2][1]+=1

        if (X[i].count('Iris-versicolor')==1):
            species[0]+=1
        elif(X[i].count('Iris-virginica')==1):
            species[1]+=1

    InD=entropytwo(species[0],species[1])

    sepLCI[0][2]=entropytwo(sepLCI[0][0],sepLCI[0][1]) 
    sepLCI[1][2]=entropytwo(sepLCI[1][0],sepLCI[1][1])
    sepLCI[2][2]=entropytwo(sepLCI[2][0],sepLCI[2][1])

    sepWCI[0][2]=entropytwo(sepWCI[0][0],sepWCI[0][1]) 
    sepWCI[1][2]=entropytwo(sepWCI[1][0],sepWCI[1][1])
    sepWCI[2][2]=entropytwo(sepWCI[2][0],sepWCI[2][1])

    petWCI[0][2]=entropytwo(petWCI[0][0],petWCI[0][1]) 
    petWCI[1][2]=entropytwo(petWCI[1][0],petWCI[1][1])
    petWCI[2][2]=entropytwo(petWCI[2][0],petWCI[2][1])

    Info_sepL = inforD(sepL,[sepLCI[0][2],sepLCI[1][2],sepLCI[2][2]])
    Info_sepW = inforD(sepW,[sepWCI[0][2],sepWCI[1][2],sepWCI[2][2]])
    Info_petW = inforD(petW,[petWCI[0][2],petWCI[1][2],petWCI[2][2]])

    print("\n***Gain results of all dataset***")
    gainSepL=InD-Info_sepL
    print("Gain (sepal length) is %f"% gainSepL)
    gainSepW=InD-Info_sepW
    print("Gain (sepal width) is %f"% gainSepW)
    gainPetW=InD-Info_petW
    print("Gain (petal width) is %f"% gainPetW)

    Result_All=[gainSepL,gainSepW,gainPetW]
    max_gain=max(Result_All)
    pos=np.argmax(Result_All)
    print("max gain of attb is %f" % max_gain,"position is",pos)

    print("\n\nsepLCI")
    print(sepLCI)
    print("\n\nsepWCI")
    print(sepWCI)
    print("\n\npetWCI")
    print(petWCI)

def third_infoCal():  
    f=open("irisds\output3.txt","r")
    X=f.readlines()
    N=3 #row
    M=3 #col
    sepL = np.zeros(3)
    sepLCI=[[0 for i in range(M)] for j in range(N)]
    sepW = np.zeros(3)
    sepWCI=[[0 for i in range(M)] for j in range(N)]

    species = np.zeros(2)

    for i in range(0,100):
        
        if(X[i].count("sl_lower")==1):
            sepL[0]+=1
            if((X[i].count('sl_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[0][0]+=1
            elif((X[i].count('sl_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[0][1]+=1
        elif(X[i].count("sl_mid")==1): 
            sepL[1]+=1
            if((X[i].count('sl_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[1][0]+=1
            elif((X[i].count('sl_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[1][1]+=1
        elif(X[i].count("sl_higher")==1): 
            sepL[2]+=1
            if((X[i].count('sl_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[2][0]+=1
            elif((X[i].count('sl_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[2][1]+=1

        if(X[i].count("sw_lower")==1):
            sepW[0]+=1
            if((X[i].count('sw_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[0][0]+=1
            elif((X[i].count('sw_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[0][1]+=1
        elif(X[i].count("sw_mid")==1): 
            sepW[1]+=1
            if((X[i].count('sw_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[1][0]+=1
            elif((X[i].count('sw_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[1][1]+=1
        elif(X[i].count("sw_higher")==1): 
            sepW[2]+=1
            if((X[i].count('sw_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepWCI[2][0]+=1
            elif((X[i].count('sw_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepWCI[2][1]+=1

        if (X[i].count('Iris-versicolor')==1):
            species[0]+=1
        elif(X[i].count('Iris-virginica')==1):
            species[1]+=1

    InD=entropytwo(species[0],species[1])

    sepLCI[0][2]=entropytwo(sepLCI[0][0],sepLCI[0][1]) 
    sepLCI[1][2]=entropytwo(sepLCI[1][0],sepLCI[1][1])
    sepLCI[2][2]=entropytwo(sepLCI[2][0],sepLCI[2][1])

    sepWCI[0][2]=entropytwo(sepWCI[0][0],sepWCI[0][1]) 
    sepWCI[1][2]=entropytwo(sepWCI[1][0],sepWCI[1][1])
    sepWCI[2][2]=entropytwo(sepWCI[2][0],sepWCI[2][1])

    Info_sepL = inforD(sepL,[sepLCI[0][2],sepLCI[1][2],sepLCI[2][2]])
    Info_sepW = inforD(sepW,[sepWCI[0][2],sepWCI[1][2],sepWCI[2][2]])

    print("\n***Gain results of all dataset***")
    gainSepL=InD-Info_sepL
    print("Gain (sepal length) is %f"% gainSepL)
    gainSepW=InD-Info_sepW
    print("Gain (sepal width) is %f"% gainSepW)

    Result_All=[gainSepL,gainSepW]
    max_gain=max(Result_All)
    pos=np.argmax(Result_All)
    print("max gain of attb is %f" % max_gain,"position is",pos)

    print("\n\nsepLCI")
    print(sepLCI)
    print("\n\nsepWCI")
    print(sepWCI)

def fourth_infoCal():  
    f=open("irisds\output4.txt","r")
    X=f.readlines()
    N=3 #row
    M=3 #col
    sepL = np.zeros(3)
    sepLCI=[[0 for i in range(M)] for j in range(N)]

    species = np.zeros(2)

    for i in range(0,100):
        
        if(X[i].count("sl_lower")==1):
            sepL[0]+=1
            if((X[i].count('sl_lower')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[0][0]+=1
            elif((X[i].count('sl_lower')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[0][1]+=1
        elif(X[i].count("sl_mid")==1): 
            sepL[1]+=1
            if((X[i].count('sl_mid')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[1][0]+=1
            elif((X[i].count('sl_mid')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[1][1]+=1
        elif(X[i].count("sl_higher")==1): 
            sepL[2]+=1
            if((X[i].count('sl_higher')==1)) and (X[i].count('Iris-versicolor')==1):
                sepLCI[2][0]+=1
            elif((X[i].count('sl_higher')==1)) and (X[i].count('Iris-virginica')==1):
                sepLCI[2][1]+=1

        if (X[i].count('Iris-versicolor')==1):
            species[0]+=1
        elif(X[i].count('Iris-virginica')==1):
            species[1]+=1

    InD=entropytwo(species[0],species[1])

    sepLCI[0][2]=entropytwo(sepLCI[0][0],sepLCI[0][1]) 
    sepLCI[1][2]=entropytwo(sepLCI[1][0],sepLCI[1][1])
    sepLCI[2][2]=entropytwo(sepLCI[2][0],sepLCI[2][1])

    Info_sepL = inforD(sepL,[sepLCI[0][2],sepLCI[1][2],sepLCI[2][2]])

    print("\n***Gain results of all dataset***")
    gainSepL=InD-Info_sepL
    print("Gain (sepal length) is %f"% gainSepL)

    Result_All=[gainSepL]
    max_gain=max(Result_All)
    pos=np.argmax(Result_All)
    print("max gain of attb is %f" % max_gain,"position is",pos)

    print("\n\nsepLCI")
    print(sepLCI)


# first_infoCal()
# second_infoCal()
# third_infoCal()
fourth_infoCal()


