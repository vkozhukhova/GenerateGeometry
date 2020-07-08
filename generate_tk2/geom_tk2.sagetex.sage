## -*- encoding: utf-8 -*-
## This file (geom_tk2.sagetex.sage) was *autogenerated* from geom_tk2.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('geom_tk2', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = 85
_st_.blockbegin()
try:
 # 1) Вычислить площадь треугольника и найти длину высоты из вершины ??.
 A = vector([randint(-7, 7) for i in range(2)])
 B = vector([randint(-4, 4) for i in range(2)])
 C = vector([randint(-10, 10) for i in range(2)])
 AB = B-A
 AC = C-A
 BC = C-B
 crossm = matrix([AB, AC])
 while det(crossm)==0 :
       C = vector([randint(-10, 10) for i in range(2)])
       AC = C-A
       BC = C-B
       crossm = matrix([AB, AC])
 SABC= abs(det(crossm)/2)
 ch1 = randint(1,3)
 if ch1 == 1 :
    vertex = r"A"
    hABC = 2*SABC/BC.norm()
 else :
    if ch1 == 2 :
       vertex = r"B"
       hABC = 2*SABC/AC.norm()
    else :
       vertex = r"C"
       hABC = 2*SABC/AB.norm()
 Gtriag=points([A,B,C], size=50, color='black', figsize=4)+line((A,B), color='black', figsize=4)+line((A,C), color='black', figsize=4)+line((B,C), color='black', figsize=4)
 # 2) Центр масс треугольника и углы
 angA = arccos(AB.dot_product(AC)/(AB.norm()*AC.norm()))
 angB = arccos((-AB).dot_product(BC)/(AB.norm()*BC.norm()))
 angC = arccos((-AC).dot_product(-BC)/(AC.norm()*BC.norm()))
 angres = []
 if (angA==angB) or (angA==angC) or (angB==angC):
    angres.append(r"равнобедренный")
 else :
    angres.append(r"не равнобедренный")
 if (angA==pi/2) or (angB==pi/2) or (angC==pi/2):
    angres.append(r"прямоугольный")
 else :
    angres.append(r"не прямоугольный")
 # 3) Длина биссектрисы при вершине ...
 if ch1 == 1 : # вершина A
    lambd = AB.norm()/AC.norm()
    D = vector([(B[0]+lambd*C[0])/(1+lambd), (B[1]+lambd*C[1])/(1+lambd)])
    AD = D-A
    biss = AD.norm()
 else :
    if ch1 == 2 : # вершина B
       lambd = BC.norm()/AB.norm()
       D = vector([(C[0]+lambd*A[0])/(1+lambd), (C[1]+lambd*A[1])/(1+lambd)])
       BD = D-B
       biss = BD.norm()
    else : # вершина C
       lambd = AC.norm()/BC.norm()
       D = vector([(A[0]+lambd*B[0])/(1+lambd), (A[1]+lambd*B[1])/(1+lambd)])
       CD = D-C
       biss = CD.norm()
 # 4) Перенос  и поворот системы координат
 S = FiniteEnumeratedSet([pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2,5*pi/3,7*pi/4,11*pi/6, arctan(3/4), arctan(5/12), arctan(4/3), arctan(12/5), arctan(8/15), arctan(15/8), arctan(7/24), arctan(24/7)])
 ang = S.random_element()
 rotm = Matrix([[cos(ang), -sin(ang)],[sin(ang),cos(ang)]])
 if ch1 == 1 :
    An = vector([0,0])
    Bn = rotm.inverse()*AB
    Cn = rotm.inverse()*AC
 else :
    if ch1 == 2 :
       Bn = vector([0,0])
       An = rotm.inverse()*(-AB)
       Cn = rotm.inverse()*BC
    else :
       Cn = vector([0,0])
       An = rotm.inverse()*(-AC)
       Bn = rotm.inverse()*(-BC)
 # Точки в ПСК и ДПСК
 def Polar_to_Cart(polar_v) :
     return vector([polar_v[0]*cos(polar_v[1]), polar_v[0]*sin(polar_v[1])])
 def Cart_to_Polar(cart_v):
     return vector([sqrt(cart_v[0]^2 + cart_v[1]^2), atan2(cart_v[1],cart_v[0])])
 M1 = vector([randint(-7, 7) for i in range(2)])
 M2 = vector([randint(-4, 4) for i in range(2)])
 M3 = vector([randint(-10, 10) for i in range(2)])
 S1 = FiniteEnumeratedSet([pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2,5*pi/3,7*pi/4,11*pi/6,pi,-pi/6, -pi/4, -pi/3, -pi/2, -2*pi/3, -3*pi/4, -5*pi/6, -7*pi/6, -5*pi/4, -4*pi/3, -3*pi/2,-5*pi/3,-7*pi/4,-11*pi/6,-pi])
 M4 = vector([randint(1, 10),S1.random_element()])
 M5 = vector([randint(1, 10),S1.random_element()])
 M6 = vector([randint(1, 10),S1.random_element()])
 M4C=Polar_to_Cart(M4)
 M5C=Polar_to_Cart(M5)
 M6C=Polar_to_Cart(M6)
 P2 = {'M1':M1,'M2':M2,'M3':M3,'M4':M4C,'M5':M5C,'M6':M6C}
 ymin=min(M1[1],M2[1],M3[1],M4C[1],M5C[1],M6C[1])
 ymax=max(M1[1],M2[1],M3[1],M4C[1],M5C[1],M6C[1])
 if sign(ymin) == sign(ymax):
    if sign(ymin)==-1:
         ymax=abs(ymax)
    else :
         if sign(ymin)==0:
            ymin=-5
            ymax=5
         else:
            ymin=-ymin
 xmin=min(M1[0],M2[0],M3[0],M4C[0],M5C[0],M6C[0])
 xmax=max(M1[0],M2[0],M3[0],M4C[0],M5C[0],M6C[0])
 if sign(xmin) == sign(xmax):
   if sign(xmin)==-1:
      xmax=abs(xmax)
   else :
      if sign(xmin)==0:
         xmin=-5
         xmax=5
      else:
         xmin=-xmin
 G1 = points(P2.values(), size = 50, color = 'black', aspect_ratio=1, ymin=1.5*ymin, ymax=1.5*ymax, figsize=4, xmin=1.5*xmin,xmax=1.5*xmax)
 i=0
 for p in P2.keys():
     G1 += text('  %s'%p,P2.values()[i],horizontal_alignment='left',color='black')
     i=i+1
 var('x,y,xc,yc,a,b')
 eleqn=((x-xc)^2/a^2+(y-yc)^2/b^2-1==0)# уравнение эллипса в канон виде
 # первое задание - окружность в центром (0,0)
 a=sqrt(randint(1,10)^2/randint(1,10)^2)
 b=a
 xc=0
 yc=0
 el2=eleqn(xc=xc,yc=yc,a=a,b=b).expand()
 el3=el2.multiply_both_sides(el2.left().denominator()) # конечное уравнение окружности
 # окружность в ПСК
 var('rho, varphi')
 el4=el3.subs(x=rho*cos(varphi), y=rho*sin(varphi)).simplify_trig()
 # график окружности
 G2=implicit_plot(el3, (x,-1.5*a,1.5*a),(y,-1.5*a,1.5*a), axes='true', figsize=4, color = 'black')
 # второе задание - окружность со смещенным центром
 a=sqrt(randint(1,10)^2/randint(1,10)^2)# положительное число
 ch2=randint(1,2)
 if ch2 ==1 :
    a=a
 else :
    a=-a # можно и отрицательное
 b=a
 ch3 = randint(1,2) # сдвиг по X или по Y
 if ch3 ==1 :
    xc=a
    yc=0
 else :
    xc=0
    yc=a
 el5=eleqn(xc=xc,yc=yc,a=a,b=b).expand()
 el6=el5.multiply_both_sides(el5.left().denominator()).simplify() # конечное уравнение окружности
 # окружность в ПСК
 el7=el6.subs(x=rho*cos(varphi), y=rho*sin(varphi)).simplify_trig()
 el8=el7.divide_both_sides(rho).expand().solve(rho)[0]
 # график окружности
 if xc==0:
    if yc<0:
       ymax = abs(a/2)
       ymin = 2*a
       xmin=a
       xmax=-a
    else:
       ymin = -a/2
       ymax = 2*a
       xmin=-a
       xmax=a
 else:
    if xc<0:
       xmax = abs(a/2)
       xmin = 2*a
       ymin=a
       ymax=-a
    else:
       xmin = -a/2
       xmax = 2*a
       ymin=-a
       ymax=a
 G3=implicit_plot(el6, (x,1.5*xmin,1.5*xmax),(y,1.5*ymin,1.5*ymax), axes='true', figsize=4, color = 'black')
 G3+=point((xc,yc), size=25, color='black')
 G3 += text('  (%s,%s)'%(xc,yc),(xc+xc/3,yc-yc/3),horizontal_alignment='left',color='black')
 # лемнискаты
 a=sqrt(randint(1,10)^2/randint(1,10)^2)
 ch4=randint(1,2)
 if ch4 == 1:
    lemeqn = (x^2+y^2)^2==2*a^2*(x^2-y^2)
 else:
    lemeqn = (x^2+y^2)^2==4*a^2*x*y
 lem2=lemeqn.subs(x=rho*cos(varphi), y=rho*sin(varphi)).simplify_trig().divide_both_sides(rho^2).expand().reduce_trig()
 G4=implicit_plot(lemeqn, (x,-1.5*a,1.5*a),(y,-1.5*a,1.5*a), axes='true', figsize=4, color = 'black')
 # спирали
 a=sqrt(randint(1,10)^2/randint(1,10)^2)
 ch5=randint(1,2)
 if ch5 ==1 :
    a=a
 else :
    a=-a # можно и отрицательное
 spireqn=rho==a*varphi
 spi2=(spireqn.subs(rho=sqrt(x^2+y^2), varphi=arctan(y/x)))^2
 G5=polar_plot(a*x, (x,0,2*pi), color='black', axes='true', figsize=3)
 # кардиоида
 a=randint(1,10)
 ch6=randint(1,4)
 if ch6 ==1 :
    cardeqn = rho==a*(1-sin(varphi))
 else :
    if ch6==2:
       cardeqn = rho==a*(1+sin(varphi))
    else:
       if ch6==3:
          cardeqn = rho==a*(1-cos(varphi))
       else:
          cardeqn = rho==a*(1+cos(varphi))
 card2=cardeqn.subs(rho=sqrt(x^2+y^2), varphi=arctan(y/x)).factor().canonicalize_radical().multiply_both_sides(sqrt(x^2 + y^2))
 if card2.right().coefficient(x,1)==0:
      card3=card2.subtract_from_both_sides(card2.right().coefficient(y,1)*y)
 else:
      card3=card2.subtract_from_both_sides(card2.right().coefficient(x,1)*x)
 card3=card3^2
 G6=polar_plot(cardeqn.right(), (varphi,0,2*pi), color='black', axes='true', figsize=3)
 # полярная роза
 Spolar=FiniteEnumeratedSet([5/2,-5/2,3/2,-3/2,7/2,-7/2,2,3,4,5,6,7,-2,-3,-4,-5,-6,-7,-2/3,2/3])
 a=Spolar.random_element()
 b=randint(2,4)
 ch7=randint(1,2)
 if ch7==1:
    roseeqn=rho==a*cos(b*varphi)
 else:
    roseeqn=rho==a*sin(b*varphi)
 ros2=((roseeqn.subs(rho=sqrt(x^2+y^2), varphi=arctan(y/x)).simplify_trig().canonicalize_radical())^2).factor()
 ros3=ros2.multiply_both_sides(ros2.right().denominator())
 G7=polar_plot(roseeqn.right(), (varphi,0,2*pi), color='black', axes='true', figsize=3)
except:
 _st_.goboom(313)
_st_.blockend()
try:
 _st_.current_tex_line = 328
 _st_.inline(0, latex(A))
except:
 _st_.goboom(328)
try:
 _st_.current_tex_line = 328
 _st_.inline(1, latex(B))
except:
 _st_.goboom(328)
try:
 _st_.current_tex_line = 328
 _st_.inline(2, latex(C))
except:
 _st_.goboom(328)
try:
 _st_.current_tex_line = 328
 _st_.inline(3, vertex)
except:
 _st_.goboom(328)
try:
 _st_.current_tex_line = 360
 _st_.inline(4, vertex)
except:
 _st_.goboom(360)
try:
 _st_.current_tex_line = 360
 _st_.inline(5, vertex)
except:
 _st_.goboom(360)
try:
 _st_.current_tex_line = 360
 _st_.inline(6, latex(ang))
except:
 _st_.goboom(360)
try:
 _st_.current_tex_line = 379
 _st_.inline(7, latex(M1))
except:
 _st_.goboom(379)
try:
 _st_.current_tex_line = 379
 _st_.inline(8, latex(M2))
except:
 _st_.goboom(379)
try:
 _st_.current_tex_line = 379
 _st_.inline(9, latex(M3))
except:
 _st_.goboom(379)
try:
 _st_.current_tex_line = 379
 _st_.inline(10, latex(M4))
except:
 _st_.goboom(379)
try:
 _st_.current_tex_line = 379
 _st_.inline(11, latex(M5))
except:
 _st_.goboom(379)
try:
 _st_.current_tex_line = 379
 _st_.inline(12, latex(M6))
except:
 _st_.goboom(379)
try:
 _st_.current_tex_line = 396
 _st_.inline(13, latex(el3))
except:
 _st_.goboom(396)
try:
 _st_.current_tex_line = 396
 _st_.inline(14, latex(el6))
except:
 _st_.goboom(396)
try:
 _st_.current_tex_line = 396
 _st_.inline(15, latex(lemeqn))
except:
 _st_.goboom(396)
try:
 _st_.current_tex_line = 412
 _st_.inline(16, latex(spireqn))
except:
 _st_.goboom(412)
try:
 _st_.current_tex_line = 412
 _st_.inline(17, latex(cardeqn))
except:
 _st_.goboom(412)
try:
 _st_.current_tex_line = 412
 _st_.inline(18, latex(roseeqn))
except:
 _st_.goboom(412)
try:
 _st_.current_tex_line = 424
 _st_.plot(0, format='notprovided', _p_=Gtriag)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(19, latex(SABC))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(20, latex(hABC))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(21, latex((A+B+C)/3))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(22, latex((B+C)/2-A))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(23, latex((A+C)/2-B))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(24, latex((B+A)/2-C))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(25, latex(angA))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(26, latex(round(angA*180/pi)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(27, latex(angB))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(28, latex(round(angB*180/pi)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(29, latex(angC))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(30, latex(round(angC*180/pi)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(31, angres[0])
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(32, angres[1])
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(33, vertex)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(34, latex(biss))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(35, latex(n(biss, digits=4)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(36, latex(An))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(37, latex(Bn))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(38, latex(Cn))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(39, latex(Cart_to_Polar(M1)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(40, latex(Cart_to_Polar(M2)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(41, latex(Cart_to_Polar(M3)))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(42, latex(M4C))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(43, latex(M5C))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(44, latex(M6C))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(1, format='notprovided', _p_=G1)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(45, latex(el4.solve(rho)[1]))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(46, latex(el8))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(47, latex(lem2))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(2, format='notprovided', _p_=G2)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(3, format='notprovided', _p_=G3)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(4, format='notprovided', _p_=G4)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(48, latex(spi2))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(49, latex(card3))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.inline(50, latex(ros3))
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(5, format='notprovided', _p_=G5)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(6, format='notprovided', _p_=G6)
except:
 _st_.goboom(424)
try:
 _st_.current_tex_line = 424
 _st_.plot(7, format='notprovided', _p_=G7)
except:
 _st_.goboom(424)
_st_.endofdoc()
