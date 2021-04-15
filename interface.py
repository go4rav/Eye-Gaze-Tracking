from tkinter import *

counter=1

def interface():

	root = Tk()
	root.config(background="black")
	root.wm_attributes('-fullscreen'
	                   , 'true')
	

	
	#root.geometry("1366x768")
	def onClick1(event):
		global counter
		counter-=1

		if counter==0:
			button1.destroy()
			frame1.destroy()
			counter=1

	    
	    
	def onClick2(event):  
	    
	    global counter
	    counter-=1
	    if counter==0:
	    	button2.destroy()
	    	frame2.destroy()
	    	counter=1

	def onClick3(event):
		
		global counter
		counter-=1
		if counter==0:
			button3.destroy()
			frame3.destroy()
			
			counter=1


	def onClick4(event):
	   
	    global counter
	    counter-=1
	    if counter==0:
	    	button4.destroy()
	    	frame4.destroy()
	    	counter=1

	def onClick5(event):
	    
	    global counter
	    counter-=1
	    if counter==0:
	    	button5.destroy()
	    	frame5.destroy()
	    	counter=1

	def onClick6(event):
	    
	    global counter
	    counter-=1
	    if counter==0:
	    	button6.destroy()
	    	frame6.destroy()
	    	counter=1

	def onClick7(event):
	    
	    global counter
	    counter-=1
	    if counter==0:
	    	button7.destroy()
	    	frame7.destroy()
	    	counter=1

	def onClick8(event):
	    
	    global counter
	    counter-=1
	    if counter==0:
	    	button8.destroy()
	    	frame8.destroy()
	    	counter=1

	def onClick9(event):
	    
	    
	    global counter
	    counter-=1
	    if counter==-1:
	    	button9.destroy()
	    	frame9.destroy()
	    	root.destroy()

	root.rowconfigure(0, weight = 0)
	root.rowconfigure(1, weight = 1)
	root.rowconfigure(2, weight = 0)

	root.columnconfigure(0, weight = 0)
	root.columnconfigure(1, weight = 1)
	root.columnconfigure(2, weight = 0)


	frame1 = Frame(root,highlightbackground="black",width=455,height=256,highlightthickness=2,bd=0)
	button1=Button(frame1,text="1",bg="cyan")
	button1.grid(row=0,column=0)
	frame1.grid(row=0,column=0)
	frame2 = Frame(root)
	button2=Button(frame2,text="2",bg="cyan")
	button2.grid(row=0,column=0)
	frame2.grid(row=0,column=1)
	frame3 = Frame(root)
	button3=Button(frame3,text="3",bg="cyan")
	button3.grid(row=0,column=0)
	frame3.grid(row=0,column=2)
	frame4 = Frame(root)
	button4=Button(frame4,text="4",bg="cyan")
	button4.grid(row=0,column=0)
	frame4.grid(row=1,column=0)
	frame5 = Frame(root)
	button5=Button(frame5,text="5",bg="cyan")
	button5.grid(row=0,column=0)
	frame5.grid(row=1,column=1)
	frame6 = Frame(root)
	button6=Button(frame6,text="6",bg="cyan")
	button6.grid(row=0,column=0)
	frame6.grid(row=1,column=2)
	frame7 = Frame(root)
	button7=Button(frame7,text="7",bg="cyan")
	button7.grid(row=0,column=0)
	frame7.grid(row=2,column=0)
	frame8 = Frame(root)
	button8=Button(frame8,text="8",bg="cyan")
	button8.grid(row=0,column=0)
	frame8.grid(row=2,column=1)
	frame9 = Frame(root)
	button9=Button(frame9,text="9",bg="cyan")
	button9.grid(row=0,column=0)
	frame9.grid(row=2,column=2)

	button1.bind('<Button-1>',onClick1)
	button2.bind('<Button-1>',onClick2)
	button3.bind('<Button-1>',onClick3)
	button4.bind('<Button-1>',onClick4)
	button5.bind('<Button-1>',onClick5)
	button6.bind('<Button-1>',onClick6)
	button7.bind('<Button-1>',onClick7)
	button8.bind('<Button-1>',onClick8)
	button9.bind('<Button-1>',onClick9)


	root.mainloop()

