from tkinter import *
from PIL import Image, ImageTk

def main_func(event):

    
    global screen_val
    click_me=event.widget.find_withtag('current')[0]

    txt=canvas.itemcget(click_me,'text')
    if txt == "=":
        try:
            val=eval(screen_val.get())
            
        except Exception as e:
            val='Error'
            print(e)
        screen_val.set(val)
        screen_ent.update ()

    elif txt == 'C':

        screen_val.set('')
        screen_ent.update()

    elif txt == 'del':

        screen_val.set(screen_val.get()[:-1])
        screen_ent.update()

    else:
        screen_val.set(screen_val.get()+txt)
        screen_ent.update ()

        
        
root=Tk()
root.geometry('644x900')
root.title('Canvas Calculator')
try:
    photo=Image.open('C:\\Users\\fc\\Pictures\\Camera Roll\\data\\All Gui tkinter course\\Copilot_20260128_212921.png')
    image=ImageTk.PhotoImage(photo)
    root.iconphoto(False,image)

except Exception as e:
    print(f'error{e}')

f1=Frame(root,bg='#A8DACA',relief=SUNKEN)
f1.pack()

screen_val=StringVar()
screen_ent=Entry(f1,bg='white',textvariable=screen_val,font='Console 40 bold',fg='#E868A0')
screen_ent.pack(fill='x',padx=10,pady=8)

canvas=Canvas(f1,height=600,width=600,bg='#A8DACA')
canvas.pack()





style={'C':{'color':'#22235F',},
       'del':{'color':'#7A4D9F',},
       '=':{'color':'#33ACEC',}}
x1=50
y1=50
x2=150
y2=150
tx1=100
tx2=100
def calculation (x1,y1,x2,y2,tx1,tx2,t,color='#E868A0',f='Concolen 30 bold'):#frame,t,padx=15,pady=10,f='Console 30 bold',bg='#3E3E3E',fg='white')
    
    canvas.create_oval(x1,y1,x2,y2,fill=color)
    text_id=canvas.create_text(tx1,tx2,text=t,font=f,fill='#A8DACA')    
    canvas.tag_bind(text_id,'<Button-1>',main_func)

button_text=[['del','*','/','C',],
             ['-','9','8','7'],
             ['+','6','5','4'],
             ['.','3','2','1'],
             [',','0','%','=']
]

start_x = 60
start_y = 20
button_width = 120
button_height = 110 #120

for row_index, row in enumerate(button_text):
    for col_index, t in enumerate(row):
        x1 = start_x + col_index * button_width
        y1 = start_y + row_index * button_height
        x2 = x1 + button_width
        y2 = y1 + button_height
        tx1 = x1 + button_width // 2
        tx2 = y1 + button_height // 2

        if t in style:
            calculation(x1, y1, x2, y2, tx1, tx2, t, **style.get(t, {}))
        else:
            calculation(x1, y1, x2, y2, tx1, tx2, t)

   


root.mainloop()