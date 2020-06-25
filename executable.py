#!/usr/bin/python3
import question, subprocess, os, random
p = question.Pregunta(1)
with open('file.text', 'w') as file:
	file.write('------------------------------\n')
	file.write('\n')
	file.write('Title:\n')
	file.write(p.text + '\n')
	file.write('% Juan Diego Rojas, Tipo 0' + str(p.tipo) +', ver 01\n')
	file.write('\n')
	random.shuffle(p.opciones)
	file.write(p.opciones[0].asterisco() +  'a. ' + str(p.opciones[0].valor) + '\n')
	file.write(p.opciones[1].asterisco() +  'b. ' + str(p.opciones[1].valor) + '\n')
	file.write(p.opciones[2].asterisco() +  'c. ' + str(p.opciones[2].valor) + '\n')
	file.write(p.opciones[3].asterisco() +  'd. ' + str(p.opciones[3].valor) + '\n')