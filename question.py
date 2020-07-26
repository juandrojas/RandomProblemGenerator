#!/usr/bin/python3
import random
import scipy.stats as st
import numpy as np
from num2words import num2words
class Tipo:
	"""docstring for Tipo"""
	def __init__(self, tipo):
		super(Tipo, self).__init__()
		self.tipo = tipo
		if tipo == 1:
			self.seccion = '4.4'
			self.numero = '4.39'
		elif tipo == 2:
			self.seccion = '4.4'
			self.numero = '4.47b'
		elif tipo == 3:
			self.seccion = '4.4'
			self.numero = '4.51'
		elif tipo == 4:
			self.seccion = '4.4'
			self.numero = '4.57'
		elif tipo == 5:
			self.seccion = '4.5'
			self.numero = '4.62'
		elif tipo == 6:
			self.seccion = '4.5'
			self.numero = '4.70'
		elif tipo == 7:
			self.seccion = '4.5'
			self.numero = '4.71'
		elif tipo == 8:
			self.seccion = '4.5'
			self.numero = '4.73b'
		elif tipo == 9:
			self.seccion = '4.5'
			self.numero = '4.74c'
		elif tipo == 10:
			self.seccion = '4.5'
			self.numero = '4.74d'
		elif tipo == 11:
			self.seccion = '4.5'
			self.numero = '4.75'
		elif tipo == 12:
			self.seccion = '4.5'
			self.numero = '4.80'
		elif tipo == 13:
			self.seccion = '4.6'
			self.numero = '4.89'
		elif tipo == 14:
			self.seccion = '4.6'
			self.numero = '4.90'
		elif tipo == 15:
			self.seccion = '4.6'
			self.numero = '4.92'
		elif tipo == 16:
			self.seccion = '4.6'
			self.numero = '4.93'
		elif tipo == 17:
			self.seccion = '4.6'
			self.numero = '4.98'
		elif tipo == 18:
			self.seccion = '4.6'
			self.numero = '4.103'
		elif tipo == 19:
			self.seccion = '4.6'
			self.numero = '4.109'
		elif tipo == 20:
			self.seccion = '4.7'
			self.numero = '4.123'
		elif tipo == 21:
			self.seccion = '4.7'
			self.numero = '4.124'
		elif tipo == 22:
			self.seccion = '4.7'
			self.numero = '4.128'
		elif tipo == 23:
			self.seccion = '4.7'
			self.numero = '4.129'
		elif tipo == 24:
			self.seccion = '4.7'
			self.numero = '4.133'
		elif tipo == 25:
			self.seccion = '4.9'
			self.numero = '4.140a'
		elif tipo == 26:
			self.seccion = '4.9'
			self.numero = '4.140c'
		elif tipo == 27:
			self.seccion = '4.10'
			self.numero = '4.146'
		elif tipo == 28:
			self.seccion = '4.10'
			self.numero = '4.147'
		elif tipo == 29:
			self.seccion = '4.10'
			self.numero = '4.151'
		elif tipo == 30:
			self.seccion = '4.10'
			self.numero = '4.152'
		elif tipo == 31:
			self.seccion = '4.10'
			self.numero = '4.153'
		elif tipo == 32:
			self.seccion = '4.12'
			self.numero = '4.161'
		elif tipo == 33:
			self.seccion = '4.12'
			self.numero = '4.162'
		elif tipo == 34:
			self.seccion = '4.5'
			self.numero = '4.66'
		elif tipo == 35:
			self.seccion = '4.12'
			self.numero = '4.163'
		elif tipo == 36:
			self.seccion = '4.12'
			self.numero = '4.168'
		elif tipo == 37:
			self.seccion = '4.12'
			self.numero = '4.169'
		elif tipo == 38:
			self.seccion = '4.12'
			self.numero = '4.171a'
		elif tipo == 39:
			self.seccion = '4.12'
			self.numero = '4.171b'

class Respuesta:
	"""docstring for Respuesta"""
	def __init__(self, valor, correcta):
		self.correcta = correcta
		self.valor = valor
	def asterisco(self):
		if self.correcta: #revisa si la opción es la correcta
			return '*'
		else:
			return ''

class Pregunta:
	"""base para cada pregunta for Pregunta"""
	def __init__(self, tipo):
		self.tipo = tipo
		self.opcionestext = []
		self.opcionestex = []
		if tipo == 1:
			a = random.randint(2, 5)
			self.tex = 'Si un paracaidista aterriza en un punto aleatorio en una recta entre los marcadores $A$ y $B$, encuentre la probabilidad de que su distancia hasta $A$ sea más de ' + num2words(a, lang='es') + ' veces su distancia a $B$.'
			# self.text = 'Si un paracaidista aterriza en un punto aleatorio en una recta entre los marcadores A y B, encuentre la probabilidad de que su distancia hasta A sea más de ' + num2words(a, lang='es') + ' veces su distancia a B.'
			# self.opcionestext.append(Respuesta(str(round(st.uniform.cdf(1/(a +1)),4)), True))
			# self.opcionestext.append(Respuesta(str(round(st.uniform.cdf(1/a),4)), False))
			# self.opcionestext.append(Respuesta(str(round(1 - st.uniform.cdf(1/(a+1)),4)), False))
			# self.opcionestext.append(Respuesta(str(round(1 - st.uniform.cdf(1/a),4)), False))
			self.opcionestex.append(Respuesta('$'+str(round(st.uniform.cdf(1/(a +1)),4))+'$', True))
			self.opcionestex.append(Respuesta('$'+str(round(st.uniform.cdf(1/a),4))+'$', False))
			self.opcionestex.append(Respuesta('$'+str(round(1 - st.uniform.cdf(1/(a+1)),4))+'$', False))
			self.opcionestex.append(Respuesta('$'+str(round(1 - st.uniform.cdf(1/a),4))+'$', False))
		elif tipo == 2:
			a = random.randint(1,5)
			i = random.randint(1,5)
			b = a+i
			self.tex = 'La falla de una tarjeta de circuito que utiliza un sistema de cómputo interrumpe el trabajo hasta que se instala una nueva. El tiempo de entrega, $Y$, está uniformemente distribuido en el intervalo de ' + num2words(a, lang='es') +' a ' + num2words(b, lang='es')+ ' días. El costo de la falla de una tarjeta y la interrupción incluye el costo fijo $c_0$ de una nueva tarjeta y un costo que aumenta proporcionalmente con $Y^2$. Si $C$ es el costo en que se incurre, $C=c_0+c_1Y^2$, en términos de $c_0$ y $c_1$ encuentre el costo esperado asociado a una sola tarjeta de circuito que falle.'
			# self.text = 'La falla de una tarjeta de circuito que utiliza un sistema de cómputo interrumpe el trabajo hasta que se instala una nueva. El tiempo de entrega, Y, está uniformemente distribuido en el intervalo de ' + num2words(a, lang='es') +' a ' + num2words(b, lang='es')+ ' días. El costo de la falla de una tarjeta y la interrupción incluye el costo fijo c_0 de una nueva tarjeta y un costo que aumenta proporcionalmente con Y^2. Si C es el costo en que se incurre, C=c_0+c_1*Y^2, , en términos de c_0 y c_1 encuentre el costo esperado asociado a una sola tarjeta de circuito que falle.' 
			self.opcionestex.append(Respuesta('$c_0 + ' + str(round(st.uniform.var(loc=a, scale =i) + st.uniform.mean(loc=a, scale =i)**2,4)) + 'c_1$', True))
			self.opcionestex.append(Respuesta('$c_0 + ' + str(round(st.uniform.mean(loc=a, scale =i)**2,4)) + 'c_1$', False))
			self.opcionestex.append(Respuesta('$c_0 + ' + str(round(st.uniform.mean(loc=a, scale =i),4)) + 'c_1$', False))
			self.opcionestex.append(Respuesta('$c_0 + ' + str(round(st.uniform.var(loc=a, scale =i),4)) + 'c_1$', False))
			# self.opcionestext.append(Respuesta('c_0 + ' + str(round(st.uniform.var(loc=a, scale =i) + st.uniform.mean(loc=a, scale =i)**2,4)) + '*c_1', True))
			# self.opcionestext.append(Respuesta('c_0 + ' + str(round(st.uniform.mean(loc=a, scale =i)**2,4)) + '*c_1', False))
			# self.opcionestext.append(Respuesta('c_0 + ' + str(round(st.uniform.mean(loc=a, scale =i),4)) + '*c_1', False))
			# self.opcionestext.append(Respuesta('c_0 + ' + str(round(st.uniform.var(loc=a, scale =i),4)) + '*c_1', False))
		elif tipo == 3:
			a = random.randint(1,10)*10
			b = random.randint(1,5)*5
			c = random.randint(1,5)*5
			d = random.randint(1,5)*5
			self.tex = 'El tiempo de ciclo para camiones que transportan concreto al lugar de construcción de una carretera está uniformemente distribuido en el intervalo de ' + str(a) +' a ' + str(a+b+c+d)+' minutos. ¿Cuál es la probabilidad de que el tiempo de ciclo exceda de ' + str(a+b+c) + ' minutos si se sabe que el tiempo de ciclo excede de ' + str(a+b) + ' minutos?'
			self.opcionestex.append(Respuesta('$' + str(round((1 - st.uniform.cdf(a+b+c, loc=a, scale=b+c+d))/(1 - st.uniform.cdf(a+b, loc=a, scale=b+c+d)), 4)) + '$', True))
			self.opcionestex.append(Respuesta('$' + str(round(1 - st.uniform.cdf(a+b, loc=a, scale=b+c+d), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round((1 - st.uniform.cdf(a+b, loc=a, scale=b+c+d))*(1 - st.uniform.cdf(a+b+c, loc=a, scale=b+c+d)), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(1 - st.uniform.cdf(a+b+c, loc=a, scale=b+c+d), 4)) + '$', False))
		elif tipo == 4:
			a = random.randint(1,5)/10
			b = random.randint(1,5)/10
			self.tex = 'De acuerdo con Zimmels (1983), los tamaños de partículas empleadas en experimentos de sedimentación a menudo tienen una distribución uniforme. En sedimentación que comprenda mezclas de partículas de varios tamaños, las más grandes impiden los movimientos de las más pequeñas. Entonces, es importante estudiar la media y la varianza de los tamaños de partículas. Suponga que las partículas esféricas tienen diámetros que están uniformemente distribuidos entre '+ str(a) +' y '+ str(a+b) +' centímetros. Encuentre la media de los volúmenes de estas partículas. (Recuerde que el volumen de una esfera es $(4/3)\\pi r^3$).'
			self.opcionestex.append(Respuesta('$' + str(round((1/6)*st.uniform.moment(3, loc=a, scale=b),7)) + '\\pi $', True))
			self.opcionestex.append(Respuesta('$' + str(round((4/3)*st.uniform.moment(3, loc=a, scale=b),7)) + '\\pi $', False))
			self.opcionestex.append(Respuesta('$' + str(round((1/6)*(st.uniform.moment(1, loc=a, scale=b)**3),7)) + '\\pi $', False))
			self.opcionestex.append(Respuesta('$' + str(round((4/3)*(st.uniform.moment(1, loc=a, scale=b)**3),7)) + '\\pi $', False))
		elif tipo == 5:
			a = random.randint(2,5)
			self.tex = 'Si $Z$ es una variable aleatoria normal estándar, ¿cuál es $P(Z^2 < 1/' + str(a**2) +' )$?'
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.cdf(1/a) - st.norm.cdf(-1/a), 4)) + '$', True))
			self.opcionestex.append(Respuesta('$' + str(round(1 - st.norm.cdf(1/a) + st.norm.cdf(-1/a), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.cdf(1/a), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(1 -st.norm.cdf(1/a), 4)) + '$', False))
		elif tipo == 6:
			a = 2.5 +random.randint(1,4)/10
			b = random.randint(3,6)/10
			n = random.randint(2,4)
			self.tex = 'Los promedios de calificaciones (GPA, por sus siglas en inglés) de una gran población de estudiantes universitarios están normalmente distribuidos en forma aproximada, con media de ' + str(a) + ' y desviación estándar '+ str(b) +'. Suponga que se escogen ' + num2words(n, lang='es') + ' estudiantes al azar del alumnado. ¿Cuál es la probabilidad de que los ' + num2words(n, lang='es') + ' estudiantes escogidos alcancen un GPA de más de 3.0?'
			self.opcionestex.append(Respuesta('$' + str(round(1 - st.norm.cdf(3, loc=a, scale = b)**n, 4)) + '$', True))
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.cdf(3, loc=a, scale = b)**n, 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.cdf(3, loc=a, scale = b), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(1 - st.norm.cdf(3, loc=a, scale = b), 4)) + '$', False))
		elif tipo == 7:
			a_ = random.randint(10,20)
			b_ = random.randint(2,5)
			m_ = random.randint(a_ +1 , a_+b_ - 1)
			a = round(a_/100, 4)
			b = round(b_/100, 4)
			m = round(m_/100, 4)
			s = random.randint(5,9)/100
			n = random.randint(2,4)
			self.tex = 'Se especifica que los cables manufacturados para usarse en un sistema de computadora deben tener resistencias entre ' + str(a) + ' y ' + str(round(a +b, 2)) + ' ohms. Las resistencias medidas reales de los cables producidos por la compañía $A$ tienen una distribución de probabilidad normal con media de ' + str(m) +' ohms y desviación estándar ' + str(s) + ' ohm. Si ' + num2words(n, lang='esp') + ' de los cables se usan en el sistema de computadora y todos son seleccionados de la compañia $A$, ¿cuál es la probabilidad de que los ' + num2words(n, lang='esp') + ' en un sistema seleccionado al azar satisfagan las especificaciones?'
			self.opcionestex.append(Respuesta('$' + str(round((st.norm.cdf(a, loc=m, scale=s) - st.norm.cdf(b, loc=m, scale=s))**n, 4)) + '$', True))
			self.opcionestex.append(Respuesta('$' + str(round((st.norm.cdf(a, loc=m, scale=s) - st.norm.cdf(b, loc=m, scale=s)), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(1 -(st.norm.cdf(a, loc=m, scale=s) - st.norm.cdf(b, loc=m, scale=s))**n, 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(1 -(st.norm.cdf(a, loc=m, scale=s) - st.norm.cdf(b, loc=m, scale=s)), 4)) + '$', False))
		elif tipo == 8:
			mu = 900 + random.randint(1,10)*10
			s = random.randint(10,20)
			q = round(random.random(), 4)
			self.tex = 'El ancho de rollos de tela está normalmente distribuido con media de ' + str(mu) + ' mm (milímimetros) y desviación estándar de ' + str(s) + ' mm. ¿Cuál es el valor apropiado para $C$ de manera que un rollo seleccionado al azar tenga un ancho menor que $C$ con probabilidad  ' + str(q) + '?'
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.ppf(q, loc = mu, scale = s), 4)) + '$', True))
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.ppf(1-q, loc = mu, scale = s), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(mu + st.norm.ppf(1-q, loc = 0, scale = 1), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(mu + st.norm.ppf(q, loc = 0, scale = 1), 4)) + '$', False))
		elif tipo == 9:
			mu = random.randint(50,75)
			s = random.randint(25,35)
			q = round(random.uniform(0.2, 0.4), 4)
			self.tex = 'Se supone que las calificaciones de un examen están normalmente distribuidas con media de '+ str(mu) + ' y varianza de ' + str(s) + '. ¿Cuál es el punto límite para pasar el examen si el examinador desea pasar sólo al ' + str(q*100) + '\\% de todas las calificaciones?' 
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.ppf(1-q, loc=mu, scale=s), 4)) + '$', True))
			self.opcionestex.append(Respuesta('$' + str(round(st.norm.ppf(q, loc=mu, scale=s), 4)) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(60) + '$', False))
			self.opcionestex.append(Respuesta('$' + str(round(60 + st.norm.ppf(1-q, loc=0, scale=1), 4)) + '$', False))
		elif tipo == 10:
			mu = random.randint(50,75)
			s = random.randint(25,35)
			q = random.randint(20,40)/100
			n = random.randint(3,8)
			self.tex = 'Se supone que las calificaciones de un examen están normalmente distribuidas con media de '+ str(mu) + ' y varianza de ' + str(s) + '. ¿Aproximadamente qué proporción de estudiantes tienen calificaciones de '+ str(n) + ' o más puntos arriba de la calificación que corta al ' + str(q*100) + '\\% más bajo?'
			self.opcionestex.append(Respuesta('$' + str(round((1 - st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) + n, loc=mu, scale=s))*100, 4)) + '\\%$', True))
			self.opcionestex.append(Respuesta('$' + str(round((st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) + n, loc=mu, scale=s))*100, 4)) + '\\%$', False))
			self.opcionestex.append(Respuesta('$' + str(round((1 - st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) - n, loc=mu, scale=s))*100, 4)) + '\\%$', False))
			self.opcionestex.append(Respuesta('$' + str(round((st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) - n, loc=mu, scale=s))*100, 4)) + '\\%$', False))
		elif tipo == 11:
			s = random.randint(2,8)/10
			q = random.randint(1,5)/100
			n = random.randint(5,10)
			self.tex = 'Una máquina expendedora de bebidas gaseosas puede ser regulada para descargar un promedio de $\\mu$ onzas por vaso. Si las onzas están normalmente distribuidas con desviación estándar de ' + str(s) + ' onzas, determine los valores de $\\mu$ de modo que vasos de '+ str(n) +' onzas se sirvan sólo ' + str(q*100) + '\\% del tiempo.'
			self.opcionestex.append(Respuesta(str(round(n - s*st.norm.ppf(1-q, loc=0, scale=1), 4)), True))
			self.opcionestex.append(Respuesta(str(round(n - s*st.norm.ppf(q, loc=0, scale=1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(n - (s**2)*st.norm.ppf(1-q, loc=0, scale=1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(n - (s**2)*st.norm.ppf(q, loc=0, scale=1), 4)), False))
		elif tipo == 12:
			n = random.randint(1,5)
			m = random.randint(1,5)
			self.tex = 'Suponga que $Y$ está normalmente distribuida con media $\\mu$ y desviación estándar $\\sigma$. Después de observar el valor de $Y$, un matemático construye un rectángulo con longitud $L = ' + str(n) + '|Y|$ y ancho $W = ' + str(m) + '|Y|$. Denote con $A$ el área del triángulo resultante. ¿Cuál es $E(A)$?'
			self.opcionestex.append(Respuesta('$' + str((n*m/2)) + '(\\mu^2 + \\sigma^2)$', True))
			self.opcionestex.append(Respuesta('$' + str((n*m)) + '(\\mu^2 + \\sigma^2)$', False))
			self.opcionestex.append(Respuesta('$' + str(n*m/2) + '(\\mu^2 - \\sigma^2)$', False))
			self.opcionestex.append(Respuesta('$' + str(n*m) + '(\\mu^2 - \\sigma^2)$', False))
		elif tipo == 13:
			q = round(random.uniform(0.01, 0.1), 4)
			n = random.randint(2,5)
			self.tex = 'Si $Y$ tiene tiene una distribución exponencial y $P(Y > ' + str(n) + ') = ' + str(q) + '$, ¿cuál es $\\beta = E(Y)$?'
			self.opcionestex.append(Respuesta(str(round(-n/np.log(q), 4)), True))
			self.opcionestex.append(Respuesta(str(round(-n/np.log(1-q), 4)), False))
			self.opcionestex.append(Respuesta(str(n), False))
			self.opcionestex.append(Respuesta(str(round(1/n, 4)), False))
		elif tipo == 14:
			a = random.randint(20,30)/10
			b = random.randint(45,60)/10
			n = random.randint(7,12)
			self.tex = 'La magnitud de los temblores registrados en una región de América del norte puede modelarse como si tuviera una distribución exponencial con media de ' + str(a) + ', según se mide en la escala de Richter. De los siguientes ' + num2words(n, lang='es') + ' temblores que afecten esta región, ¿cuál es la probabilidad de que al menos uno de ellos sea mayor que ' + str(b) + ' en la escala de Richter?'
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(b, loc=0, scale=a)**n, 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(b, loc=0, scale=a)**n, 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(b, loc=0, scale=a), 4)), False))
			self.opcionestex.append(Respuesta(str(round(n*(1 - st.expon.cdf(b, loc=0, scale=a))*st.expon.cdf(b, loc=0, scale=a)**7, 4)), False))
		elif tipo == 15:
			n = random.randint(5,15)
			a = random.randint(80,120)
			b = random.randint(25,50)
			c = random.randint(3,5)
			self.tex = 'El tiempo $Y$ necesario para completar una operación clave en la construcción de casas tiene una distribución exponencial con media de ' + str(n) + ' horas. La fórmula $C = ' + str(a) +' + ' +  str(b) + 'Y + ' + str(c) + 'Y^2$ relaciona el costo $C$ de completar esta operación con el cuadrado del tiempo para completarla. Encuentre la media de $C$.'
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.moment(2, loc=0, scale=n), 4)), True))
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.var(loc=0, scale=n), 4)), False))
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.mean(loc=0, scale=n), 4)), False))
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + (c**2)*st.expon.var(loc=0, scale=n), 4)), False))
		elif tipo == 16:
			n = random.randint(30,50)
			m = random.randint(2,25)
			self.tex ='Una evidencia histórica indica que los tiempos entre accidentes mortales en vuelos nacionales de horario programado en aviones de pasajeros en Estados Unidos tienen una distribución aproximadamente exponencial. Suponga que el tiempo medio entre accidentes es de ' + str(n) + ' días. Si el primero de los accidentes del mes de julio ocurrió el día ' + str(m) + ' de un año seleccionado al azar en el periodo de estudio, ¿cuál es la probabilidad de que ocurra otro accidente ese mismo mes?'
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(31-m+1, loc=0, scale=n), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(31, loc=0, scale=n), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(31-m+1, loc=0, scale=n), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(31, loc=0, scale=n), 4)), False))
		elif tipo == 17:
			b = random.randint(2,7)
			q = random.randint(1,10)/100
			self.tex = 'Una planta de manufactura utiliza un producto específico a granel. La cantidad de producto empleada en un día puede ser modelada por una distribución exponencial con $\\beta = ' + str(b) + '$ (medida en toneladas). ¿Cuánto producto a granel debe tener en existencia para que la probabilidad de que se agote el producto en la planta sea de solo ' + str(q) + '?'
			self.opcionestex.append(Respuesta(str(round(st.expon.ppf(1-q, loc=0, scale=b), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.expon.ppf(q, loc=0, scale=b), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.expon.ppf(1-q, loc=0, scale=1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.expon.ppf(q, loc=0, scale=1), 4)), False))
		elif tipo == 18:
			b = random.randint(5,15)
			self.tex = 'Materiales explosivos que se usan en operaciones de minería producen cráteres casi circulares cuando se hacen denotar. Los radios de estos cráteres están distribuidos exponencialmente con media de ' + str(b) + ' pies. Encuentre la varianza del área producida por estos materiales explosivos.'
			self.opcionestex.append(Respuesta('$' + str(int(st.expon.moment(4, loc=0, scale=b) - st.expon.moment(2, loc=0, scale=b)**2)) + '\\pi^2 $', True))
			self.opcionestex.append(Respuesta('$' + str(int(st.expon.moment(4, loc=0, scale=b) - st.expon.moment(1, loc=0, scale=b)**4)) + '\\pi^2 $', False))
			self.opcionestex.append(Respuesta('$' + str(int(st.expon.var(loc=0, scale=b)**4)) + '\\pi^2 $', False))
			self.opcionestex.append(Respuesta('$' + str(int(st.expon.moment(4, loc=0, scale=b) + st.expon.moment(2, loc=0, scale=b)**2)) + '\\pi^2 $', False))
		elif tipo == 19:
			a = random.randint(1,5)
			b = random.randint(1,5)
			s = random.randint(25,50)
			t = random.randint(2,5)
			self.tex = 'El tiempo improductivo por semana $Y$ (en horas) de una máquina industrial tiene aproximadamente una distribución gamma con $\\alpha = ' + str(a) + ' $ y $\\beta = ' + str(b) + ' $. La pérdida $L$ (en dólares) para la operación industrial como resultado de este tiempo improductivo está dada por $L = ' + str(s) + 'Y + ' + str(t) + 'Y^2$. Encuentre la varianza de $L$.'  
			self.opcionestex.append(Respuesta(str(int((s**2)*st.gamma.var(a, loc=0, scale=b) + (t**2)*(st.gamma.moment(4, a, loc=0, scale=b) - st.gamma.moment(2, a, loc=0, scale=b)**2) + 2*s*t*(st.gamma.moment(3, a, loc=0, scale=b) - st.gamma.moment(1, a, loc=0, scale=b)*st.gamma.moment(2, a, loc=0, scale=b)))), True))
			self.opcionestex.append(Respuesta(str(int((s**2)*st.gamma.var(a, loc=0, scale=b) + (t**2)*(st.gamma.moment(4, a, loc=0, scale=b) - st.gamma.moment(2, a, loc=0, scale=b)**2))), False))
			self.opcionestex.append(Respuesta(str(int((s**2)*st.gamma.var(a, loc=0, scale=b) + (t**2)*(st.gamma.moment(4, a, loc=0, scale=b) - st.gamma.moment(2, a, loc=0, scale=b)**2) + 2*s*t*(st.gamma.moment(3, a, loc=0, scale=b) - st.gamma.moment(1, a, loc=0, scale=b)**3))), False))
			self.opcionestex.append(Respuesta(str(int((s**2)*st.gamma.var(a, loc=0, scale=b) + (t**2)*(st.gamma.moment(4, a, loc=0, scale=b) - st.gamma.moment(1, a, loc=0, scale=b)**4) + 2*s*t*(st.gamma.moment(3, a, loc=0, scale=b) - st.gamma.moment(1, a, loc=0, scale=b)**3))), False))
		elif tipo == 20:
			a = random.randint(2,5)
			b = random.randint(2,5)
			self.tex = 'La humedad relativa $Y$, cuando se mide en una localidad, tiene una función de densidad de probabilidad dada por la siguiente expresión. Encuentre el valor de $k$ que hace a $f(y)$ una función de densidad. $$ f(y)=\\begin{cases} k y^' + str(a) + '(1-y)^' + str(b) + ', & 0 \\leq y \\leq 1, \\\\ 0, & \\text{ en cualquier otro punto.}\\end{cases}$$'
			self.opcionestex.append(Respuesta(str(round(np.math.factorial(a+b+1)/(np.math.factorial(a)*np.math.factorial(b)), 4)), True))
			self.opcionestex.append(Respuesta(str(round((np.math.factorial(a)*np.math.factorial(b))/np.math.factorial(a+b+1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(np.math.factorial(a+b+2)/(np.math.factorial(a+1)*np.math.factorial(b+1)), 4)), False))
			self.opcionestex.append(Respuesta(str(round((np.math.factorial(a+1)*np.math.factorial(b+1))/np.math.factorial(a+b+2), 4)), False))
		elif tipo == 21:
			q = random.randint(4,12)*5/100
			a = random.randint(2,5)
			b = random.randint(2,5)
			self.tex = 'El porcentaje de impurezas por lote en un producto químico es una variable aleatoria $Y$ con función de densidad $f(y)$ como se muestra abajo. Se sabe que un lote con más de ' + str(q*100) + '\\% de impurezas no se puede vender. Determine la probabilidad de que un lote seleccionado al azar no se pueda vender por exceso de impurezas. $$ f(y)=\\begin{cases} ' + str(int(np.math.factorial(a+b+1)/(np.math.factorial(a)*np.math.factorial(b)))) + 'y^' + str(a) + '(1-y)^' + str(b) + ', & 0 \\leq y \\leq 1, \\\\ 0, & \\text{ en cualquier otro punto.}\\end{cases}$$'
			self.opcionestex.append(Respuesta(str(round(1 - st.beta.cdf(q, a+1, b+1), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.beta.cdf(q, a+1, b+1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.beta.cdf(q, a, b), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.beta.cdf(q, a, b), 4)), False))
		elif tipo == 22:
			q = random.randint(1,12)*5/100
			a = random.randint(2,5)
			b = random.randint(2,5)
			self.tex = 'El costo $Y$ de reparaciones semanales para un máquina tiene una función de densidad de probabilidad $f(y)$ con mediciones en cientos de dólares. ¿Cuánto dinero debe presupuestarse a la semana para costos de reparación, de modo que el costo real rebase la cantidad presupuestada sólo el ' + str(q*100) + '\\% del tiempo? $$ f(y)=\\begin{cases} ' + str(int(np.math.factorial(a+b+1)/(np.math.factorial(a)*np.math.factorial(b)))) + 'y^' + str(a) + '(1-y)^' + str(b) + ', & 0 \\leq y \\leq 1, \\\\ 0, & \\text{ en cualquier otro punto.}\\end{cases}$$'
			self.opcionestex.append(Respuesta(str(round(st.beta.ppf(1-q, a+1, b+1), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.beta.ppf(q, a+1, b+1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.beta.ppf(1-q, a, b), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.beta.ppf(q, a, b), 4)), False))
		elif tipo == 23:
			a = random.randint(1,5)
			b = random.randint(1,5)
			s = random.randint(2,10)
			t = random.randint(2,8)*5
			r = random.randint(2,10)
			self.tex = 'Durante un turno de ocho horas la proporción de tiempo $Y$ que una máquina troqueladora de láminas metálicas está sin operar por mantenimiento o reparaciones tiene  una distribución beta con $\\alpha = ' + str(a) + '$ y $\\beta = '+ str(b) + '$. El costo (en cientos de dólares) de este tiempo improductivo, debido a producción perdida y costo de mantenimiento y reparación, está dado por $C = '+ str(s) + ' + ' + str(t) + 'Y + ' + str(r) + 'Y^2$. Encuentre la media de $Y$.'
			self.opcionestex.append(Respuesta(str(round(s + t*st.beta.mean(a,b) + r*st.beta.moment(2, a, b), 4)), True))
			self.opcionestex.append(Respuesta(str(round(t*st.beta.mean(a,b) + r*st.beta.moment(2, a, b), 4)), False))
			self.opcionestex.append(Respuesta(str(round(s + t*st.beta.mean(a,b) + r*st.beta.mean(a, b)**2, 4)), False))
			self.opcionestex.append(Respuesta(str(round(s + t*st.beta.mean(a,b) + r*st.beta.var(a, b), 4)), False))
		elif tipo == 24:
			a = random.randint(2,5)
			b = random.randint(2,5)
			self.tex = 'La proporción de tiempo por día que todas las cajas en un supermecado están ocupadas es una variable aleatoria $Y$ con una función de densidad dada por $f(y)$, para una constante $c$ que hace de $f(y)$ una función de densidad. Calcule la desviación estádar de $Y$. $$ f(y)=\\begin{cases} cy^' + str(a) + '(1-y)^' + str(b) + ', & 0 \\leq y \\leq 1, \\\\ 0, & \\text{ en cualquier otro punto.}\\end{cases}$$'
			self.opcionestex.append(Respuesta(str(round(st.beta.std(a+1,b+1), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.beta.var(a+1,b+1), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.beta.std(a,b), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.beta.var(a,b), 4)), False))
		elif tipo == 25:
			a = random.randint(2,5)
			b = random.randint(2,5)
			self.tex = 'Si la variable aleatoria $Y$ tiene la siguiente función generadora de momentos, ¿cómo se distribuye $Y$? $$ m(t) = \\frac{1}{(1-' + str(a) + 't)^' + str(b) + '} $$'	
			self.opcionestex.append(Respuesta('$Y \\sim $ Gamma(' + str(a) + ',' + str(b) + ')', True))
			self.opcionestex.append(Respuesta('$Y \\sim $ Beta(' + str(a + 1) + ',' + str(b + 1) + ')', False))
			self.opcionestex.append(Respuesta('$Y \\sim $ Beta(' + str(a) + ',' + str(b) + ')', False))
			self.opcionestex.append(Respuesta('$Y \\sim $ Gamma(' + str(a + 1) + ',' + str(b + 1) + ')', False))
		elif tipo == 26:
			mu = random.randint(-5,5)*2
			s = random.randint(2,5)
			self.tex = 'Si la variable aleatoria $Y$ tiene la siguiente función generadora de momentos, ¿cómo se distribuye $Y$? $$ m(t) = \\exp(' + str(mu) + 't + ' + str((s**2)/2) +' t^2)  $$'	
			self.opcionestex.append(Respuesta('$Y \\sim $ Normal($\\mu = ' + str(mu) + '$, $\\sigma = ' + str(s) + '$)', True))
			self.opcionestex.append(Respuesta('$Y \\sim $ Normal($\\mu = ' + str(mu) + '$, $\\sigma = ' + str((s**2)/2) + '$)', False))
			self.opcionestex.append(Respuesta('$Y \\sim $ Normal($\\mu = ' + str(mu) + '$, $\\sigma = ' + str(s**2) + '$)', False))
			self.opcionestex.append(Respuesta('$Y \\sim $ Normal($\\mu = ' + str(-mu) + '$, $\\sigma = ' + str((s**2)/2) + '$)', False))
		elif tipo == 27:
			q = random.randint(1,10)*5/100
			mu = random.randint(1,10)*5000
			s = random.randint(1,5)*1000
			self.tex = 'Un fabricante de llantas desea calcular un intervalo de rendimiento en millas que excluya no más de ' + str(q*100) + '\\% del rendimiento de las llantas que él vende. Todo lo que sabe es que, para un gran número de llantas probadas, la media del rendimiento fue de ' + str(mu) + ' millas y que la desviación estándar fue de ' + str(s) + ' millas. ¿Qué intervalo sugiere usted?'
			self.opcionestex.append(Respuesta('$(' + str(round((-s/np.sqrt(q)) + mu, 4)) + ',' + str(round((s/np.sqrt(q)) + mu, 4)) + ')$', True))
			self.opcionestex.append(Respuesta('$(' + str(round((-s/np.sqrt(q)), 4)) + ',' + str(round((s/np.sqrt(q)), 4)) + ')$', False))
			self.opcionestex.append(Respuesta('$(' + str(round((-s/q) + mu, 4)) + ',' + str(round((s/q) + mu, 4)) + ')$', False))
			self.opcionestex.append(Respuesta('$(' + str(round((-s/q), 4)) + ',' + str(round((s/q), 4)) + ')$', False))
		elif tipo == 28:
			n = random.randint(1,5)
			q = random.randint(11, 18)*5/100
			self.tex = 'Una máquina empleada para llenar cajas de cereal despacha, en promedio, $\\mu$ onzas por caja. El fabricante desea que las $Y$ onzas reales despachadas no rebasen por más de ' + str(n) + ' onzas a $\\mu$, al menos el ' + str(q*100) + '\\% del tiempo. ¿Cuál es el máximo valor de $\\sigma$, la desviación estándar de $Y$, que se puede tolerar si las metas del fabricante han de satisfacerse?'
			self.opcionestex.append(Respuesta(str(round(n*np.sqrt(1-q), 4)), True))
			self.opcionestex.append(Respuesta(str(round(n*np.sqrt(q), 4)), False))
			self.opcionestex.append(Respuesta(str(round(n*(1-q), 4)), False))
			self.opcionestex.append(Respuesta(str(round(n*(q), 4)), False))
		elif tipo == 29:
			n = random.randint(5,15)
			a = random.randint(80,120)
			b = random.randint(25,50)
			c = random.randint(2,3)
			r = random.randint(6,9)*1000
			mu = a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.moment(2, loc=0, scale=n)
			s = np.sqrt(a**2 + (b**2)*st.expon.moment(2, loc=0, scale=n) + (c**2)*st.expon.moment(4, loc=0, scale=n) + 2*a*b*st.expon.mean(loc=0, scale=n) + 2*a*c*st.expon.moment(2, loc=0, scale=n) + 2*b*c*st.expon.moment(3, loc=0, scale=n) - mu**2)
			self.tex = 'El tiempo $Y$ necesario para completar una operación clave en la construcción de casas tiene una distribución exponencial con media de ' + str(n) + ' horas. La fórmula $C = ' + str(a) +' + ' +  str(b) + 'Y + ' + str(c) + 'Y^2$ relaciona el costo $C$ (en dólares) de completar esta operación con el cuadrado del tiempo para completarla. ¿A lo sumo con qué frecuencia el costo rebasa los ' + str(r) + ' dólares?'
			self.opcionestex.append(Respuesta(str(round((s**2)/((r-mu)**2), 4)), True))
			self.opcionestex.append(Respuesta(str(round((s)/((r-mu)), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - (s**2)/((r-mu)**2), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - (s)/((r-mu)), 4)), False))
		elif tipo == 30:
			a = random.randint(1,5)
			b = random.randint(1,5)
			s = random.randint(25,50)
			t = random.randint(2,5)
			q = random.randint(75,95)/100
			sigma = np.sqrt((s**2)*st.gamma.var(a, loc=0, scale=b) + (t**2)*(st.gamma.moment(4, a, loc=0, scale=b) - st.gamma.moment(2, a, loc=0, scale=b)**2) + 2*s*t*(st.gamma.moment(3, a, loc=0, scale=b) - st.gamma.moment(1, a, loc=0, scale=b)*st.gamma.moment(2, a, loc=0, scale=b)))
			mu = s*st.gamma.mean(a, loc=0, scale=b) + t*st.gamma.moment(2, a, loc=0, scale=b)
			self.tex = 'El tiempo improductivo por semana $Y$ (en horas) de una máquina industrial tiene aproximadamente una distribución gamma con $\\alpha = ' + str(a) + ' $ y $\\beta = ' + str(b) + ' $. La pérdida $L$ (en dólares) para la operación industrial como resultado de este tiempo improductivo está dada por $L = ' + str(s) + 'Y + ' + str(t) + 'Y^2$. Encuentre un intervalo que contenga $L$ durante al menos ' + str(q*100) + ' \\% de las semanas que la máquina esta en uso.'  
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/np.sqrt(1-q)) + mu, 4)) + ',' + str(round((sigma/np.sqrt(1-q)) + mu, 4)) + ')$', True))
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/np.sqrt(q)) + mu, 4)) + ',' + str(round((sigma/np.sqrt(q)) + mu, 4)) + ')$', False))
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/q) + mu, 4)) + ',' + str(round((sigma/q) + mu, 4)) + ')$', False))
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/(1-q)) + mu, 4)) + ',' + str(round((sigma/(1-q)) + mu, 4)) + ')$', False))
		elif tipo == 31:
			a = random.randint(1,5)
			b = random.randint(1,5)
			s = random.randint(2,10)
			t = random.randint(2,8)*5
			r = random.randint(2,10)
			q = random.randint(75,95)/100
			mu = s + t*st.beta.mean(a,b) + r*st.beta.moment(2, a, b)
			sigma = np.sqrt(s**2 + (t**2)*st.beta.moment(2, a, b) + (r**2)*st.beta.moment(4, a, b) + 2*s*t*st.beta.mean(a, b) + 2*s*r*st.beta.moment(2, a, b) + 2*t*r*st.beta.moment(3, a, b) - mu**2)
			self.tex = 'Durante un turno de ocho horas la proporción de tiempo $Y$ que una máquina troqueladora de láminas metálicas está sin operar por mantenimiento o reparaciones tiene  una distribución beta con $\\alpha = ' + str(a) + '$ y $\\beta = '+ str(b) + '$. El costo (en cientos de dólares) de este tiempo improductivo, debido a producción perdida y costo de mantenimiento y reparación, está dado por $C = '+ str(s) + ' + ' + str(t) + 'Y + ' + str(r) + 'Y^2$. Encuentre un intervalo para el cual la probabilidad de que $C$ se encuentre dentro del mismo sea al menos ' + str(q) + '.'
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/np.sqrt(1-q)) + mu, 4)) + ',' + str(round((sigma/np.sqrt(1-q)) + mu, 4)) + ')$', True))
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/np.sqrt(q)) + mu, 4)) + ',' + str(round((sigma/np.sqrt(q)) + mu, 4)) + ')$', False))
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/q) + mu, 4)) + ',' + str(round((sigma/q) + mu, 4)) + ')$', False))
			self.opcionestex.append(Respuesta('$(' + str(round((-sigma/(1-q)) + mu, 4)) + ',' + str(round((sigma/(1-q)) + mu, 4)) + ')$', False))
		elif tipo == 32:
			mu = random.randint(12,18)*5
			s = random.randint(8,15)
			q = random.randint(14,18)*5/100
			self.tex = 'El tiempo necesario para completar un examen de aptitud en universidades se encuentra normalmente distribuido con media de ' + str(mu) + ' minutos y desviación estándar de ' + str(s) + ' minutos. ¿Cuántos minutos debe durar el examen si deseamos que el ' +str(q*100) + '\\% de los estudiantes tenga suficiente tiempo para completar el examen?'
			self.opcionestex.append(Respuesta(str(round(st.norm.ppf(q, loc=mu, scale=s), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.norm.ppf(1-q, loc=mu, scale=s), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.norm.ppf(q, loc=mu, scale=s**2), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.norm.ppf(q, loc=0, scale=1), 4)), False))
		elif tipo == 33:
			n = random.randint(6,10)*500
			mu = random.randint(3,6)*100
			s = random.randint(4,7)*10
			q = random.randint(1,5)/100
			self.tex = 'Una fábrica utiliza ' + str(n) + ' focos cuya vida útil está normalmente distribuida con media de ' + str(mu) + ' horas y desviación estándar de ' + str(s) + '. Para reducir al mínimo el número de focos que se queman durante horas de operación, todos son cambiados después de un periodo determinado. ¿Con quué frecuencia deben cambiarse los focos si deseamos que no más de ' + str(q*100) + '\\% de los focos se quemen entre periodos de cambio.'
			self.opcionestex.append(Respuesta(str(round(st.norm.ppf(1-q, loc=mu, scale=s), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.norm.ppf(q, loc=mu, scale=s), 4)), False))
			self.opcionestex.append(Respuesta(str(round(n*q, 4)), False))
			self.opcionestex.append(Respuesta(str(round(n*(1-q))), False))
		elif  tipo == 34:
			n = random.randint(1,5)
			mu = n + random.randint(1,2)*5/10000
			s = random.randint(2,5)*5/10000
			e = random.randint(5,10)*5/10000
			self.tex = 'Una operación de maquinado produce cojinetes con diámteros que está normalmente distribuidos con media de ' + str(mu) + ' pulgadas y desviación estándar de ' + str(s) + ' pulgadas. Las especificaciones requieren que los diámetros de los cojinetes se encuentren el intervalo $' + str(n) + ' \\pm ' + str(e) + ' $ pulgadas. Los cojinetes que estén fuera de este intervalo son considerados de desecho y deben volver a maquinarse. Con el ajuste de la máquina existente, ¿qué fracción de la producción total se desechará?'
			self.opcionestex.append(Respuesta(str(round(1 - (st.norm.cdf(n + e, loc=mu, scale=s) - st.norm.cdf(n - e, loc=mu, scale=s)),  5)), True))
			self.opcionestex.append(Respuesta(str(round((st.norm.cdf(n + e, loc=mu, scale=s) - st.norm.cdf(n - e, loc=mu, scale=s)),  5)), False))
			self.opcionestex.append(Respuesta(str(round(1 - (st.norm.cdf(n + e, loc=mu, scale=s)),  5)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.norm.cdf(n - e, loc=mu, scale=s),  5)), False))
		elif tipo == 35:
			n = random.randint(1,5)
			m = random.randint(2,5)
			mu = n + random.randint(1,2)*5/10000
			s = random.randint(2,5)*5/10000
			e = random.randint(5,10)*5/10000
			self.tex = 'Una operación de maquinado produce cojinetes con diámteros que está normalmente distribuidos con media de ' + str(mu) + ' pulgadas y desviación estándar de ' + str(s) + ' pulgadas. Las especificaciones requieren que los diámetros de los cojinetes se encuentren el intervalo $' + str(n) + ' \\pm ' + str(e) + ' $ pulgadas. Los cojinetes que estén fuera de este intervalo son considerados de desecho y deben volver a maquinarse. Suponga que ' + num2words(m, lang = 'es') + ' se sacan al azar de la producción. ¿Cuál es la probabilidad de que al menos uno esté defectuso?'
			q = 1 - (st.norm.cdf(n + e, loc=mu, scale=s) - st.norm.cdf(n - e, loc=mu, scale=s))
			self.opcionestex.append(Respuesta(str(round(1 - ((1-q)**m), 4)), True))
			self.opcionestex.append(Respuesta(str(round(1 - ((q)**m), 4)), False))
			self.opcionestex.append(Respuesta(str(round(((1-q)**m), 4)), False))
			self.opcionestex.append(Respuesta(str(round(q, 4)), False))
		elif tipo == 36:
			mu = random.randint(8,12)*1000
			c = random.randint(3,7)*1000
			self.tex = 'El número de millas que un automóvil puede recorrer antes de que su batería se agote se distribuye exponencialmente con media de ' + str(mu) + ' millas. El propietario de un automóvil necesita hacer un viaje de ' + str(c) + ' millas. ¿Cuál es la probabilidad de que pueda hacer el viaje sin tener que reemplazar la batería del coche?'
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(c, loc=0, scale=mu), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(c, loc=0, scale=mu), 4)), False))
			self.opcionestex.append(Respuesta('Como no se sabe cuánta batería ha agotado el automóvil antes de iniciar el viaje, no hay suficiente información para responder.', False))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(c, loc=0, scale=mu+c), 4)), False))
		elif tipo == 37:
			l = random.randint(5,15)
			t = random.randint(10,25)
			self.tex = 'Si entran llamadas a un centro policial de emergencia a razón de ' + num2words(l, lang='es') + ' por hora, ¿cuál es la probabilidad de que transcurran más de ' + str(t) + ' minutos entre las dos llamadas siguientes?'
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(t/60, loc=0, scale=1/l), 4)), True))
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(t/60, loc=0, scale=1/l), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(t/60, loc=0, scale=l), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(t/60, loc=0, scale=l), 4)), False))
		elif tipo == 38:
			l = random.randint(2, 5)
			self.tex = 'Suponga que llegan clientes a una caja a razón de ' + num2words(l, lang='es') + ' por minuto. ¿Cuáles son la media y la varianza de los tiempo de espera entre llegadas sucesivas de clientes?'
			self.opcionestex.append(Respuesta('$\\mu = \\frac{1}{' + str(l) + '}$, $\\sigma^2 = \\frac{1}{' + str(l**2) + '}$', True))
			self.opcionestex.append(Respuesta('$\\mu = ' + str(l) + '$, $\\sigma^2 = \\frac{1}{' + str(l) + '}$', False))
			self.opcionestex.append(Respuesta('$\\mu = ' + str(l) + '$, $\\sigma^2 = ' + str(l**2) + '$', False))
			self.opcionestex.append(Respuesta('$\\mu = \\frac{1}{' + str(l) + '}$, $\\sigma^2 = \\frac{1}{' + str(l) + '}$', False))
		elif tipo == 39:
			l = random.randint(2, 5)
			n = random.randint(3,5)
			self.tex = 'Suponga que llegan clientes a una caja a razón de ' + num2words(l, lang='es') + ' por minuto. Si una empleada tarda ' + str(n) + ' minutos en atender al primer cliente que llega a una caja, ¿cuál es la probabilidad de que al menos un cliente más esté esperando cuando se termine de servir al primer cliente?'
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(n, loc=0, scale=1/l), 4)), True))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(n, loc=0, scale=1/l), 4)), False))
			self.opcionestex.append(Respuesta(str(round(1 - st.expon.cdf(n, loc=0, scale=l), 4)), False))
			self.opcionestex.append(Respuesta(str(round(st.expon.cdf(n, loc=0, scale=l), 4)), False))
		
