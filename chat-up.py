import pyrebase
from datetime import datetime
import firebase_admin
from firebase_admin import db, credentials
import pandas as pd
import tabulate
import time
Config = {
  "apiKey": "AIzaSyB_10tblL-oi-IGAPgF8Mt5dpbRh18pUBo",
  "authDomain": "firestore-4dc04.firebaseapp.com",
  "databaseURL": "https://firestore-4dc04.firebaseio.com",
  "projectId": "firestore-4dc04",
  "storageBucket": "firestore-4dc04.appspot.com",
  "messagingSenderId": "457513041638",
  "appId": "1:457513041638:web:7777fb5545f144a9704527",
  "measurementId": "G-0ZJ7WYP7GD"
};
firebase=pyrebase.initialize_app(Config)
dbv=firebase.database()

cred = credentials.Certificate("C:/Users/shreya_s/Desktop/whatsup/firebase_key.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://firestore-4dc04.firebaseio.com/"})
ref = db.reference("/Chat_Up/")
#fetching Session Id
Session_id_count=len(list(ref.get().keys()))

def compose_new_msg( Sessionid, loginid ):
    date_time = (str(datetime.now()).replace(" ",":")).replace(".",":")
    Message = input()
    new = {"Date_Time": str(date_time),
           "Name": loginid,
           "Message": Message,
           "Deleted": "false"
           }
    Session_id_count = len(list(ref.get().keys()))
    if Sessionid != 'Session'+(str(Session_id_count)):
        ''' start msg id from 1'''
        msg_id = "Msg_" + str(1)
        entry = "Chat_Up/" + Sessionid + "/Data/" + str(msg_id)
        db_Update = dbv.child(entry).update(new)

    else:
        Msg_id_list_keys = list((ref.child(Sessionid).child('Data').get()).keys())
        Msg_id_count = len(Msg_id_list_keys) + 1
        msg_id = "Msg_" + str(Msg_id_count)
        entry = "Chat_Up/" + Sessionid + "/Data/" + str(msg_id)
        db_Update = dbv.child(entry).update(new)
def show_msg(SessionID):
    global session_data
    session_data = pd.DataFrame(ref.child(SessionID).child('Data').get().values())
    #print(tabulate(session_data[['Name','Message','Date_Time']],headers='keys'))
    print(session_data[['Name','Message','Date_Time']] )
def get_latest_msg(SessionID):
    last_msg_key = list(ref.child(SessionID).child('Data').get().keys())[-1]
    a=ref.child(SessionID).child('Data').child(last_msg_key).get()
    print(a['Name'], a['Message'], a['Date_Time'])

    '''Msg_id_list_keys = list((ref.child(Sessionid).child('Data').get()).keys())
    current_msg_id=len(Msg_id_list_keys)
    current_msg_show=pd.DataFrame(ref.child(SessionID).child('Data').child('Msg_'+str(current_msg_id)).get())
    print(current_msg_show)
'''
def delete_msg(SessionID, login_id):
    show_msg(SessionID)
    msg_id=int(input("type msg index corresponding to msg you want to delete"))


print("\n###########################     WELCOME TO COMMUNE!!     #######################################\n")
login_id = input("Enter Username to join Commune")
print("Hi "+str(login_id)+"\n")
print('''
    1. Do you wish to join a new session
    2. Do you wish to join an ongoing active session? 
    3. Logout chat room
''')
choice = int(input(str(login_id) + "  Select from the following"))
while(1):
    print('''
            1. Send message?? press S 
            2. Press N if you dont wanna speak up
            3. Delete a message
            4. press exit to logout chat room

        ''')
    if choice==1:
        #fetch last sessonID
        SessionID = 'Session' + str(Session_id_count + 1)

        while(1):
            snd_msg = input("S/N/exit")
            if snd_msg=='S':
                compose_new_msg(SessionID,login_id)
                #Session_id_count = len(list(ref.get().keys()))
                #SessionID = 'Session' + str(Session_id_count + 1)
                get_latest_msg(SessionID)
            elif snd_msg=='N':
                get_latest_msg(SessionID)
            elif snd_msg=='exit':
                print('Exiting Chat Room')
                break
        break
    elif choice==2:
        #msg_send = input('1. Enter "Y" to send message \n2. Enter "N" to exit')
        SessionID = 'Session' + str(Session_id_count)
        print("Current Active Session is Session "+str(Session_id_count))
        print("\nHave a look what have you missed ..\n")
        show_msg(SessionID)
        '''
                                            1. Send message?? press S 
                                            2. Press N if dont wanna send
                                            3. Delete a message
                                            4. press exit to logout chat room
                                        '''
        #msg_send = input('1. Enter "Y" to send message \n2. Enter "N" to exit')

        while(1):
            msg_send = input('S/N/exit')
            if msg_send=='S':
                compose_new_msg(SessionID,login_id)
                time.sleep(3)
                get_latest_msg(SessionID)
            elif msg_send=='N':
                get_latest_msg(SessionID)
            elif msg_send=='exit':
                break
        break
    elif choice==3:
        break
    #print("3. Delete user message")
#Message creation and update

'''elif x==2:
        Message_logs=[]
        print("which msg you want to delete")
        user_id=input(print("enter the user name for which you want to delete the msgs"))
        if ref.child('Session1').child('Data').order_by_child('Name').equal_to(user_id).get():
            a= ref.child('Session1').child('Data').order_by_child('Name').equal_to(user_id).get()
            #b=list(a.items())
            for i in range(1,len(a)+1):
                temp=a['Msg_'+str(i)]['Message']
                Message_logs.append(temp)


    elif x!=2:
        break
'''



'''
cred = credentials.Certificate("C:/Users/dell/Desktop/chat-app/credential.json")
firebase_admin.initialize_app(cred, {
                              'databaseURL': "https://firestore-4dc04.firebaseio.com/"})
ref = db.reference("/Chat_Up/")
ref.child('Session1').child('Data').order_by_child('Message').equal_to('shreyatesting').get()

'''
'''
ref.child('Data').child('Msg_'+str(msg_id)).get()
ref.child('Data').child('Msg_1').order_by_child('Name').get()
ref.child('Data').order_by_child('Message').equal_to('msg1').get()
2 issues-- Msg 10 is getting added under Msg1
Session1 we have index
how to fetch msg and name --- apply index
'''