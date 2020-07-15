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
			c = random.randint(2,5)
			self.tex = 'El tiempo $Y$ necesario para completar una operación clave en la construcción de casas tiene una distribución exponencial con media de ' + str(n) + ' horas. La fórmula $C = ' + str(a) +' + ' +  str(b) + 'Y + ' + str(c) + 'Y^2$ relaciona el costo $C$ de completar esta operación con el cuadrado del tiempo para completarla. Encuentre la media de $C$.'
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.moment(2, loc=0, scale=n), 4)), True))
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.var(loc=0, scale=n), 4)), False))
			self.opcionestex.append(Respuesta(str(round(a + b*st.expon.mean(loc=0, scale=n) + c*st.expon.mean(loc=0, scale=n)**2, 4)), False))
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
			

			
			
