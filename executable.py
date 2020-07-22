#!/usr/bin/python3
import question, subprocess, os, random

def write_in_text(file, p):
	file.write('------------------------------\n')
	file.write('\n')
	file.write('Title:\n')
	file.write(p.text + '\n')
	file.write('% Juan Diego Rojas, Tipo 0' + str(p.tipo) +', ver 01\n')
	file.write('\n')
	random.shuffle(p.opcionestext)
	file.write(p.opcionestext[0].asterisco() +  'a. ' + p.opciones[0].valor + '\n')
	file.write(p.opcionestext[1].asterisco() +  'b. ' + p.opciones[1].valor + '\n')
	file.write(p.opcionestext[2].asterisco() +  'c. ' + p.opciones[2].valor + '\n')
	file.write(p.opcionestext[3].asterisco() +  'd. ' + p.opciones[3].valor + '\n')
	file.write('------------------------------\n')

def write_in_tex(file, p):
	file.write('\\item ' + p.tex + '\n')
	file.write('\\begin{enumerate}[label = (\\alph*)]\n')
	#random.shuffle(p.opcionestex)
	file.write('\\item '+ p.opcionestex[0].valor + '\n')
	file.write('\\item '+ p.opcionestex[1].valor + '\n')
	file.write('\\item '+ p.opcionestex[2].valor + '\n')
	file.write('\\item '+ p.opcionestex[3].valor + '\n')
	file.write('\\end{enumerate}\n')

def tex_preamble(file):
	file.write('\\documentclass[11pt]{article}\n')
	file.write('\\usepackage[utf8]{inputenc}\n')
	file.write('\\usepackage[spanish,es-nodecimaldot]{babel}\n')
	file.write('\\usepackage{blindtext}\n')
	file.write('\\usepackage{enumitem}\n')
	file.write('\\usepackage{amsmath}\n')
	file.write('\\begin{document}\n')
	file.write('\\begin{enumerate}\n')

file = open('main.tex', 'w')
tex_preamble(file)
for i in range(1,32):
	write_in_tex(file, question.Pregunta(i))
file.write('\\end{enumerate}\n')
file.write('\\end{document}\n')


