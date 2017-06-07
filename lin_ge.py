import numpy as np
import scipy.optimize as op
def optimize(price,percent_profit,current_money):
	c=[]
	for i in range(0,len(price)):
		current_item_price = price[i]
		real_sell_price = current_item_price + percent_profit*current_item_price
		real_sell_price=real_sell_price - current_item_price
		real_sell_price=-1.0*real_sell_price
		c.append(real_sell_price)

	airlimit=20000.0
	astrallimit=10000.0
	bloodlimit=10000.0
	bodylimit=12000.0
	chaoslimit=12000.0
	cosmiclimit=12000.0
	deathlimit=10000.0
	dustlimit=12000.0
	earthlimit=20000.0
	firelimit=20000.0
	lavalimit=12000.0
	lawlimit=12000.0
	mindlimit=12000.0
	mistlimit=12000.0
	mudlimit=12000.0
	naturelimit=12000.0
	smokelimit=12000.0
	soullimit=10000.0
	steamlimit=12000.0
	waterlimit=20000.0

	b_ub= [airlimit,astrallimit,bloodlimit,bodylimit,chaoslimit,cosmiclimit,deathlimit,dustlimit,earthlimit,firelimit,lavalimit,lawlimit,mindlimit, mistlimit,mudlimit,naturelimit,smokelimit,soullimit,steamlimit,waterlimit]
	numberofrunes=len(b_ub)
	b_eq=[current_money]
	bound_list=()
		

	A_eq = np.ones((1,numberofrunes))
	for i in range(0,numberofrunes):
		A_eq[0,i] = price[i]
	A_ub= np.eye(numberofrunes,numberofrunes)
	res = op.linprog(c, A_ub=A_ub, b_ub=b_ub,A_eq=A_eq,b_eq=b_eq, bounds=(0,None),options={"disp": True})
	sol=res.x
	return (c,sol,res.fun)

def optimal_optimize(price,percent_profit,current_money):
	(c,x,fun)=optimize(price,percent_profit,current_money)
	print x


optimal_optimize([5.0,138.0,253.0,5.0,103.0,123.0,263.0,2.0,5.0,5.0,3.0,207.0,4.0,22.0,212.0,205.0,19.0,144.0,81.0,5.0],.025,100000.0)











		