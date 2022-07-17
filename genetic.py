#최대적합도 올리기, 함수, 반복 간략화, 변이 확률



#genetic algorithm
import random
import matplotlib.pyplot as plt
x1=[]
y1=[]
gs=int(input("개체의 유전자수(15):"))
k=round(gs/3)
roop=int(input("반복 횟수 입력(100):"))
M1=int(input("변이 1 확률(10):"))
M2=int(input("변이 2 확률(2):"))
print()



#Initialize
a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i=[],[],[],[],[],[],[],[],[],[]
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    a_i.append(1)
  else:
    a_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    b_i.append(1)
  else:
    b_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    c_i.append(1)
  else:
    c_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    d_i.append(1)
  else:
    d_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    e_i.append(1)
  else:
    e_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    f_i.append(1)
  else:
    f_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    g_i.append(1)
  else:
    g_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    h_i.append(1)
  else:
    h_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    i_i.append(1)
  else:
    i_i.append(0)
for i in range(0,gs):#
  i_p=random.randint(1,5)
  if i_p==1:
    j_i.append(1)
  else:
    j_i.append(0)




#Loop
for i in range(1,roop):



#output(print,graph)
  suit=(sum(a_i)+sum(b_i)+sum(c_i)+sum(d_i)+sum(e_i)+sum(f_i)+sum(g_i)+sum(h_i)+sum(i_i)+sum(j_i))
  print(i,"generation:",a_i  ,"suitabilty:",suit/10)#
  print()
  plt.axhline(gs,c="r",linewidth=0.7)#
  x=i
  y=(suit/10)#
  x1.append(i)
  y1.append(y)
  plt.plot(x1,y1,c="b",linewidth=0.5)
  plt.scatter(x,y,s=2,c="b")
  plt.xlabel("generation")
  plt.ylabel("suitability")
  plt.pause(0.1)
  plt.ylim([0, gs+gs/10])  #
  plt.title("Generation Algorithm")
  if suit/10==gs:#
    print("최대 적합도에 도달하였습니다")#
    break

  
  
#Selection
  all_gen=[a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i]
  all_gen.sort()
  a_p=all_gen[-1]
  b_p=all_gen[-2]
  c_p=all_gen[-3]
  d_p=all_gen[-4]
  p_g=[all_gen[-1],all_gen[-2],all_gen[-3],all_gen[-4]]



#Crossover and Replace
  a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i=[],[],[],[],[],[],[],[],[],[]
  
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      a_i.append(0)
    else:
      a_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      b_i.append(0)
    else:
      b_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      c_i.append(0)
    else:
      c_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      d_i.append(0)
    else:
      d_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      e_i.append(0)
    else:
      e_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      f_i.append(0)
    else:
      f_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      g_i.append(0)
    else:
      g_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      h_i.append(0)
    else:
      h_i.append(1)
  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      i_i.append(0)
    else:
      i_i.append(1)

  p=p_g[random.randint(0,3)]
  q=p_g[random.randint(0,3)]
  for i in range(0,gs):#
    if p[i]+q[i]==0:
      j_i.append(0)
    else:
      j_i.append(1)



#Mutation
  if M1==0:
    continue
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      a_i[random.randint(0,gs-1)]=random.randint(0,1) #
  if m_p==2:
    a_i.reverse()
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      b_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      c_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      d_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      e_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      f_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      g_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      h_i[random.randint(0,gs-1)]=random.randint(0,1)#
  
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      i_i[random.randint(0,gs-1)]=random.randint(0,1)#
  m_p=random.randint(1,round(100/M1))
  if m_p==1:
    for i in range(random.randint(1,k)):
      j_i[random.randint(0,gs-1)]=random.randint(0,1)#
  
  
  if M2==0:
    continue
  m_p1=random.randint(1,round(100/M2))
  m_p2=random.randint(1,10)
  if m_p1==1:
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(b_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(c_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(d_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(e_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(f_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(g_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(h_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(i_i)
    if m_p2==random.randint(1,10) or random.randint(1,10):
      random.shuffle(j_i)
    
  
    
#result
plt.show()



#a_i ~ j_i : 개체의 유전정보
#loop : 반복 설정
#suit : 개체 유전자의 합 (suit/n : 적합도)
#all_gen: 개체 유전정보의 모임
#a_p ~ d_p : 선택된 부모들
#p_g : 부모 유전정보의 모임