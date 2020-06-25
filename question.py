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
		self.opciones = []
		if tipo == 1:
			a = random.randint(2, 5)
			self.tex = 'Si un paracaidista aterriza en un punto aleatorio en una recta entre los marcadores $A$ y $B$, encuentre la probabilidad de que su distancia hasta $A$ sea más de ' + num2words(a, lang='es') + ' veces su distancia a $B$.'
			self.text = 'Si un paracaidista aterriza en un punto aleatorio en una recta entre los marcadores A y B, encuentre la probabilidad de que su distancia hasta A sea más de ' + num2words(a, lang='es') + ' veces su distancia a B.'
			self.opciones.append(Respuesta(st.uniform.cdf(1/(a +1)), True))
			self.opciones.append(Respuesta(st.uniform.cdf(1/a), False))
			self.opciones.append(Respuesta(1 - st.uniform.cdf(1/(a+1)), False))
			self.opciones.append(Respuesta(1 - st.uniform.cdf(1/a), False))
		else:
			pass

