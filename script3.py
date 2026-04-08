acl = int(input("ingresar numero de acl ipv4:"))
if acl >= 1 and acl <=99:
	print ("este es un acl estandar")
elif acl >=100 and acl <=199:
	print("este es un acl extendido")
else:
	print("ingrese un numero valido")

