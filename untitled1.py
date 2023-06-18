import tkinter
import tkinter.messagebox
from twilio.rest import Client

def sendSms(message,toNumber):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        if (message.get()!= None and toNumber.get() != None):
            msg = str(message.get())
            rec = str(toNumber.get())
            message = client.messages.create(body=msg,from_='',to= rec)
            print(message.sid)
            tkinter.messagebox.showinfo('Success', 'Message sent successfully')
    
        #Create root window
root = tkinter.Tk()
        #Set title of root window
root.title("SMS CLIENT")
        #Create top frame
top_frame = tkinter.Frame(root)
        #Create bottom frame
bottom_frame = tkinter.Frame(root)
        #Create a label
header = tkinter.Label(top_frame, text = "SMS Sending App")
        #Pack the label
header.pack(side = 'top')
        #Label for TO number
to = tkinter.Label(top_frame, text = "To: ")
to.pack(side = 'left')
        #Create an entry widget for TO: number
toNumber = tkinter.Entry(top_frame, width = 20)
toNumber.pack(side = 'left')
        #Create an entry widget
message = tkinter.Entry(bottom_frame, width = 150)
        #Create button
send = tkinter.Button(bottom_frame, text = "Send SMS", command = sendSms(message,toNumber))
        #pack message entry and send button
message.pack(side = 'left')
send.pack(side = 'left')
        #pack frames
top_frame.pack()
bottom_frame.pack()
tkinter.mainloop()
