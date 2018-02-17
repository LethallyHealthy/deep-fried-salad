from tkinter import*

def sendMessage():
   msg_list.insert(END, "user: %s" % (E1.get()))
   E1.delete(0, END)
 
def pushEnter(event):
   sendMessage()






root= Tk()
root.title("Not Skype")
messages_frame = Frame(root)

my_msg = StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = Listbox(messages_frame, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(fill=BOTH)
messages_frame.pack(fill=BOTH)

text_frame = Frame(root, height=1)
#L1 = Label(text_frame, text="Message Box")
#L1.pack(side=LEFT)

E1 = Entry(text_frame)
E1.bind("<Return>", pushEnter)
E1.pack(side=LEFT, expand = TRUE, fill=BOTH)

sendbutton = Button(text_frame, text ="Send", command = sendMessage, bg="blue", fg="white")
sendbutton.pack(fill=BOTH, side=RIGHT)
text_frame.pack(fill=X)



def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
menubar = Menu(root)
contactsmenu = Menu(menubar, tearoff=0)
contactsmenu.add_command(label="New", command=donothing)
contactsmenu.add_separator()
contactsmenu.add_command(label="Amy Hedwig", command=donothing)
contactsmenu.add_command(label="Francesca Risquet", command=donothing)
contactsmenu.add_command(label="Allah Bishar", command=donothing)
contactsmenu.add_command(label="Zhun Chang", command=donothing)

contactsmenu.add_separator()

contactsmenu.add_command(label="Delete", command=donothing)
menubar.add_cascade(label="Contacts", menu=contactsmenu)
archivemenu = Menu(menubar, tearoff=0)
archivemenu.add_command(label="Clear", command=donothing)

archivemenu.add_separator()

archivemenu.add_command(label="Yesterday", command=donothing)
archivemenu.add_command(label="This Week", command=donothing)
archivemenu.add_command(label="This Month", command=donothing)
archivemenu.add_command(label="This Year", command=donothing)
archivemenu.add_command(label="Select Year to View", command=donothing)

menubar.add_cascade(label="Archive", menu=archivemenu)
optionsmenu = Menu(menubar, tearoff=0)
optionsmenu.add_command(label="Text", command=donothing)
optionsmenu.add_command(label="Notifications", command=donothing)
optionsmenu.add_command(label="Cursor", command=donothing)
optionsmenu.add_command(label="Block", command=donothing)
optionsmenu.add_command(label="Log Out", command=root.quit)
menubar.add_cascade(label="Options", menu=optionsmenu)

root.config(menu=menubar)

root.mainloop()
