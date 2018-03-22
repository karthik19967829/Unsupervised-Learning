# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:08:17 2017

@author: Karthik
"""

import random
cie1=[]
ass1=[]
cie2=[]
ass2=[]
cie3=[]
ass3=[]
cie4=[]
ass4=[]
cie5=[]
ass5=[]
for x in range(2000):
    #cie1.append(random.randint(15,30))
    ciem1=random.randint(12,30)
    cie1.append(ciem1)
    if ciem1>20:
        ass1.append(random.randint(15,20))
    else:
        ass1.append(random.randint(10,20))
    if ciem1+5>30:    
        ciem2=(random.randint(ciem1-3,30))
    else:    
        ciem2=(random.randint(ciem1-3,ciem1+5))
    if ciem2>20:
        ass2.append(random.randint(15,20))
    else:
        ass2.append(random.randint(10,20))
    cie2.append(ciem2)
    if ciem2+5>30:    
        ciem3=(random.randint(ciem2-3,30))
    else:    
        ciem3=(random.randint(ciem2-3,ciem2+5))
    if ciem3>20:
        ass3.append(random.randint(15,20))
    else:
        ass3.append(random.randint(10,20))
    cie3.append(ciem3)
    if ciem3+5>30:    
        ciem4=(random.randint(ciem3-3,30))
    else:    
        ciem4=(random.randint(ciem3-3,ciem3+5))
    if ciem4>20:
        ass4.append(random.randint(15,20))
    else:
        ass4.append(random.randint(10,20))
    cie4.append(ciem4)
    if ciem4+5>30:    
        ciem5=(random.randint(ciem4-3,30))
    else:    
        ciem5=(random.randint(ciem4-3,ciem4+5))
    if ciem5>20:
        ass5.append(random.randint(15,20))
    else:
        ass5.append(random.randint(10,20))
    cie5.append(ciem5)
    """cie3.append(random.randint(15,30))
    ass3.append(random.randint(10,20))
    cie4.append(random.randint(15,30))
    ass4.append(random.randint(10,20))
    cie5.append(random.randint(15,30))
    ass5.append(random.randint(10,20))"""

cgpa1=[]
sgpa1=[]
cgpa2=[]
sgpa2=[]
cgpa3=[]
sgpa3=[]
cgpa4=[]
sgpa4=[]
cgpa5=[]
sgpa5=[]
fin1=[]
fin2=[]
fin3=[]
fin4=[]
fin5=[]
for i in range(2000):
    fin1.append(cie1[i]+ass1[i])
    fin2.append(cie2[i]+ass2[i])
    fin3.append(cie3[i]+ass3[i])
    fin4.append(cie4[i]+ass4[i])
    fin5.append(cie5[i]+ass5[i])
for i in fin1:
    if i>45:
        cgpa1.append(10)
        sgpa1.append(10)
    elif i<45 and i>40:
        cgpa1.append(9)
        sgpa1.append(9)
    elif i<40 and i>35:
        cgpa1.append(8)
        sgpa1.append(8)
    elif i<35 and i>30:
        cgpa1.append(7)
        sgpa1.append(7)
    else:
        cgpa1.append(6)
        sgpa1.append(6)
for i in fin2:
    if i>45:
        cgpa2.append(10)
        sgpa2.append(10)
    elif i<45 and i>40:
        cgpa2.append(9)
        sgpa2.append(9)
    elif i<40 and i>35:
        cgpa2.append(8)
        sgpa2.append(8)
    elif i<35 and i>30:
        cgpa2.append(7)
        sgpa2.append(7)
    else:
        cgpa2.append(6)
        sgpa2.append(6)
for i in fin3:
    if i>45:
        cgpa3.append(10)
        sgpa3.append(10)
    elif i<45 and i>40:
        cgpa3.append(9)
        sgpa3.append(9)
    elif i<40 and i>35:
        cgpa3.append(8)
        sgpa3.append(8)
    elif i<35 and i>30:
        cgpa3.append(7)
        sgpa3.append(7)
    else:
        cgpa3.append(6)
        sgpa3.append(6)
for i in fin4:
    if i>45:
        cgpa4.append(10)
        sgpa4.append(10)
    elif i<45 and i>40:
        cgpa4.append(9)
        sgpa4.append(9)
    elif i<40 and i>35:
        cgpa4.append(8)
        sgpa4.append(8)
    elif i<35 and i>30:
        cgpa4.append(7)
        sgpa4.append(7)
    else:
        cgpa4.append(6)
        sgpa4.append(6)
for i in fin5:
    if i>45:
        cgpa5.append(10)
        sgpa5.append(10)
    elif i<45 and i>40:
        cgpa5.append(9)
        sgpa5.append(9)
    elif i<40 and i>35:
        cgpa5.append(8)
        sgpa5.append(8)
    elif i<35 and i>30:
        cgpa5.append(7)
        sgpa5.append(7)
    else:
        cgpa5.append(6)
        sgpa5.append(6)
#print("Printing cie1",cie1)
#print("Printing ass1",ass1)
#print("Printing final1",fin1)
#print("Printing cgpa1",cgpa1)
#print("Printing sgpa1",sgpa1)

#print("Printing cie2",cie2)
#print("Prinitng ass2",ass2)
#print("Printing final2",fin2)
#print("Printing cgpa2",cgpa2)
#print("Prinitng sgpa2",sgpa2)
''',('MathRate',math_ratings),
        ('CultRatings',cult_ratings),('sport_ratings',sport_rating),
        ('Research',research_rating)])'''
#print("Printing cie3",cie3)
#print("Printing ass3",ass3)
#print("Printing final3",fin3)
#print("priniting cgpa3",cgpa3)
#print("Printing sgpa3",sgpa3)

#print("Printing cie4",cie4)
#print("Printing ass4",ass4)
#print("Printing final4",fin4)
#print("Printing cgpa 4",cgpa4)
#print("Printgin sgpa4",sgpa4)

#print("Printing cie5",cie5)
#print("Printing ass5",ass5)
#print("Printing final5",fin5)
#print("Printing cgpa5",cgpa5)
#print("Prinintg sgpa5",sgpa5)

cgpa=[]
sgpa=[]
for i in range(2000):
    cgpa.append((cgpa1[i]+cgpa2[i]+cgpa3[i]+cgpa4[i]+cgpa5[i])/5)
for i in range(2000):
    sgpa.append(random.uniform(int(cgpa[i]),int(cgpa[i])+0.5))
#print(cgpa)
#print(sgpa)
math_ratings=[]
cult_ratings=[]
sport_rating=[]
research_rating=[]
for j in range(2000): 
    math_ratings.append(random.randint(5,10))
    cult_ratings.append(random.randint(5,10))
    sport_rating.append(random.randint(5,10))
    research_rating.append(random.randint(5,10))
import pandas as pd
from collections import OrderedDict
data=OrderedDict([('CIE1',cie1),('ASSIGN1',ass1),
        ('CIE2',cie2),('ASSIGN2',ass2),
        ('CIE3',cie3),('ASSIGN3',ass3),
        ('CIE4',cie4),('ASSIGN4',ass4),
        ('CIE5',cie5),('ASSIGN5',ass5),
        ('CGPA',cgpa),('SGPA',sgpa),('MathRate',math_ratings),
        ('CulturalRatings',cult_ratings),('SportRate',sport_rating),
        ('ResearchRatings',research_rating)])
        
df = pd.DataFrame.from_dict(data)
df.to_csv('example1.csv', index=False)
