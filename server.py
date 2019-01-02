from socket import * 
import time
import threading
from threading import Event
e=Event()
e1=Event()
#from threading import Lock
#mutex1 = Lock()
#mutex2=Lock()
from Tkinter import *
from functools import partial
root=Tk()
root.title("Server")
root.geometry("500x500")
app=Frame(root)
app.grid()
tog_ks="k"
time_limit=10
slflag=".log"
client_cs="some_socket"
client_cs_flag=0
kill_flag=0
retrive_all_log=0

def set_time():
    global time_limit
    time_limit=var.get()
    print(var.get())

st=Frame(root)
st.grid()
allowed=["chrome","firefox","python","bash","gedit"]
aa_t=""
aa_text=Text(st, width = 70, height =2 , wrap = WORD,fg="green")
def delete_list(da):
    pos=0
    global aa_text
    print(da.get())
    aa_text.delete('1.0', END)
    for i in range(0,len(allowed)):
        if(da.get()==allowed[i]):
            pos=i
        else:
            aa_text.insert(END, allowed[i])
            aa_text.insert(END, " ")
    try:
        del allowed[pos]
    except:
        pass
    da.delete(0,END)
    print(allowed)
    sentence=",".join(allowed)
    #print(aa_text.get(1.0,2.4))
    
def add_list(aa):
    global aa_t
    global aa_text
    allowed.append(aa.get())
    #w = Label(root, text=aa.get(), bg="green", fg="white")
    #w.pack(fill=X)
    aa_t=aa.get()
    #aa_t=aa_t+" "+aa.get()
    aa_text.insert(END, aa_t)
    aa_text.insert(END, " ")
    aa_text.grid(row=3,column=1,columnspan = 10, sticky = W)
    aa.delete(0,END)
    sentence=",".join(allowed)
    print(allowed)

var=IntVar()

def screen():
    global tog_ks
    tog_ks="s"

def god():
    global tog_ks
    if(tog_ks=="k"):
        tog_ks="t"
    else:
        tog_ks="k"

time_stamp=""

def time_int2(t):
	global kill_flag,retrive_all_log
	time.sleep(int(t)*60)
	kill_flag=0
	retrive_all_log=1

	
def time_int(ti):
	global kill_flag
	global time_stamp
	kill_flag=1
	time_thread=threading.Thread(target=time_int2,args=(ti.get(),))
	time_thread.start()

def mac():
    global tog_ks
    tog_ks="m"

mac_addr=""
def mac_recv(cs):
    while(1):
        mdata=cs.recv(4096)
        global mac_addr
        print(mdata)
        mac_addr=mac_addr+" "+mdata
        mac_lbl = Label(st, text = "MAC ADDRESS="+mac_addr)
        mac_lbl.grid(row=14,column=0,columnspan=4,sticky=W)
  
def shutdown():
	global tog_ks
	tog_ks="shutdown"  
    
def add():
    aa_lbl = Label(st, text = "Allowed Apps :")
    aa_lbl.grid(row=2,column=1,sticky=W)
    aa=Entry(st)
    aa.grid(row=2,column=2,sticky=W)
    aa_submit_bttn = Button(st, text = "+", command = partial(add_list,aa))
    aa_submit_bttn.grid(row = 2, column = 3,columnspan=2)
    da_lbl = Label(st, text = "Delete Allowed Apps :")
    da_lbl.grid(row=5,column=1,sticky=W)
    da=Entry(st)
    da.grid(row=5,column=2,sticky=W)
    da_submit_bttn = Button(st, text = "-", command = partial(delete_list,da))
    da_submit_bttn.grid(row = 5, column = 3,columnspan=2)
    aa_lbl = Label(st, text = " ")
    aa_lbl.grid(row=6,column=2,sticky=W)
    aa_lbl = Label(st, text = "Time:",bg="Black",fg="white")
    aa_lbl.grid(row=8,column=2,sticky=W)
    global var
    R1 = Radiobutton(st, text="10", variable=var, value=10,command=set_time)
    R1.grid(row=9,column=0)
    R2 = Radiobutton(st, text="30", variable=var, value=30,command=set_time)
    R2.grid(row=9,column=1)
    R3 = Radiobutton(st, text="40", variable=var, value=40,command=set_time)
    R3.grid(row=9,column=2)
    R4 = Radiobutton(st, text="60", variable=var, value=60,command=set_time)
    R4.grid(row=9,column=3)
    ss_bttn = Button(st, text = "Screenshot", command = screen)
    ss_bttn.grid(row = 10, column = 1)
    ab_bttn = Button(st, text = "ADMIN Mode", command = god)
    ab_bttn.grid(row = 10, column = 2)
    ti_lbl = Label(st, text = "Set Time Interval:")
    ti_lbl.grid(row=11,column=1,sticky=W)
    ti=Entry(st)
    ti.grid(row=11,column=2,sticky=W)
    ti_submit_bttn = Button(st, text = "SET", command = partial(time_int,ti))
    ti_submit_bttn.grid(row = 11, column = 3,columnspan=2)
    shut_bttn = Button(st, text = "Shutdown Computer", command = shutdown)
    shut_bttn.grid(row = 12, column = 2)
    
    

def start():
    st.pack(fill=X)
    lbl=Label(st,text="Welcome to Application Monitor")
    lbl.grid(row=1,column=2,sticky=W)
    add()
   
   
    
def check():
    pas=pent.get()
    flag=pas
    if(flag=="1"):
        app.destroy()
        start()
    else:
        albl=Label(app,text="Enter Again")
        albl.grid(row=7,column=1)


    
lbl=Label(app,text="Welcome to Application Monitor")
lbl.grid(row=0,column=1,columnspan=2,sticky=W)
usr_lb = Label(app, text = "Enter User name")
usr_lb.grid(row=1,column=0,sticky=W)
uent=Entry(app)
uent.grid(row=1,column=1,sticky=W)
pent=Entry(app)
pent.grid(row=2,column=1,sticky=W)
pass_lb= Label(app, text = "Enter Password")
pass_lb.grid(row=2,column=0,sticky=W)
submit_bttn = Button(app, text = "Submit", command = check)
submit_bttn.grid(row = 4, column = 1)

#root.title("Simple GUI")

'''def setInterval(func,time):
	e=threading.Event()
	while not e.wait(time):
		func()
		print("Thread")'''

def ServerData():
    #global sentence
    global allowed
    global cs
    global client
    global tog_ks
    global time_stamp , kill_flag ,retrive_all_log
    global client_cs_flag,client_cs,slflag 
    count1=1
    while(1):
        if(kill_flag==1):
        	print("all",allowed)
		#allowed.append(time_stamp)
		allowed.append(tog_ks)
		sentence=",".join(allowed)
		del allowed[allowed.index(tog_ks)]
	    	if(client_cs_flag==1):
				client_cs.send(slflag)
				connectionSocket=client_cs
				length = connectionSocket.recv(4096)
				connectionSocket.send("test1")
				#print(length)
				myfile = open("new_server"+str(count1)+slflag[1:], 'wb')
				tl=0
				data=b''
				while(len(data) < int(length)):
					recv_data = connectionSocket.recv(4096)
					print("data")
					tl=tl+len(recv_data)
					data+=recv_data
				myfile.write(data)
				print(len(data))
				myfile.close()
				count1+=1
				client_cs_flag=0
		for cs in client:
		    print(cs)
		    try:
		        cs.send(sentence)
		    except:
		        cs.close()
		        print("Client disconnected")
		if(tog_ks=="m"):
		    tog_ks="k"
	elif(kill_flag==0):
		print("Not Killing")
		for cs in client:
		    print(cs)
		    try:
		        cs.send("nk")
		    except:
		        cs.close()
		        print("Client disconnected")
	if(retrive_all_log==1):
		for client_cs in client:
			slflag=",.txt"
			try:
				client_cs.send(slflag)
				connectionSocket=client_cs
				length = connectionSocket.recv(4096)
				connectionSocket.send("test1")
				#print(length)
				myfile = open("new_server"+str(count1)+slflag[1:], 'wb')
				tl=0
				data=b''
				while(len(data) < int(length)):
					recv_data = connectionSocket.recv(4096)
					print("data")
					tl=tl+len(recv_data)
					data+=recv_data
				myfile.write(data)
				print(len(data))
				myfile.close()
				count1+=1
			except:
				client_cs.close()
				print("Client Disconnected")
			retrive_all_log=0
		
	time.sleep(time_limit)
	
	
t1=threading.Thread(target=ServerData)
client=[]




def logClick():
	global slflag
	slflag=",.log"
	print(slflag)
	pass

def screenShotClick():
	global slflag
	slflag=",.jpg"
	print(slflag)
	pass

capp = Tk()
capp.title("Connected Clients ")
capp.geometry('500x500')
logBtn = Radiobutton(capp,text='Log', value=1,command=logClick)
screensBtn = Radiobutton(capp,text='Screen Shot',value=2,  command=screenShotClick)
logBtn.grid(column=0, row=0)
screensBtn.grid(column=4, row=0)

def client_action(cs):
	global client_cs_flag,client_cs
	client_cs_flag=1
	client_cs=cs
	print(cs)

def server(capp):
    global client
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('10.1.10.18',serverPort))
    serverSocket.listen(3)
    print 'Server is ready'
    client=[]
    t1.start()
    client_count=1
    cframe=Frame(capp)
    cframe.grid()
    #setInterval(ServerData,5)
    while 1:
        connectionSocket,addr=serverSocket.accept()
        if(connectionSocket not in client):
            client.append(connectionSocket)
            Button(cframe, text = str(client_count),command=partial(client_action,connectionSocket)).pack()
            print(client)
            #print(cframe.winfo_children())
            #print(child.destroy) 
            client_count+=1
        #ct=threading.Thread(target=sshot,args=(connectionSocket,))
        #ct.start()
        #cm=threading.Thread(target=mac_recv,args=(connectionSocket,))
        #cm.start()
        


t2=threading.Thread(target=server,args=(capp,))
t2.start()
capp.mainloop()
root.mainloop()
	
		

#	sentence=connectionSocket.recv(1024)
#	connectionSocket.close()

