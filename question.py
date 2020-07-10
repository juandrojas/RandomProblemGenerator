#!/usr/bin/python3
import random
import scipy.stats as st
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
			q = round(random.uniform(0.2, 0.3), 4)
			n = random.randint(3,8)
			self.tex = 'Se supone que las calificaciones de un examen están normalmente distribuidas con media de '+ str(mu) + ' y varianza de ' + str(s) + '. ¿Aproximadamente qué proporción de estudiantes tienen calificaciones de '+ str(n) + ' o más puntos arriba de la calificación que corta al ' + str(q*100) + '\\% más bajo?'
			self.opcionestex.append(Respuesta('$' + str(round((1 - st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) + n, loc=mu, scale=s))*100, 4)) + '\\%$', True))
			self.opcionestex.append(Respuesta('$' + str(round((st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) + n, loc=mu, scale=s))*100, 4)) + '\\%$', False))
			self.opcionestex.append(Respuesta('$' + str(round((1 - st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) - n, loc=mu, scale=s))*100, 4)) + '\\%$', False))
			self.opcionestex.append(Respuesta('$' + str(round((st.norm.cdf(st.norm.ppf(q, loc=mu, scale=s) - n, loc=mu, scale=s))*100, 4)) + '\\%$', False))
			
