import os

def simplify(p,q):
	i = 2
	while(p%i==0 and q%i==0):
		p = int(p/i)
		q = int(q/i)
	i += 1	
	while(i<=p and i<=q):
		while(p%i==0 and q%i==0):
			p = int(p/i)
			q = int(q/i)
		i += 2
	r = [p,q]
	return r

def fileWrite(num,den,nom,des):
	f = open(nom,"w+", encoding="utf-8")
	f.write(f"! {nom}\n!\n{des}\n {len(num)}\n!\n")
	for i in range(0,len(num)):
		f.write(f" {num[i]}/{den[i]}\n")
	f.close()
	print("\n\nARCHIVO SCL CREADO")
	os.system("PAUSE>NUL")

def toFloat(p,q):
	return p/q

def order(num1,den1,num2,den2):
	rp = []
	rq = []
	while(len(num1)>0 or len(num2)>0):
		if(len(num1)>0 and len(num2)>0):
			if(toFloat(num1[0],den1[0])==toFloat(num2[0],den2[0])):
				rp.append(num1[0])
				rq.append(den1[0])
				num1.pop(0)
				den1.pop(0)
				num2.pop(0)
				den2.pop(0)
			elif(toFloat(num1[0],den1[0])<toFloat(num2[0],den2[0])):
				rp.append(num1[0])
				rq.append(den1[0])
				num1.pop(0)
				den1.pop(0)
			elif(toFloat(num1[0],den1[0])>toFloat(num2[0],den2[0])):
				rp.append(num2[0])
				rq.append(den2[0])
				num2.pop(0)
				den2.pop(0)
		elif(len(num1)>0 and len(num2)==0):
			for i in range(0,len(num1)):
				rp.append(num1[i])
				rq.append(den1[i])
			num1.clear()
			den1.clear()
		elif(len(num2)>0 and len(num1)==0):
			for i in range(0,len(num2)):
				rp.append(num2[i])
				rq.append(den2[i])
			num2.clear()
			den2.clear()
	aux = [rp,rq]
	return aux


def printList(num,den):
	print("\nEscala obtenida: ")
	for i in range(0,len(num)):
		print(f" {num[i]}/{den[i]}")

op = input("Seleccionar el tipo de escala: \n\n\t[1] Fundamental\n\t[2] Recíproca\n\t[3] Recíproca gradual\n\t[4] Compleja\n\t[5] Compleja con reciproca gradual\n\n_> ")
op = int(op)
if(op%5 == 1):
	p = []
	q = []
	M = int(input("\n\nMetro musical: "))
	n = int(input("\nNúmero de escala: "))
	for i in range(n,M*n):
		aux = simplify(i,n)
		p.append(aux[0])
		q.append(aux[1])
	desc = f"Escala fundamental de {n} con metro musical de {M}"
	nombre = f"Novaro-F_{n}-{M}.scl"
	if(p[len(p)-1]!= M and q[len(q)-1]!=1):
		p.append(M)
		q.append(1)
	printList(p,q)
	if(p[0]==1 and q[0]==1):
		p.pop(0)
		q.pop(0)
	fileWrite(p,q,nombre,desc)
elif(op%5 == 2):
	p = []
	q = []
	M = int(input("\n\nMetro musical: "))
	n = int(input("\nNúmero de escala: "))
	for i in range(n,M*n):
		aux = simplify(M*n,i)
		p.append(aux[0])
		q.append(aux[1])
	p.reverse()
	q.reverse()
	desc = f"Escala recíproca de {n} con metro musical de {M}"
	nombre = f"Novaro-R_{n}-{M}.scl"
	if(p[len(p)-1]!= M and q[len(q)-1]!=1):
		p.append(M)
		q.append(1)
	printList(p,q)
	if(p[0]==1 and q[0]==1):
		p.pop(0)
		q.pop(0)
	r = p
	s = q
	fileWrite(r,s,nombre,desc)
elif(op%5 == 3):
	p = []
	q = []
	M = int(input("\n\nMetro musical: "))
	n = int(input("\nNúmero de escala: "))
	G = int(input("\nEscalar para recíproca: "))
	for i in range(n,M*n):
		aux = simplify(M*G*n,i)
		p.append(aux[0])
		q.append(aux[1])
	p.reverse()
	q.reverse()
	desc = f"Escala recíproca gradual de {n} con metro musical de {M} y escalar {G}"
	nombre = f"Novaro-G_{n}-{M}.scl"
	if(p[len(p)-1]!= G*M and q[len(q)-1]!=1):
		p.append(M)
		q.append(1)
	printList(p,q)
	if(p[0]==1 and q[0]==1):
		p.pop(0)
		q.pop(0)
	fileWrite(p,q,nombre,desc)
elif(op%5 == 4):
	p = []
	q = []
	M = int(input("\n\nMetro musical: "))
	n = int(input("\nNúmero de escala: "))
	for i in range(n,M*n):
		aux = simplify(i,n)
		p.append(aux[0])
		q.append(aux[1])
	r = []
	s = []
	for i in range(n,M*n):
		aux = simplify(M*n,i)
		r.append(aux[0])
		s.append(aux[1])
	r.reverse()
	s.reverse()
	desc = f"Escala compleja de {n} con metro musical de {M}"
	nombre = f"Novaro-C_{n}-{M}.scl"
	lsts = order(p,q,r,s)
	p = lsts[0]
	q = lsts[1]
	r.clear()
	s.clear()
	if(p[len(p)-1]!= M and q[len(q)-1]!=1):
		p.append(M)
		q.append(1)
	printList(p,q)
	if(p[0]==1 and q[0]==1):
		p.pop(0)
		q.pop(0)
	fileWrite(p,q,nombre,desc)
else:
	p = []
	q = []
	M = int(input("\n\nMetro musical para fundamental: "))
	n = int(input("\nNúmero de escala: "))
	G = int(input("\nEscalar para recíproca: "))
	for i in range(n,M*n):
		aux = simplify(i,n)
		p.append(aux[0])
		q.append(aux[1])
	r = []
	s = []
	for i in range(n,M*n):
		aux = simplify(M*G*n,i)
		r.append(aux[0])
		s.append(aux[1])
	r.reverse()
	s.reverse()
	desc = f"Escala compleja con reciprocas graduales de {n} con metro musical de {M} y escalar {G}"
	nombre = f"Novaro-E_{n}-{M}-{G}.scl"
	lsts = order(p,q,r,s)
	p = lsts[0]
	q = lsts[1]
	r.clear()
	s.clear()
	if(p[len(p)-1]!= M*G and q[len(q)-1]!=1):
		p.append(M)
		q.append(1)
	printList(p,q)
	if(p[0]==1 and q[0]==1):
		p.pop(0)
		q.pop(0)
	fileWrite(p,q,nombre,desc)