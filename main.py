import threading 
from queue import Queue
import time 
import mouse as mou
import interface as inte
global m
import main2
import average_value_assigner as cal
import interface2 as int4
import os
import time
import speedometer
def firstjob(worker):
	global m
	m=mou.mouse()
	fp=open("data.txt","w")
	
	#fp.close()
	#os.system('cls')
	main2.iris_average=1
	time.sleep(1)
	fp.write('"Ratios "\n {0} \n   {1}\n  iris_ratops \n {2} \n"screen coordinates"\n {3}\niris_ratios \n'.format(main2.ratios , main2.iris,m,main2.iris_ratios))

	#main2.mouselist=m
	main2.callibration=False
	int4.main()

	


	
def secondjob(worker):	
	inte.interface()

def  thirdjob(worker):
	main2.eyes()
def fourthjob(worker):
	speedometer.speed()
	
def threader():
	while  True:

		worker=q.get()
		firstjob(worker)
		q.task_done()	
def threader2():
	while True:
		worker2=q.get()
		secondjob(worker2)
		q.task_done()
def threader3():
	while True:
		worker3=q.get()
		thirdjob(worker3)
		q.task_done()
def threader4():
	while  True:
		worker4=q.get()
		fourthjob(worker4)
		q.task_done()


q=Queue()
t3=threading.Thread(target=threader3)
t3.daemon=True
t3.start()
time.sleep(5)
t2=threading.Thread(target= threader2)
t2.daemon=True
t2.start()
t1= threading.Thread(target = threader)
t1.daemon=True
t1.start()
t4=threading.Thread(target = threader4)
t4.daemon=True
t4.start()







for worker in range(4):
	q.put(worker)
q.join()

global m


