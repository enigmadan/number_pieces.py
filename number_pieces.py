#!/usr/bin/python
# # -*- coding: utf-8 -*-
# # @Author: dmyers
# # @Date:   2017-05-06 20:19:59
# # @Last Modified by:   dmyers
# # @Last Modified time: 2017-10-09 19:56:16



from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
import random
import sys

scale = [1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1] #starts major two octaves
used_notes = {}

if len(sys.argv)!=1:
	num = int(sys.argv[1])
	key = int(sys.argv[2]) if sys.argv[2] else 1
else:
	num = 8
	key = 2
	print "Defaulting to 1"
parts = []
middle = float(num)/2
if num % 2 != 0:
	middle = [int(middle + .5)]
else:
	middle = [int(middle), int(middle+1)]
key_to_str = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"][key]

# note creation
note_parts = []
for x in xrange(num):
	note_parts.append([])
	for y in xrange(num):
		note_ret = []
		for z in xrange(random.randint(1,3)):
			note_ret.append(key+random.choice([i for i,r in enumerate(scale) if r==1]))
		for n in note_ret:
			try:
				used_notes[z]+=1
			except:
				used_notes[z] = 1
		note_parts[x].append(note_ret)

	for z in used_notes:
		if used_notes[z]>=5:
			used_notes[z]=0
			scale[random.choice([i for i,r in enumerate(scale) if r==0])]=1
			scale[z-key]=0
	# print scale


for x in xrange(num):
	parts.append([])
	rand = random.choice(range(num,num*4,num))
	for y in xrange(num):
		y += 1
		if y in middle:
			if len(middle)>1:
				if y==min(middle):
					a=random.choice(range((y-1)*60,y*60,num))
					b=random.choice(range(a,y*60,num))
					c=num*30
					d=num*30 
				else:
					a=num*30
					b=num*30
					c=random.choice(range(a,y*60,num))
					d=random.choice(range(c,(y+1)*60,num))
			else:
				a=(num*30)-rand
				b=a
				c=(num*30)+rand
				d=c
		else:
			if y<min(middle):
				a = random.choice(range((y-1)*60,y*60,num))
				b = random.choice(range(a,y*60,num))
				c = random.choice(range(a,min(y*60,num*30-rand),num))
				d = random.choice(range(c,min((y+1)*60,(num*30-rand)),num))
			else:
				#start
				a = random.choice(range(max((y-1)*60,num*30+rand),y*60,num))
				b = random.choice(range(a,y*60,num))
				#end
				c = random.choice(range(a,y*60,num))
				if(y==num):
					d=num*60
				else:
					d = random.choice(range(c,(y+1)*60,num))
		# print x,y
		parts[x].append((a,b,note_parts[x][y-1],c,d))
# print parts
"""
for i, part in enumerate(parts):
	print "Part {}:".format(i+1)
	for i,x in enumerate(part):
		if x[0]==x[1]:
			a = "{}'{}\"".format(x[0]/60,x[0]%60)
		else:
			a = "{}'{}\"-{}'{}\"".format(x[0]/60,x[0]%60,x[1]/60,x[1]%60)
		if x[3]==x[4]:
			b = "{}'{}\"".format(x[3]/60,x[3]%60)
		else:
			b = "{}'{}\"-{}'{}\"".format(x[3]/60,x[3]%60,x[4]/60,x[4]%60)
		print "Measure {}: {}--{}--{}".format(i+1,a,x[2],b)
#"""

 
########################################################################
class MusicMaker(object):
	""""""
 
	#----------------------------------------------------------------------
	def __init__(self, pdf_file):
		self.c = canvas.Canvas(pdf_file, pagesize=letter)
		self.styles = getSampleStyleSheet()
		self.width, self.height = letter 
	#----------------------------------------------------------------------
	def createDocument(self):
		""""""
		voffset = 65
		
		# create title
		self.c.setFont('Helvetica', 50)
		
		self.c.drawCentredString(4.25*inch,5.5*inch,"{} in {}".format(num,key_to_str))
		self.c.line(2.5*inch,6*inch,6*inch,6*inch)
		self.c.line(2.5*inch,5.875*inch,6*inch,5.875*inch)
		self.c.line(2.5*inch,5.75*inch,6*inch,5.75*inch)
		self.c.line(2.5*inch,5.625*inch,6*inch,5.625*inch)
		self.c.line(2.5*inch,5.5*inch,6*inch,5.5*inch)
		self.c.drawImage("./img/gclef.png", 2.4*inch,5.3*inch, width=23.32,height=60,mask='auto')
		self.c.line(5.95*inch,6*inch,5.95*inch,5.5*inch)
		self.c.rect(5.97*inch,5.5*inch,.03*inch,.5*inch, fill=1)
		self.c.setFont('Helvetica', 10)
		self.c.drawCentredString(4.25*inch,5.1*inch,"A number piece in the style of John Cage's Five.")
		self.c.drawCentredString(4.25*inch,4.95*inch,"Randomly generated by number_pieces.py,")
		self.c.drawCentredString(4.25*inch,4.8*inch,"a python program by Daniel Myers.")

		self.c.showPage()
		self.createParagraph("Performance Notes",0,voffset, self.styles["Title"])
		ptext = """The parts are for voices or instruments or mixture of voices and instruments having the ability to play a twelve tone scale in a two octave range of their choice.<br/>
				All parts begin in the directed key and slowly (or rapidly, diverge)<br/>
				Time brackets are given. As in John Cage's number pieces: <br />
				\"Within these brackets the durations of tones are free, as are their beginnings and endings, which should be \"brushed\" in and out rather than turned on and off.\" <br/>
				<br/>
				<center><b>An explanation for how to read and perform the piece</b></center> <br />
				\"The timings in minutes and seconds used in what are now known as the \"number\" pieces by John Cage are called time brackets. The time brackets that appear to the left of each staff indicate a period of time during which the music on that staff must begin. The time brackets to the right indicate a period of time during which the music on that staff must end. These are flexible time brackets that overlap. The exact placement and duration of the music is free within these limitations. Some of the time brackets (those without arrows) are fixed meaning that the music must begin and end at exactly those periods of time. There should be no attempt to coordinate the different parts.\" Take breaths whenever you need to.
				"""
		p = Paragraph(ptext, self.styles["Normal"])
		p.wrapOn(self.c, self.width-110, self.height)
		p.drawOn(self.c, *self.coord(20, voffset+80, mm))
		
		for l,part in enumerate(parts):
			page = 1
			for i, measure in enumerate(part):
				if i%7==0:
					self.c.showPage()
					self.c.drawCentredString(4.25*inch,10.5*inch,"{}".format(num))
					self.c.drawString(.5*inch,10.1*inch,"Player {}".format(l+1))
					self.c.drawRightString(8*inch,10.1*inch,"number_pieces.py")
					self.c.drawCentredString(4.25*inch,.2*inch,"Player {} | Page {}".format(l+1,page))
					page+=1
					if num<8:
						distance = 9.5/num #1.4
					else:
						if len(part)-i>6:
							distance = 9.5/7
						else:
							distance = 9.5/(len(part)-i)
					# print distance

				if measure[0]==measure[1]:
					a = "{}'{}\"".format(measure[0]/60,measure[0]%60)
				else:
					a = "{}'{}\"↔{}'{}\"".format(measure[0]/60,measure[0]%60,measure[1]/60,measure[1]%60)
				if measure[3]==measure[4]:
					b = "{}'{}\"".format(measure[3]/60,measure[3]%60)
				else:
					b = "{}'{}\"↔{}'{}\"".format(measure[3]/60,measure[3]%60,measure[4]/60,measure[4]%60)
				#draw times
				self.c.drawRightString(2.5*inch,(9.5-(i%7*distance))*inch,"{}".format(a))
				self.c.drawString(6*inch,(9.5-(i%7*distance))*inch,"{}".format(b))
				#draw measure
				self.c.line(2.5*inch,(9.5-(i%7*distance))*inch,6*inch,(9.5-(i%7*distance))*inch)
				self.c.line(2.5*inch,(9.4-(i%7*distance))*inch,6*inch,(9.4-(i%7*distance))*inch)
				self.c.line(2.5*inch,(9.3-(i%7*distance))*inch,6*inch,(9.3-(i%7*distance))*inch)
				self.c.line(2.5*inch,(9.2-(i%7*distance))*inch,6*inch,(9.2-(i%7*distance))*inch)
				self.c.line(2.5*inch,(9.1-(i%7*distance))*inch,6*inch,(9.1-(i%7*distance))*inch)
				self.c.drawImage("./img/gclef.png", 2.5*inch,(8.944-(i%7*distance))*inch, width=18.656,height=48,mask='auto')
				self.c.line(6*inch,(9.5-(i%7*distance))*inch,6*inch,(9.1-(i%7*distance))*inch)
				self.c.drawString(4.25*inch,(8.8-(i%7*distance))*inch,"{}".format(measure[2]))
				for k,note in enumerate(measure[2]):
					note %= 24 #cycle back to middle c instead of high c
					n_p=[0,0,1,1,2,3,3,4,4,5,5,6,7,7,8,8,9,10,10,11,11,12,12,13] #note_placement
					w_s=[0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0] #where sharp?
					k += 1
					if note<2:
						#draw low
						self.c.line((2.5+(k*(6-2.5)/(len(measure[2])+1)))*inch-2,(9-(i%7*distance))*inch,(2.5+(k*(6-2.5)/(len(measure[2])+1)))*inch+14,(9-(i%7*distance))*inch)
					elif note>20:
						#draw high
						self.c.line((2.5+(k*(6-2.5)/(len(measure[2])+1)))*inch-2,(9.6-(i%7*distance))*inch,(2.5+(k*(6-2.5)/(len(measure[2])+1)))*inch+14,(9.6-(i%7*distance))*inch)
					if w_s[note]:
						self.c.drawString((2.5+(k*(6-2.5)/(len(measure[2])+1)))*inch-7,(8.942-(i%7*distance)+(.05*n_p[note]))*inch,"#")
					self.c.drawImage("./img/whole.png", (2.5+(k*(6-2.5)/(len(measure[2])+1)))*inch,(8.946-(i%7*distance)+(.05*n_p[note]))*inch, width=12.23,height=7.99,mask='auto')







 
	#----------------------------------------------------------------------
	def coord(self, x, y, unit=1):
		"""
		# http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
		Helper class to help position flowables in Canvas objects
		"""
		x, y = x * unit, self.height - y * unit
		return x, y    
 
	#----------------------------------------------------------------------
	def createParagraph(self, ptext, x, y, style=None):
		""""""
		if not style:
			style = self.styles["Normal"]
		p = Paragraph(ptext, style=style)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(x, y, mm))
 
	#----------------------------------------------------------------------
	def savePDF(self):
		""""""
		self.c.save()   
 
#----------------------------------------------------------------------
if __name__ == "__main__":
	doc = MusicMaker("Number_Piece_{}_in_{}.pdf".format(num,key_to_str))
	doc.createDocument()
	doc.savePDF()