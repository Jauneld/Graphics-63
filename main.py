#Jaunel Deans
#12/6/23
#k

from cmu_graphics import *
from cmu_graphics.shape_logic import opacityTest
#square

  #Rect(left, top, width, height, fill = 'color', border = 'color', borderWidth = number))
  #Rect((5), (10), (100), (100), fill='goldenrod', border='black', borderWidth=5, opacity=60)

  #circle 
  #Circle(centerX, centerY, radius, fill = 'color', border = 'color', borderWidth = number))
  #Circle(50, 100, 50, fill='salmon', border='black', borderWidth=5)

  ##***Other shapes***

  #Oval
  #Oval(centerX, centerY, width, height, fill = 'color', border = 'color', borderWidth = number))
  #Oval(300, 100, 70, 100, fill='olive', border='black', borderWidth=5)

  #Star
  #Star(centerX, centerY, radius, points, fill = 'color', border = 'color', borderWidth = number)
  #Star(300, 200, 40, 10, fill='darkOrange', border='black', borderWidth=5)

  #Regular Polygons
  #RegularPolygon(centerX, centerY, radius, points, fill = 'color', border = 'color', borderWidth = number)
  #RegularPolygon(80, 300, 90, 5, fill = 'orchid', border = 'black', borderWidth = 5)

  #Polygon
  #Polygon(point1X, point1Y, point2X, point2Y, point3X, point3Y, fill = 'color', border = 'color', borderWidth = number)
  #Polygon(350, 370, 200, 100, 200, 200, fill = 'darkSeaGreen', border ='black', borderWidth = 5)

  # tuple (dashWidth, gapWidth).
  ##***Try***

  #square
  #Rect((400), (0), (100), (100), fill='darkRed', border='white', borderWidth=3, dashes=(5, 10) )

  #circle 
  #Circle(200, 30, 20, fill='darkOrange', border='white', borderWidth=5,dashes=(5, 10))

  #Oval
  #Oval(70, 100, 300, 100, fill='darkKhaki', border='white', borderWidth=5, dashes=(5, 10))

  #Star
  #Star(400, 70, 40, 10, fill='darkGreen', border='white', borderWidth=5)

  #Regular Polygons
  #RegularPolygon(80, 300, 90, 5, fill = 'darkTurquoise', border = 'white', borderWidth = 5, dashes=(5, 10))

  #Polygon
  #Polygon(50, 50, 200, 50, 200, 200, fill = 'mistyRose', border ='white', borderWidth = 5, dashes=(5, 10))


  ##***Line***
  #Line(x1, y1, x2, y2, fill = 'color', lineWidth = number, dashes = (dashWidth, gapWidth))
  #Line(400, 0, 400, 400, fill='darkBlue', lineWidth=10, dashes=(5, 10))
  #Label
  #Label('text', x, y, fill = 'color', size = number, font = 'font', bold = True/false, italic = True/false, underline = True/false, align = 'left/center/right')
  #Label(('Hello'), 265, 265, fill='yellow', size=30, font='arial', bold=True, italic=True)#Circle(100,200,150,fill=gradient('lightGoldenrodYellow','gold','yellow','pink','deepPink','hotPink','pink','lightPink', start='bottom'))

                      #*********REAL CODE*********

app.background = 'darkSlateGray'
def name():
  Label(('Johack'), 20, 20, fill='yellow', size=30, font='cinzel', bold=True)

def background():
  Circle(200,200,150,fill=gradient('deepSkyBlue','lightBlue', 'lightCyan',start='bottom-right'),border = 'black', borderWidth=5)

def face():
  Circle(200,200,70,fill="burlyWood")
  Oval(170, 190, 40, 40, fill='black')
  Oval(230, 190, 20, 20, fill='oliveDrab',opacity=70)
  Line(150, 150, 200, 270, fill='black', lineWidth=5, opacity=70)
  Line(170, 243, 230, 243, fill='black', lineWidth=7, dashes = True)
  Polygon(200, 225, 200, 200, 230, 210, fill = 'brown',opacity=60)

def body():
  Rect(160,275,80,20,fill=gradient('wheat','burlyWood', 'sienna', start='left'), rotateAngle=90)
  Circle(200,360,70,fill="red")
  Oval(200, 350, 200, 10, fill='black', opacity=60)

def fillIn():
  Circle(200,425,98,fill="darkSlateGray")
  Rect(100,330,200,30,fill="darkSlateGray")

background()
body()
fillIn()
face()
name()

#hair()
#clothes()
cmu_graphics.run()