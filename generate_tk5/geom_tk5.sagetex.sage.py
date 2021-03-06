## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file geom_tk5.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_32 = Integer(32); _sage_const_69 = Integer(69); _sage_const_33 = Integer(33); _sage_const_403 = Integer(403); _sage_const_36 = Integer(36); _sage_const_359 = Integer(359); _sage_const_350 = Integer(350); _sage_const_372 = Integer(372); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_50 = Integer(50); _sage_const_384 = Integer(384); _sage_const_419 = Integer(419)## This file (geom_tk5.sagetex.sage) was *autogenerated* from geom_tk5.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('geom_tk5', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_69 
_st_.blockbegin()
try:
 # составление уравнение эллипса и параболы
 var('x,y,rho,varphi')
 # полуоси и фокальный параметр
 a = randint(_sage_const_1 , _sage_const_10 )
 b=a
 p=_sage_const_0 
 curve=randint(_sage_const_1 ,_sage_const_2 )
 Os=randint(_sage_const_1 , _sage_const_2 )
 while a==b or p==_sage_const_0 :
   b=randint(_sage_const_1 , _sage_const_10 )
   p=randint(-_sage_const_10 , _sage_const_10 )
 # ось симметрии и полуоси
 if Os==_sage_const_1 :
   symm=r'Ox'
 else:
   symm=r'Oy'
 if curve==_sage_const_1 :
   txtcurve=r'эллипса'
 else:
   txtcurve=r'гиперболы'
 if Os==_sage_const_1  and curve==_sage_const_1 :
   # эллипс
   answ1=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 ==_sage_const_1 
   c=sqrt(abs(a**_sage_const_2 -b**_sage_const_2 ))
   if a>b:
     F1=vector([c,_sage_const_0 ])
     F2=vector([-c,_sage_const_0 ])
   else:
     F1=vector([_sage_const_0 ,c])
     F2=vector([_sage_const_0 ,-c])
   # парабола
   answ2=y**_sage_const_2 ==_sage_const_2 *p*x
   F=vector([p/_sage_const_2 ,_sage_const_0 ])
 else:
   if Os==_sage_const_1  and curve==_sage_const_2 :
      # гипербола
      answ1=x**_sage_const_2 /a**_sage_const_2 -y**_sage_const_2 /b**_sage_const_2 ==_sage_const_1 
      c=sqrt(a**_sage_const_2 +b**_sage_const_2 )
      F1=vector([c,_sage_const_0 ])
      F2=vector([-c,_sage_const_0 ])
      # парабола
      answ2=y**_sage_const_2 ==_sage_const_2 *p*x
      F=vector([p/_sage_const_2 ,_sage_const_0 ])
   else:
      if Os==_sage_const_2  and curve==_sage_const_1 :
         # эллипс
         answ1=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 ==_sage_const_1 
         c=sqrt(abs(a**_sage_const_2 -b**_sage_const_2 ))
         if a>b:
           F1=vector([c,_sage_const_0 ])
           F2=vector([-c,_sage_const_0 ])
         else:
           F1=vector([_sage_const_0 ,c])
           F2=vector([_sage_const_0 ,-c])
         # парабола
         answ2=x**_sage_const_2 ==_sage_const_2 *p*y
         F=vector([_sage_const_0 ,p/_sage_const_2 ])
      else:
         # гипербола
         answ1=x**_sage_const_2 /a**_sage_const_2 -y**_sage_const_2 /b**_sage_const_2 ==_sage_const_1 
         c=sqrt(a**_sage_const_2 +b**_sage_const_2 )
         F1=vector([c,_sage_const_0 ])
         F2=vector([-c,_sage_const_0 ])
         # парабола
         answ2=x**_sage_const_2 ==_sage_const_2 *p*y
         F=vector([_sage_const_0 ,p/_sage_const_2 ])
 eq1=answ1
 eq2=eq1.multiply_both_sides(lcm(a**_sage_const_2 ,b**_sage_const_2 ))
 eq2=eq2.subs(x==rho*cos(varphi), y==rho*sin(varphi))
 eq2=eq2.trig_simplify()
 if eq2.find(cos(varphi))==[]:
    eq2=eq2.subs(sin(varphi)**_sage_const_2 ==_sage_const_1 /_sage_const_2 -cos(_sage_const_2 *varphi)/_sage_const_2 )
 else:
    eq2=eq2.subs(cos(varphi)**_sage_const_2 ==_sage_const_1 /_sage_const_2 +cos(_sage_const_2 *varphi)/_sage_const_2 )
 eq2=eq2.left().collect(rho**_sage_const_2 )==eq2.right()
 eq2=eq2.divide_both_sides(eq2.left()).multiply_both_sides(rho**_sage_const_2 )
 eq3=rho==sqrt(eq2.right()).simplify()
 polar1=eq3
 eq1=answ2
 eq2=eq1.multiply_both_sides(lcm(a**_sage_const_2 ,b**_sage_const_2 ))
 eq2=eq2.subs(x==rho*cos(varphi), y==rho*sin(varphi))
 eq2=eq2.trig_simplify()
 if eq2.find(cos(varphi))==[]:
   eq2=eq2.subs(sin(varphi)**_sage_const_2 ==_sage_const_1 /_sage_const_2 -cos(_sage_const_2 *varphi)/_sage_const_2 )
 else:
   eq2=eq2.subs(cos(varphi)**_sage_const_2 ==_sage_const_1 /_sage_const_2 +cos(_sage_const_2 *varphi)/_sage_const_2 )
 eq2=eq2.divide_both_sides(rho)
 eq3=eq2.divide_both_sides(eq2.left()).multiply_both_sides(rho)
 polar2=eq3
 G1=implicit_plot(answ1, (x,-_sage_const_2 *max(a,c),_sage_const_2 *max(a,c)), (y,-_sage_const_2 *max(a,c),_sage_const_2 *max(a,c)), axes='true', figsize=_sage_const_3 , color = 'black')
 #G1=polar_plot(polar1.right(), (varphi,0,2*pi),color='black', axes='true', #figsize=3)
 G2=implicit_plot(answ2, (x,-_sage_const_10 ,_sage_const_10 ), (y,-_sage_const_10 ,_sage_const_10 ), axes='true', figsize=_sage_const_3 , color = 'black')
 # составление уравнения по точке и расстоянию до кривой
 a1=_sage_const_0 
 b1=_sage_const_0 
 while a1==_sage_const_0  or b1==_sage_const_0 :
    A=vector([randint(-_sage_const_7 , _sage_const_7 ) for i in range(_sage_const_2 )])
    S=FiniteEnumeratedSet([_sage_const_1 /_sage_const_2 ,_sage_const_1 /_sage_const_3 ,_sage_const_1 ,_sage_const_2 ,_sage_const_3 ,_sage_const_3 /_sage_const_2 ,_sage_const_2 /_sage_const_3 ])
    n=S.random_element()
    ch1=randint(_sage_const_1 ,_sage_const_2 )
    c=randint(-_sage_const_4 ,_sage_const_7 )
    if ch1==_sage_const_1 :
         l=x-c==_sage_const_0 
    else:
         l=y-c==_sage_const_0 
    eq1=sqrt((x-A[_sage_const_0 ])**_sage_const_2 +(y-A[_sage_const_1 ])**_sage_const_2 )==n*(l.left())
    eq2=eq1**_sage_const_2 
    eq3=eq2.canonicalize_radical()
    eq4=eq3.left()-eq3.right()==_sage_const_0 
    a1=eq4.left().coefficient(x,_sage_const_2 )
    a2=eq4.left().coefficient(x,_sage_const_1 )
    c1=eq4.left().coefficient(x,_sage_const_0 ).coefficient(y,_sage_const_0 )
    b1=eq4.left().coefficient(y,_sage_const_2 )
    b2=eq4.left().coefficient(y,_sage_const_1 )
 eq5=x**_sage_const_2 +a2*x/a1
 eq6=y**_sage_const_2 +b2*y/b1
 var('cx,cy,k1,k2')
 from sympy import solve
 s1=solve(eq5-((x-cx)**_sage_const_2 +k1),[cx,k1])
 s2=solve(eq6-((y-cy)**_sage_const_2 +k2),[cy,k2])
 eq7=a1*(x-s1[_sage_const_0 ][_sage_const_0 ])**_sage_const_2 +b1*(y-s2[_sage_const_0 ][_sage_const_0 ])**_sage_const_2 ==-a1*s1[_sage_const_0 ][_sage_const_1 ]-b1*s2[_sage_const_0 ][_sage_const_1 ]-c1
 if eq7.rhs()==_sage_const_0 :
    answ3=eq7
 else:
    answ3=eq7.divide_both_sides(eq7.rhs())
 # приведение к каноническому виду
 # гиперболический тип
 def MakeEquationHypElps(a,b,ch1,mysgn):
     if mysgn==_sage_const_1 :
       eq=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 ==ch1
     else:
       eq=x**_sage_const_2 /a**_sage_const_2 -y**_sage_const_2 /b**_sage_const_2 ==ch1
     return eq
 ah=_sage_const_0 
 bh=_sage_const_0 
 while ah==bh:
     bh=randint(_sage_const_1 , _sage_const_10 )
     ah=randint(_sage_const_1 , _sage_const_10 )
 ch1h=randint(-_sage_const_1 ,_sage_const_1 )
 hyperb=MakeEquationHypElps(ah, bh, ch1h, _sage_const_2 )
 ae=_sage_const_0 
 be=_sage_const_0 
 while ae==be:
    be=randint(_sage_const_1 , _sage_const_10 )
    ae=randint(_sage_const_1 , _sage_const_10 )
 ch1e=randint(-_sage_const_1 ,_sage_const_1 )
 elps=MakeEquationHypElps(ae, be, ch1e, _sage_const_1 )
 def CanonToGeneralHypElps(eq,a,b):
     x0=randint(-_sage_const_10 ,_sage_const_10 )
     y0=randint(-_sage_const_10 ,_sage_const_10 )
     S = FiniteEnumeratedSet([pi/_sage_const_6 , pi/_sage_const_4 , pi/_sage_const_3 , _sage_const_2 *pi/_sage_const_3 , _sage_const_3 *pi/_sage_const_4 , _sage_const_5 *pi/_sage_const_6 , _sage_const_7 *pi/_sage_const_6 , _sage_const_5 *pi/_sage_const_4 , _sage_const_4 *pi/_sage_const_3 , _sage_const_5 *pi/_sage_const_3 ,_sage_const_7 *pi/_sage_const_4 ,_sage_const_11 *pi/_sage_const_6 , arctan(_sage_const_3 /_sage_const_4 ), arctan(_sage_const_5 /_sage_const_12 ), arctan(_sage_const_4 /_sage_const_3 ), arctan(_sage_const_12 /_sage_const_5 ), arctan(_sage_const_8 /_sage_const_15 ), arctan(_sage_const_15 /_sage_const_8 ), arctan(_sage_const_7 /_sage_const_24 ), arctan(_sage_const_24 /_sage_const_7 )])
     ang = S.random_element()
     eq1=eq.add_to_both_sides(-eq.right()).simplify()
     eq2=eq1.subs(x==x*cos(ang)+y*sin(ang), y==-x*sin(ang)+y*cos(ang))
     eq3=eq2.canonicalize_radical()
     eq4=eq3.multiply_both_sides(eq3.left().denominator())
     eq5=eq4.subs(x==x-x0,y==y-y0).expand()
     return [x0,y0,ang,eq5]
 hyp_task=CanonToGeneralHypElps(hyperb,ah,bh)
 G3=implicit_plot(hyp_task[_sage_const_3 ].left(), (x,-_sage_const_50 ,_sage_const_50 ), (y,-_sage_const_50 ,_sage_const_50 ), axes='true', figsize=_sage_const_3 , color = 'red')
 elps_task=CanonToGeneralHypElps(elps,ae,be)
 G4=implicit_plot(elps_task[_sage_const_3 ].left(), (x,-_sage_const_50 ,_sage_const_50 ), (y,-_sage_const_50 ,_sage_const_50 ), axes='true', figsize=_sage_const_3 , color = 'blue')
 # параболу делаем!
 ch1=randint(_sage_const_1 ,_sage_const_6 )
 ch2=randint(_sage_const_1 ,_sage_const_2 )
 p=_sage_const_0 
 while p==_sage_const_0 :
     p=randint(-_sage_const_10 ,_sage_const_10 )
 if ch1<=_sage_const_4 :
      if ch2==_sage_const_1 :
          parab=y**_sage_const_2 ==_sage_const_2 *p*x
      else:
          parab=x**_sage_const_2 ==_sage_const_2 *p*y
 else:
      if ch2==_sage_const_1  and p>_sage_const_0 :
          parab=y**_sage_const_2 ==p**_sage_const_2 
      elif ch2==_sage_const_1  and p<_sage_const_0 :
          parab=y**_sage_const_2 ==-p**_sage_const_2 
      elif ch2==_sage_const_2  and p>_sage_const_0 :
          parab=x**_sage_const_2 ==p**_sage_const_2 
      else:
          parab=x**_sage_const_2 ==-p**_sage_const_2 
 def CanonToGeneralParab(eq):
     x0=randint(-_sage_const_10 ,_sage_const_10 )
     y0=randint(-_sage_const_10 ,_sage_const_10 )
     S = FiniteEnumeratedSet([pi/_sage_const_6 , pi/_sage_const_4 , pi/_sage_const_3 , _sage_const_2 *pi/_sage_const_3 , _sage_const_3 *pi/_sage_const_4 , _sage_const_5 *pi/_sage_const_6 , _sage_const_7 *pi/_sage_const_6 , _sage_const_5 *pi/_sage_const_4 , _sage_const_4 *pi/_sage_const_3 , _sage_const_5 *pi/_sage_const_3 ,_sage_const_7 *pi/_sage_const_4 ,_sage_const_11 *pi/_sage_const_6 , arctan(_sage_const_3 /_sage_const_4 ), arctan(_sage_const_5 /_sage_const_12 ), arctan(_sage_const_4 /_sage_const_3 ), arctan(_sage_const_12 /_sage_const_5 ), arctan(_sage_const_8 /_sage_const_15 ), arctan(_sage_const_15 /_sage_const_8 ), arctan(_sage_const_7 /_sage_const_24 ), arctan(_sage_const_24 /_sage_const_7 )])
     ang = S.random_element()
     eq1=eq.add_to_both_sides(-eq.right()).simplify()
     eq2=eq1.subs(x==x-x0,y==y-y0).expand()
     eq3=eq2.subs(x==x*cos(ang)+y*sin(ang), y==-x*sin(ang)+y*cos(ang)).expand()
     eq4=eq3.multiply_both_sides(eq3.left().denominator())
     return [x0,y0,ang,eq4]
 parab_task=CanonToGeneralParab(parab)
 G5=implicit_plot(parab_task[_sage_const_3 ].left(), (x,-_sage_const_50 ,_sage_const_50 ), (y,-_sage_const_50 ,_sage_const_50 ), axes='true', figsize=_sage_const_3 , color = 'green')
 # робим поверхности. сначала со всеми тремя переменными (12 вариантов)
 ch1=randint(_sage_const_1 ,_sage_const_12 )
 ch2=randint(-_sage_const_1 ,_sage_const_1 )
 ch3=randint(_sage_const_1 ,_sage_const_2 )
 if ch3==_sage_const_1 :
    ch3=-_sage_const_1 
 else:
    ch3=_sage_const_1 
 var('z')
 abc=vector([randint(_sage_const_1 ,_sage_const_10 ) for i in range(_sage_const_3 )])
 a=abc[_sage_const_0 ]
 b=abc[_sage_const_1 ]
 c=abc[_sage_const_2 ]
 if ch1<=_sage_const_3 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==_sage_const_1 
 elif ch1==_sage_const_4 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 -z**_sage_const_2 /c**_sage_const_2 ==ch2
 elif ch1==_sage_const_5 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 -y**_sage_const_2 /b**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==ch2
 elif ch1==_sage_const_6 :
      eqconic=-x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==ch2
 elif ch1==_sage_const_7 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 ==ch3*_sage_const_2 *z
 elif ch1==_sage_const_8 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==ch3*_sage_const_2 *y
 elif ch1==_sage_const_9 :
      eqconic=y**_sage_const_2 /b**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==ch3*_sage_const_2 *x
 elif ch1==_sage_const_10 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 -y**_sage_const_2 /b**_sage_const_2 ==ch3*_sage_const_2 *z
 elif ch1==_sage_const_11 :
      eqconic=x**_sage_const_2 /a**_sage_const_2 -z**_sage_const_2 /c**_sage_const_2 ==ch3*_sage_const_2 *y
 else:
      eqconic=y**_sage_const_2 /b**_sage_const_2 -z**_sage_const_2 /c**_sage_const_2 ==ch3*_sage_const_2 *x
 x0y0z0=zero_vector(_sage_const_3 )
 while x0y0z0==zero_vector(_sage_const_3 ):
      x0y0z0=vector([randint(-_sage_const_10 ,_sage_const_10 ) for i in range(_sage_const_3 )])
 eq1=eqconic.subs(x==x-x0y0z0[_sage_const_0 ],y==y-x0y0z0[_sage_const_1 ],z==z-x0y0z0[_sage_const_2 ])
 eq2=eq1.expand()
 eq3=eq2.add_to_both_sides(-eq2.right())
 eq4=eq3.multiply_both_sides(eq3.left().denominator())
 conic_task=[x0y0z0, eq4]
 # робим поверхности. теперь цилиндрические (12 вариантов)
 ch1=randint(_sage_const_1 ,_sage_const_12 )
 ch2=randint(-_sage_const_1 ,_sage_const_1 )
 ch3=randint(_sage_const_1 ,_sage_const_2 )
 if ch3==_sage_const_1 :
    ch3=-_sage_const_1 
 else:
    ch3=_sage_const_1 
 pabc=vector([randint(_sage_const_1 ,_sage_const_10 ) for i in range(_sage_const_4 )])
 a=pabc[_sage_const_0 ]
 b=pabc[_sage_const_1 ]
 c=pabc[_sage_const_2 ]
 p=pabc[_sage_const_3 ]
 if ch1==_sage_const_1 :
    eqcyl=x**_sage_const_2 ==ch3*_sage_const_2 *p*y
 elif ch1==_sage_const_2 :
    eqcyl=y**_sage_const_2 ==ch3*_sage_const_2 *p*x
 elif ch1==_sage_const_3 :
    eqcyl=x**_sage_const_2 ==ch3*_sage_const_2 *p*z
 elif ch1==_sage_const_4 :
    eqcyl=z**_sage_const_2 ==ch3*_sage_const_2 *p*x
 elif ch1==_sage_const_5 :
    eqcyl=y**_sage_const_2 ==ch3*_sage_const_2 *p*z
 elif ch1==_sage_const_6 :
    eqcyl=z**_sage_const_2 ==ch3*_sage_const_2 *p*y
 elif ch1==_sage_const_7 :
    eqcyl=x**_sage_const_2 /a**_sage_const_2 +y**_sage_const_2 /b**_sage_const_2 ==_sage_const_1 
 elif ch1==_sage_const_8 :
    eqcyl=x**_sage_const_2 /a**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==_sage_const_1 
 elif ch1==_sage_const_9 :
    eqcyl=y**_sage_const_2 /b**_sage_const_2 +z**_sage_const_2 /c**_sage_const_2 ==_sage_const_1 
 elif ch1==_sage_const_10 :
    eqcyl=x**_sage_const_2 /a**_sage_const_2 -y**_sage_const_2 /b**_sage_const_2 ==ch2
 elif ch1==_sage_const_11 :
    eqcyl=x**_sage_const_2 /a**_sage_const_2 -z**_sage_const_2 /c**_sage_const_2 ==ch2
 else:
    eqcyl=y**_sage_const_2 /b**_sage_const_2 -z**_sage_const_2 /c**_sage_const_2 ==ch2
 x0y0z0=zero_vector(_sage_const_3 )
 while x0y0z0==zero_vector(_sage_const_3 ):
    x0y0z0=vector([randint(-_sage_const_10 ,_sage_const_10 ) for i in range(_sage_const_3 )])
 eq1=eqcyl.subs(x==x-x0y0z0[_sage_const_0 ],y==y-x0y0z0[_sage_const_1 ],z==z-x0y0z0[_sage_const_2 ])
 eq2=eq1.expand()
 eq3=eq2.add_to_both_sides(-eq2.right())
 eq4=eq3.multiply_both_sides(eq3.left().denominator())
 cyl_task=[x0y0z0, eq4]
except:
 _st_.goboom(_sage_const_350 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_359 
 _st_.inline(_sage_const_0 , txtcurve)
except:
 _st_.goboom(_sage_const_359 )
try:
 _st_.current_tex_line = _sage_const_359 
 _st_.inline(_sage_const_1 , latex(a))
except:
 _st_.goboom(_sage_const_359 )
try:
 _st_.current_tex_line = _sage_const_359 
 _st_.inline(_sage_const_2 , latex(b))
except:
 _st_.goboom(_sage_const_359 )
try:
 _st_.current_tex_line = _sage_const_359 
 _st_.inline(_sage_const_3 , latex(p))
except:
 _st_.goboom(_sage_const_359 )
try:
 _st_.current_tex_line = _sage_const_359 
 _st_.inline(_sage_const_4 , symm)
except:
 _st_.goboom(_sage_const_359 )
try:
 _st_.current_tex_line = _sage_const_372 
 _st_.inline(_sage_const_5 , latex(A))
except:
 _st_.goboom(_sage_const_372 )
try:
 _st_.current_tex_line = _sage_const_372 
 _st_.inline(_sage_const_6 , latex(l))
except:
 _st_.goboom(_sage_const_372 )
try:
 _st_.current_tex_line = _sage_const_372 
 _st_.inline(_sage_const_7 , latex(n))
except:
 _st_.goboom(_sage_const_372 )
try:
 _st_.current_tex_line = _sage_const_384 
 _st_.inline(_sage_const_8 , latex(hyp_task[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_384 )
try:
 _st_.current_tex_line = _sage_const_384 
 _st_.inline(_sage_const_9 , latex(elps_task[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_384 )
try:
 _st_.current_tex_line = _sage_const_384 
 _st_.inline(_sage_const_10 , latex(parab_task[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_384 )
try:
 _st_.current_tex_line = _sage_const_403 
 _st_.inline(_sage_const_11 , latex(conic_task[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_403 )
try:
 _st_.current_tex_line = _sage_const_403 
 _st_.inline(_sage_const_12 , latex(cyl_task[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_403 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_13 , txtcurve)
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_14 , latex(answ1))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_15 , latex(F1))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_16 , latex(F2))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_17 , latex(answ2))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_18 , latex(F))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_19 , latex(polar1))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_20 , latex(polar2))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=G1)
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=G2)
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_21 , latex(answ3))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_22 , latex(hyperb))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_23 , latex(hyp_task[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_24 , latex(hyp_task[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_25 , latex(hyp_task[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_26 , latex(elps))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_27 , latex(elps_task[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_28 , latex(elps_task[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_29 , latex(elps_task[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_30 , latex(parab))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_31 , latex(parab_task[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_32 , latex(parab_task[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_33 , latex(parab_task[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=G3)
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=G4)
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=G5)
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_34 , latex(eqconic))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_35 , latex(conic_task[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_36 , latex(eqcyl))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_37 , latex(cyl_task[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_419 )
_st_.endofdoc()

