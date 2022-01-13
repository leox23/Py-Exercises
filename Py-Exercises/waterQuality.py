import re

riesgo4 = "MPS, INS, MAVDT, Contraloría General, Procuraduría General"
riesgo3 = "SSPD"
riesgo2 = "Alcaldía, Gobernación"
riesgo1 = "Persona prestadora, COVE"
prefijoRiesgo = "El caso debe ser notificado a:"
riesgo0 = "Sin riesgo alguno, continuar el control y la vigilancia."

def waterQuality(state):
	"""
Limitacion: en la concatenacion dentro de las printeadas no se como quitarle los espacios al concatenar unos con otros, ya que lo hice concatenando las variabes que contienen los strings
	"""
	if re.search("[|¬°\"\'!#$%&/\(\)=?¿¡+¨´*~\{\}\[\]\^\`\-,;:_\<\>]", state):
		print("\nFavor agregar un nivel de riesgo valido o numero positivo IRCA(%) valido, debe ser sin simbolos.\nDatos validos son:\n=> Sin riesgo, Bajo, Medio, Alto, Inviable,\n=> O numero del 0 al 100.")
		waterQuality(input('Ingrese el tipo de riesgo, o numero del 0 al 100:'))
		return
	elif not re.search("[a-zA-Z]|\s|\.", state):
		state = int(state)
	elif re.search("\.", state) and (not re.search("[a-zA-Z]|\s", state)):
		state = float(state)
	else:
		state = (state.strip()).upper()
	if isinstance(state, str):
		if state == "INVIABLE":
			print(prefijoRiesgo,riesgo1,',',riesgo2,',',riesgo3,',',riesgo4,end=".")
		elif state == "ALTO":
			print(prefijoRiesgo,riesgo1,',',riesgo2,',',riesgo3,end=".")
		elif state == "MEDIO":
			print(prefijoRiesgo,riesgo1,',',riesgo2,',',end=".")
		elif state == "BAJO":
			print(prefijoRiesgo,riesgo1,end=".")
		elif state == "SIN RIESGO": #corregir
			print(riesgo0)
		else:
			print("\nSiendo texto, favor colocar uno de los riesgos valido:\n=> Sin riesgo, Bajo, Medio, Alto, Inviable.")
			waterQuality(input('Ingrese el tipo de riesgo, o numero del 0 al 100:'))
	elif isinstance(state, int) or isinstance(state, float):
		if state > 80 and state <= 100:
			print(prefijoRiesgo,riesgo1,',',riesgo2,',',riesgo3,',',riesgo4,end=".")
		elif state > 35 and state <= 80:
			print(prefijoRiesgo,riesgo1,',',riesgo2,',',riesgo3,end=".")
		elif state > 14 and state <= 35:
			print(prefijoRiesgo,riesgo1,',',riesgo2,end=".")
		elif state > 5 and state <= 14:
			print(prefijoRiesgo,riesgo1,end=".")
		elif state >= 0 and state <= 5:
			print(riesgo0)
		else:
			print("\nSe debe ingresar un numero positivo de 0 a 100,\ncorrespondiente a la Clasificación IRCA (%).")
			waterQuality(input('Ingrese el tipo de riesgo, o numero del 0 al 100:'))

waterQuality(input('Detector del nivel de la calidad del agua y a que Entidades notificar\nIngrese el tipo de riesgo, o numero del 0 al 100:'))
