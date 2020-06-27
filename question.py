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
			self.numero = '39'
		elif tipo == 2:
			self.seccion = '4.4'
			self.numero = '4.47b'

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
			self.text = 'Si un paracaidista aterriza en un punto aleatorio en una recta entre los marcadores A y B, encuentre la probabilidad de que su distancia hasta A sea más de ' + num2words(a, lang='es') + ' veces su distancia a B.'
			self.opcionestext.append(Respuesta(str(st.uniform.cdf(1/(a +1))), True))
			self.opcionestext.append(Respuesta(str(st.uniform.cdf(1/a)), False))
			self.opcionestext.append(Respuesta(str(1 - st.uniform.cdf(1/(a+1))), False))
			self.opcionestext.append(Respuesta(str(1 - st.uniform.cdf(1/a)), False))
			self.opcionestex.append(Respuesta(str(st.uniform.cdf(1/(a +1))), True))
			self.opcionestex.append(Respuesta(str(st.uniform.cdf(1/a)), False))
			self.opcionestex.append(Respuesta(str(1 - st.uniform.cdf(1/(a+1))), False))
			self.opcionestex.append(Respuesta(str(1 - st.uniform.cdf(1/a)), False))
		elif tipo == 2:
			a = random.randint(1,5)
			i = random.randint(1,5)
			b = a+i
			self.tex = 'La falla de una tarjeta de circuito que utiliza un sistema de cómputo interrumpe el trabajo hasta que se instala una nueva. El tiempo de entrega, $Y$, está uniformemente distribuido en el intervalo de ' + num2words(a, lang='es') +' a ' + num2words(b, lang='es')+ ' días. El costo de la falla de una tarjeta y la interrupción incluye el costo fijo $c_0$ de una nueva tarjeta y un costo que aumenta proporcionalmente con $Y^2$ .Si $C$ es el costo en que se incurre, $C=c_0+c_1Y^2$, en términos de $c_0$ y $c_1$ encuentre el costo esperado asociado a que una sola tarjeta de circuito que falle.'
			self.text = 'La falla de una tarjeta de circuito que utiliza un sistema de cómputo interrumpe el trabajo hasta que se instala una nueva. El tiempo de entrega, Y, está uniformemente distribuido en el intervalo de ' + num2words(a, lang='es') +' a ' + num2words(b, lang='es')+ ' días. El costo de la falla de una tarjeta y la interrupción incluye el costo fijo c_0 de una nueva tarjeta y un costo que aumenta proporcionalmente con Y^2 .$ Si C es el costo en que se incurre, C=c_0+c_1*Y^2, , en términos de c_0 y c_1 encuentre el costo esperado asociado a que una sola tarjeta de circuito que falle.' 
			self.opcionestex.append(Respuesta('$c_0 + ' + str(st.uniform.var(loc=a, scale =i) + st.uniform.mean(loc=a, scale =i)**2) + 'c_1$', True))
			self.opcionestex.append(Respuesta('$c_0 + ' + str(st.uniform.mean(loc=a, scale =i)**2) + 'c_1$', False))
			self.opcionestex.append(Respuesta('$c_0 + ' + str(st.uniform.mean(loc=a, scale =i)) + 'c_1$', False))
			self.opcionestex.append(Respuesta('$c_0 + ' + str(st.uniform.var(loc=a, scale =i)) + 'c_1$', False))
			self.opcionestext.append(Respuesta('c_0 + ' + str(st.uniform.var(loc=a, scale =i) + st.uniform.mean(loc=a, scale =i)**2) + '*c_1', True))
			self.opcionestext.append(Respuesta('c_0 + ' + str(st.uniform.mean(loc=a, scale =i)**2) + '*c_1', False))
			self.opcionestext.append(Respuesta('c_0 + ' + str(st.uniform.mean(loc=a, scale =i)) + '*c_1', False))
			self.opcionestext.append(Respuesta('c_0 + ' + str(st.uniform.var(loc=a, scale =i)) + '*c_1', False))


