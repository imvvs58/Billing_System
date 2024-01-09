from tkinter import *
from tkinter import messagebox
import random , os , tempfile, smtplib

# ============= Functional Part ======================

# ============= Email Frame ======================

def clear():

    sanitizer_txt.delete(0,END)
    mask_txt.delete(0,END)
    hand_gloves_txt.delete(0,END)
    dettol_txt.delete(0,END)
    newsprin_txt.delete(0,END)
    bandage_txt.delete(0,END)

    rice_txt.delete(0,END)
    oil_txt.delete(0,END)
    wheat_txt.delete(0,END)
    daal_txt.delete(0,END)
    sugar_txt.delete(0,END)
    tea_txt.delete(0,END)

    pepsi_txt.delete(0,END)
    coka_txt.delete(0,END)
    sprite_txt.delete(0,END)
    dew_txt.delete(0,END)
    frooti_txt.delete(0,END)
    maaza_txt.delete(0,END)

    sanitizer_txt.insert(0,0)
    mask_txt.insert(0,0)
    hand_gloves_txt.insert(0,0)
    dettol_txt.insert(0,0)
    newsprin_txt.insert(0,0)
    bandage_txt.insert(0,0)

    rice_txt.insert(0,0)
    oil_txt.insert(0,0)
    wheat_txt.insert(0,0)
    daal_txt.insert(0,0)
    sugar_txt.insert(0,0)
    tea_txt.insert(0,0)

    pepsi_txt.insert(0,0)
    coka_txt.insert(0,0)
    sprite_txt.insert(0,0)
    dew_txt.insert(0,0)
    frooti_txt.insert(0,0)
    maaza_txt.insert(0,0)

    medicalPriceEntry.delete(0,END)
    groceryPriceEntry.delete(0,END)
    coolDrinkPriceEntry.delete(0,END)
    medicalTaxEntry.delete(0,END)
    groceryTaxEntry.delete(0,END)
    coolDrinkTaxEntry.delete(0,END)

    cname_txt.delete(0,END)
    pname_txt.delete(0,END)
    cbill_txt.delete(0,END)

    textarea.delete(1.0,END)


# ============= Email Frame ======================
def send_email():
    def send_mail():
        try: 
            ob=smtplib.SMTP('smpt.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            msg=emailTextarea.get(1.0, END)
            reciever_addrs=recipientEntry.get()
            ob.sendmail(senderEntry.get(),reciever_addrs,msg)
            ob.quit()
            messagebox.showinfo('Successful', 'Bill is Successfully Sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', "Something went Wrong",parent=root1)
        


    if textarea.get(1.0, END)=='\n':
    # mail = textarea.get(1.0, END)
    # if mail == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Send Email')
        root1.iconbitmap("mails.ico")
        root1.config(bg='#FFB6C1')
        root1.resizable(0,0)

        # ============= Sender ======================
        senderFrame = LabelFrame(root1, text='SENDER',font=('arial',16,'bold'),bd=6,bg='#FFB6C1',fg='Black')
        senderFrame.grid(row=0,column=0, padx=40, pady=20)

        senderLable= Label(senderFrame,text="Sender's Email ID: ",font=('arial',13,'bold'),bg='#FFB6C1',fg='Black')
        senderLable.grid(row=0,column=0,padx=10,pady=8)
        

        senderEntry= Entry(senderFrame,font=('arial',12),bd=7,width=28, relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8,sticky='w')
        senderEntry.insert(END, 'mech2018batch@gmail.com')

        passwordLable= Label(senderFrame,text="Password: ",font=('arial',13,'bold'),bg='#FFB6C1',fg='Black')
        passwordLable.grid(row=1,column=0,padx=10,pady=8, sticky='w')

        passwordEntry= Entry(senderFrame,font=('arial',12),bd=7,width=28, relief=RIDGE)
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        # ============= Recipent ======================

        recipientFrame = LabelFrame(root1, text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='#FFB6C1',fg='Black')
        recipientFrame.grid(row=1,column=0, padx=40, pady=20)

        recipientLable= Label(recipientFrame,text="Email ID: ",font=('arial',13,'bold'),bg='#FFB6C1',fg='Black')
        recipientLable.grid(row=0,column=0,padx=10,pady=8, sticky='w')

        recipientEntry= Entry(recipientFrame,font=('arial',12),bd=7,width=28, relief=RIDGE)
        recipientEntry.grid(row=0,column=1,padx=10,pady=8)
        
        messageLable= Label(recipientFrame,text="Message: ",font=('arial',13,'bold'),bg='#FFB6C1',fg='Black')
        messageLable.grid(row=1,column=0,padx=10,pady=8, sticky='w')

        emailTextarea= Text(recipientFrame,font=('arial',13,'bold'), bd=2,width=42,height=11,relief=SUNKEN)
        emailTextarea.grid(row=2,column=0, columnspan=2)
        emailTextarea.delete(1.0, END)
        emailTextarea.insert(END, textarea.get(1.0, END).replace('=',''))

        sendButton= Button(root1,text='SEND',font=('arial',13,'bold'),width=15,bg='gray50', command=send_mail)
        sendButton.grid(row=2, column=0, pady=20)

        root1.mainloop()
# =============  ======================




def print_bills():
    bill_content = textarea.get(1.0, END)
    
    if bill_content == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file_path = tempfile.mktemp('.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(bill_content)
        
        os.startfile(file_path, 'Print')


def search_bills():
    file_name = cbill_txt.get()
    bill_path = f'bills/{file_name}.txt'

    if os.path.exists(bill_path):
        with open(bill_path, 'r', encoding='utf-8') as f:
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')



if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno('Conformation', 'Do You Want To Save The Bill ?')
    if result:
        bill_content=textarea.get(1.0, END)
        with open(f'bills/{billnumber}.txt', 'w', encoding='utf-8') as file:
            file.write(bill_content) 
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully ')
        billnumber=random.randint(1000,9999)


billnumber=random.randint(1000,9999)
def bill_Genrate():
    if cname_txt.get()=='' or pname_txt.get()=='':
        messagebox.showerror('Error !', 'Customer Details Are Required*')
    elif medicalPriceEntry.get()=='' and groceryPriceEntry.get()=='' and coolDrinkPriceEntry.get()=='':
        messagebox.showerror('Error !', 'No Products Are Selected*')
    elif medicalPriceEntry.get()=='₹. 0' and groceryPriceEntry.get()=='₹. 0' and coolDrinkPriceEntry.get()=='₹. 0':
        messagebox.showerror('Error !', 'No Products Are Selected*')

    else :
        textarea.delete(1.0, END)
        textarea.insert(END, '\t    **Welcome Customer**')
        textarea.insert(END, f'\n  Bill Number: {billnumber}')
        textarea.insert(END, f'\n  Customer Name: {cname_txt.get()}')
        textarea.insert(END, f'\n  Customer Phone Number: +91 {pname_txt.get()}')
        # ============= Product , Quantity , Price ======================
        textarea.insert(END,    f'\n=============================================')
        textarea.insert(END, f'\n Product \t\t Quantity \t\t Price')
        textarea.insert(END,    f'\n=============================================')

        if sanitizer_txt.get()!='0':
            textarea.insert(END, f' Sanitizer\t\t {sanitizer_txt.get()}\t\t ₹. {sanitizervalue}')
        if mask_txt.get()!='0':
            textarea.insert(END, f'\n Mask \t\t {mask_txt.get()}\t\t ₹. {maskvalue}')
        if hand_gloves_txt.get()!='0':
            textarea.insert(END, f'\n Hand Gloves \t\t {hand_gloves_txt.get()}\t\t ₹. {handglovesvalue}')
        if dettol_txt.get()!='0':
            textarea.insert(END, f'\n Dettol \t\t {dettol_txt.get()}\t\t ₹. {dettolvalue}')
        if newsprin_txt.get()!='0':
            textarea.insert(END, f'\n Newsprin \t\t {newsprin_txt.get()}\t\t ₹. {newsprinvalue}')
        if bandage_txt.get()!='0':
            textarea.insert(END, f'\n Bandage \t\t {bandage_txt.get()}\t\t ₹. {bandagevalue}')

        if rice_txt.get()!='0':
            textarea.insert(END, f'\n Rice \t\t {rice_txt.get()}\t\t ₹. {ricepricevalue}')
        if oil_txt.get()!='0':
            textarea.insert(END, f'\n Oil \t\t {oil_txt.get()}\t\t ₹. {oilpricevalue}')
        if wheat_txt.get()!='0':
            textarea.insert(END, f'\n Wheat \t\t {wheat_txt.get()}\t\t ₹. {wheatpricevalue}')
        if daal_txt.get()!='0':
            textarea.insert(END, f'\n Daal \t\t {daal_txt.get()}\t\t ₹. {daalpricevalue}')
        if sugar_txt.get()!='0':
            textarea.insert(END, f'\n Sugar \t\t {sugar_txt.get()}\t\t ₹. {sugarpricevalue}')
        if tea_txt.get()!='0':
            textarea.insert(END, f'\n Tea \t\t {tea_txt.get()}\t\t ₹. {teapricevalue}')

        if pepsi_txt.get()!='0':
            textarea.insert(END, f'\n Pepsi \t\t {pepsi_txt.get()}\t\t ₹. {pepsiprice}')
        if coka_txt.get()!='0':
            textarea.insert(END, f'\n Coco Cola \t\t {coka_txt.get()}\t\t ₹. {cokeprice}')
        if sprite_txt.get()!='0':
            textarea.insert(END, f'\n Sprite \t\t {sprite_txt.get()}\t\t ₹. {spriteprice}')
        if dew_txt.get()!='0':
            textarea.insert(END, f'\n Dew \t\t {dew_txt.get()}\t\t ₹. {dewprice}')
        if frooti_txt.get()!='0':
            textarea.insert(END, f'\n Frooti \t\t {frooti_txt.get()}\t\t ₹. {frootiprice}')
        if maaza_txt.get()!='0':
            textarea.insert(END, f'\n Maaza \t\t {maaza_txt.get()}\t\t ₹. {maazaprice}')
        
        textarea.insert(END,    f'\n---------------------------------------------')
        if medicalTaxEntry.get() !='₹. 0.0':
            textarea.insert(END,f'\n Medical Tax \t\t\t ₹. {mTax}')
        if groceryTaxEntry.get() !='₹. 0.0':
            textarea.insert(END,f'\n Grocery Tax \t\t\t ₹. {gTax}')
        if coolDrinkTaxEntry.get() !='₹. 0.0':
            textarea.insert(END,f'\n Cool Drinks Tax \t\t\t ₹. {cdTax}')
        textarea.insert(END,    f'\n---------------------------------------------')
        textarea.insert(END,f'\n Total Amount  \t\t\t\t ₹. {totalAmount}')
        textarea.insert(END,f'\n Total Tax  \t\t\t\t ₹.  {totalTax}')
        textarea.insert(END,f'\n\n Total Bill \t\t\t\t ₹. {totalPrice}')
        textarea.insert(END,    f'\n---------------------------------------------')
    save_bill()

def total():
    # ============= Medical ======================
    global sanitizervalue,maskvalue,handglovesvalue,dettolvalue,newsprinvalue,bandagevalue, mTax,totalMedicalPrice
    sanitizervalue=int(sanitizer_txt.get())*20
    maskvalue=int(mask_txt.get())*5
    handglovesvalue=int(hand_gloves_txt.get())*10
    dettolvalue=int(dettol_txt.get())*25
    newsprinvalue=int(newsprin_txt.get())*3
    bandagevalue=int(bandage_txt.get())*2
    
    totalMedicalPrice= sanitizervalue+maskvalue+handglovesvalue+dettolvalue+newsprinvalue+bandagevalue
    medicalPriceEntry.delete(0, END)
    medicalPriceEntry.insert(0, f'₹. {totalMedicalPrice}')
    mTax= totalMedicalPrice*0.05
    medicalTaxEntry.delete(0, END)
    medicalTaxEntry.insert(0,f'₹. {mTax}')

    # ============= Grocery ======================
    global ricepricevalue, oilpricevalue, wheatpricevalue, daalpricevalue, sugarpricevalue, teapricevalue,gTax,totalGroceryPrice
    ricepricevalue = int(rice_txt.get())*200   
    oilpricevalue = int(oil_txt.get())*200
    wheatpricevalue = int(wheat_txt.get())*220
    daalpricevalue = int(daal_txt.get())*240
    sugarpricevalue = int(sugar_txt.get())*50
    teapricevalue = int(tea_txt.get())*55

    totalGroceryPrice= ricepricevalue+oilpricevalue+wheatpricevalue+daalpricevalue+sugarpricevalue+teapricevalue
    groceryPriceEntry.delete(0, END)
    groceryPriceEntry.insert(0,f'₹. {totalGroceryPrice}')

    gTax= totalGroceryPrice*0.05
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0,f'₹. {gTax}')



    # ============= Coldrinks ======================
    global pepsiprice, cokeprice, spriteprice, dewprice,frootiprice, maazaprice,cdTax,totalCooldrinkPrice
    pepsiprice = int(pepsi_txt.get())*20
    cokeprice = int(coka_txt.get())*20 
    spriteprice = int(sprite_txt.get())*20
    dewprice = int(dew_txt.get())*20
    frootiprice = int(frooti_txt.get())*20
    maazaprice = int(maaza_txt.get())*20

    totalCooldrinkPrice=pepsiprice+cokeprice +spriteprice+dewprice +frootiprice+maazaprice
    coolDrinkPriceEntry.delete(0, END)
    coolDrinkPriceEntry.insert(0,f'₹. {totalCooldrinkPrice}')
    cdTax= totalCooldrinkPrice*0.04
    coolDrinkTaxEntry.delete(0, END)
    coolDrinkTaxEntry.insert(0,f'₹. {cdTax}')


    global totalPrice, totalAmount, totalTax
    totalAmount= totalMedicalPrice+totalGroceryPrice+ totalCooldrinkPrice
    totalTax = mTax+gTax+cdTax
    totalPrice = totalMedicalPrice+mTax+totalGroceryPrice+gTax+ totalCooldrinkPrice+cdTax






# ============= GUI Part ====================== 
root = Tk()
root.title("VVS Mega Mart")
root.geometry("1270x685")
root.iconbitmap("rupee.ico")
heading = Label(root,text='Billing Here', font=('times new roman',30,'bold'), bg="gray20", fg="gold",bd=20, relief=RIDGE)
heading.pack (fill=X)

# =============customer retail details======================
F1 = LabelFrame(root, text='Customer Details',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8, relief=RIDGE)
F1.pack(fill=X)
cname_lbl =Label(F1, text='Customer Name:',font=('times new roman',15,'bold'),bg="gray20", fg="#B0E0E6")
cname_lbl.grid(row=0, column=0,padx=20)
cname_txt =Entry(F1, font=('arial',13),bd=7,width=18)
cname_txt.grid(row=0, column=1, padx=8)
# cname_txt.insert(END, 'XYZ')

pname_lbl =Label(F1, text='Phone Number:',font=('times new roman',15,'bold'),bg="gray20", fg="#B0E0E6")
pname_lbl.grid(row=0, column=2,padx=20, pady=2)
pname_txt =Entry(F1, font=('arial',13),bd=7,width=18)
pname_txt.grid(row=0, column=3, padx=8)
pname_txt.insert(END, 'xxxxxxxxxx  ')

cbill_lbl =Label(F1, text='Bill Number:',font=('times new roman',15,'bold'),bg="gray20", fg="#B0E0E6")
cbill_lbl.grid(row=0, column=4,padx=20, pady=2)
cbill_txt =Entry(F1, font=('arial',13),bd=7,width=18)
cbill_txt.grid(row=0, column=5, padx=8)

sbtn=Button(F1,text="Search",font=('arial',12,'bold'),bd=10,width=12,bg='#c5d1f9', command=search_bills) 
sbtn.grid(row=0, column=6, padx=20, pady=8)

# ============= Frame ======================
productFrame=Frame(root)
productFrame.pack(pady=3)

# ============= Medical ======================

medicalFrame = LabelFrame(productFrame, text='Medical',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
medicalFrame.grid(row=0,column=0)

sanitizer_lbl = Label(medicalFrame,text='Senitizer: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
sanitizer_lbl.grid(row=0,column=0,pady=9,sticky='W')
sanitizer_txt = Entry(medicalFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
sanitizer_txt.grid(row=0, column=1,pady=9,padx=10)
sanitizer_txt.insert(0,0)

mask_lbl = Label(medicalFrame,text='Mask: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
mask_lbl.grid(row=1,column=0,pady=9,sticky='W')
mask_txt = Entry(medicalFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
mask_txt.grid(row=1, column=1,pady=9,padx=10)
mask_txt.insert(0,0)

hand_gloves_lbl = Label(medicalFrame,text='Hand Gloves: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
hand_gloves_lbl.grid(row=2,column=0,pady=9,sticky='W')
hand_gloves_txt = Entry(medicalFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
hand_gloves_txt.grid(row=2, column=1,pady=9,padx=10)
hand_gloves_txt.insert(0,0)

dettol_lbl = Label(medicalFrame,text='Dettol: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
dettol_lbl.grid(row=3,column=0,pady=9,sticky='W')
dettol_txt = Entry(medicalFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
dettol_txt.grid(row=3, column=1,pady=9,padx=10)
dettol_txt.insert(0,0)

newsprin_lbl = Label(medicalFrame,text='Newsprin: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
newsprin_lbl.grid(row=4,column=0,pady=9,sticky='W')
newsprin_txt = Entry(medicalFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
newsprin_txt.grid(row=4, column=1,pady=9,padx=10)
newsprin_txt.insert(0,0)

bandage_lbl = Label(medicalFrame,text='Bandage: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
bandage_lbl.grid(row=5,column=0,pady=9,sticky='W')
bandage_txt = Entry(medicalFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
bandage_txt.grid(row=5, column=1,pady=9,padx=10)
bandage_txt.insert(0,0)

# ============= Grocery Item ======================

GroceryItemsFrame = LabelFrame(productFrame, text='Grocery Items',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
GroceryItemsFrame.grid(row=0,column=1)

rice_lbl = Label(GroceryItemsFrame,text='Rice: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
rice_lbl.grid(row=0,column=0,pady=9,sticky='W')
rice_txt = Entry(GroceryItemsFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
rice_txt.grid(row=0, column=1,pady=9,padx=10)
rice_txt.insert(0,0)

oil_lbl = Label(GroceryItemsFrame,text='Oil: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
oil_lbl.grid(row=1,column=0,pady=9,sticky='W')
oil_txt = Entry(GroceryItemsFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
oil_txt.grid(row=1, column=1,pady=9,padx=10)
oil_txt.insert(0,0)

wheat_lbl = Label(GroceryItemsFrame,text='Wheat: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
wheat_lbl.grid(row=2,column=0,pady=9,sticky='W')
wheat_txt = Entry(GroceryItemsFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
wheat_txt.grid(row=2, column=1,pady=9,padx=10)
wheat_txt.insert(0,0)

daal_lbl = Label(GroceryItemsFrame,text='Daal: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
daal_lbl.grid(row=3,column=0,pady=9,sticky='W')
daal_txt = Entry(GroceryItemsFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
daal_txt.grid(row=3, column=1,pady=9,padx=10)
daal_txt.insert(0,0)

sugar_lbl = Label(GroceryItemsFrame,text='Sugar: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
sugar_lbl.grid(row=4,column=0,pady=9,sticky='W')
sugar_txt = Entry(GroceryItemsFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
sugar_txt.grid(row=4, column=1,pady=9,padx=10)
sugar_txt.insert(0,0)

tea_lbl = Label(GroceryItemsFrame,text='Tea: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
tea_lbl.grid(row=5,column=0,pady=9,sticky='W')
tea_txt = Entry(GroceryItemsFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
tea_txt.grid(row=5, column=1,pady=9,padx=10)
tea_txt.insert(0,0)

# ============= Cool Drinks ======================

cooldFrame = LabelFrame(productFrame, text='Cool Drinks',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
cooldFrame.grid(row=0,column=2)

pepsi_lbl = Label(cooldFrame,text='Pepsi: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
pepsi_lbl.grid(row=0,column=0,pady=9,sticky='W')
pepsi_txt = Entry(cooldFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
pepsi_txt.grid(row=0, column=1,pady=9,padx=10)
pepsi_txt.insert(0,0)

coka_lbl = Label(cooldFrame,text='Coca Cola: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
coka_lbl.grid(row=1,column=0,pady=9,sticky='W')
coka_txt = Entry(cooldFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
coka_txt.grid(row=1, column=1,pady=9,padx=10)
coka_txt.insert(0,0)

sprite_lbl = Label(cooldFrame,text='Sprite: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
sprite_lbl.grid(row=2,column=0,pady=9,sticky='W')
sprite_txt = Entry(cooldFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
sprite_txt.grid(row=2, column=1,pady=9,padx=10)
sprite_txt.insert(0,0)

dew_lbl = Label(cooldFrame,text='Dew: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
dew_lbl.grid(row=3,column=0,pady=9,sticky='W')
dew_txt = Entry(cooldFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
dew_txt.grid(row=3, column=1,pady=9,padx=10)
dew_txt.insert(0,0)

frooti_lbl = Label(cooldFrame,text='Frooti: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
frooti_lbl.grid(row=4,column=0,pady=9,sticky='W')
frooti_txt = Entry(cooldFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
frooti_txt.grid(row=4, column=1,pady=9,padx=10)
frooti_txt.insert(0,0)

maaza_lbl = Label(cooldFrame,text='Maaza: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
maaza_lbl.grid(row=5,column=0,pady=9,sticky='W')
maaza_txt = Entry(cooldFrame,font=('times new roman', 15, 'bold'),width=16, bd=5)
maaza_txt.grid(row=5, column=1,pady=9,padx=10)
maaza_txt.insert(0,0)

# ============= Bill Area ======================

billframe = Frame(productFrame,bd=8,relief=GROOVE,bg='#c5d1f9')
billframe.grid(row=0, column=3,padx=10)

billarea=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bg='#bed6ea',bd=7,relief=GROOVE)
billarea.pack(fill=X)

scbar=Scrollbar(billframe,orient=VERTICAL)
scbar.pack(side=RIGHT, fill=Y)

textarea=Text(billframe,height=20,width=45, yscrollcommand=scbar.set)
textarea.pack()
scbar.config(command=textarea.yview)

# ============= bill Menu ======================

billmenuFrame = LabelFrame(root, text='Bill Menu',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
billmenuFrame.pack()

medicalPrice = Label(billmenuFrame,text='Medical Price: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
medicalPrice.grid(row=0,column=0,pady=9,sticky='W')
medicalPriceEntry = Entry(billmenuFrame,font=('times new roman', 15, 'bold'),width=15, bd=5)
medicalPriceEntry.grid(row=0, column=1,pady=9,padx=10)
# medicalPriceEntry.insert(0,0)

groceryPrice = Label(billmenuFrame,text='Grocery Price: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
groceryPrice.grid(row=1,column=0,pady=9,sticky='W')
groceryPriceEntry = Entry(billmenuFrame,font=('times new roman', 15, 'bold'),width=15, bd=5)
groceryPriceEntry.grid(row=1, column=1,pady=9,padx=10)
# groceryPriceEntry.insert(0,0)

coolDrinkPrice = Label(billmenuFrame,text='Cool Drink Price: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
coolDrinkPrice.grid(row=2,column=0,pady=9,sticky='W')
coolDrinkPriceEntry = Entry(billmenuFrame,font=('times new roman', 15, 'bold'),width=15, bd=5)
coolDrinkPriceEntry.grid(row=2, column=1,pady=9,padx=10)
# coolDrinkPriceEntry.insert(0,0)

medicalTax = Label(billmenuFrame,text='Medical Tax: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
medicalTax.grid(row=0,column=2,pady=9,sticky='W')
medicalTaxEntry = Entry(billmenuFrame,font=('times new roman', 15, 'bold'),width=15, bd=5)
medicalTaxEntry.grid(row=0, column=3,pady=9,padx=10)
# medicalTaxEntry.insert(0,0)

groceryTax = Label(billmenuFrame,text='Grocery Tax: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
groceryTax.grid(row=1,column=2,pady=9,sticky='W')
groceryTaxEntry = Entry(billmenuFrame,font=('times new roman', 15, 'bold'),width=15, bd=5)
groceryTaxEntry.grid(row=1, column=3,pady=9,padx=10)
# groceryTaxEntry.insert(0,0)

coolDrinkTax = Label(billmenuFrame,text='Cool Drink Tax: ',font=('times new roman',15,'bold'),bg="gray20", fg="gold",bd=8)
coolDrinkTax.grid(row=2,column=2,pady=9,sticky='W')
coolDrinkTaxEntry = Entry(billmenuFrame,font=('times new roman', 15, 'bold'),width=15, bd=5)
coolDrinkTaxEntry.grid(row=2, column=3,pady=9,padx=10)
# coolDrinkTaxEntry.insert(0,0)

# ============= Button Frame ======================

buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=('arial',13,'bold'),bd=5,width=12,bg='#912CEE',fg='Black',pady=10, command=total)
totalButton.grid(row=0,column=0, pady=20, padx=5)

BillButton=Button(buttonFrame,text="Generate Bill",font=('arial',13,'bold'),bd=5,width=12,bg='#808A87',fg='Black',pady=10, command=bill_Genrate)
BillButton.grid(row=0,column=1, pady=20, padx=5)

printButton=Button(buttonFrame,text="Print",font=('arial',13,'bold'),bd=5,width=12,bg='#3bab37',fg='Black',pady=10, command=print_bills)
printButton.grid(row=0,column=2, pady=20, padx=5)

emailButton=Button(buttonFrame,text="Email",font=('arial',13,'bold'),bd=5,width=12,bg='#FFB6C1',fg='Black',pady=10,command=send_email)
emailButton.grid(row=0,column=3, pady=20, padx=5)

clearButton=Button(buttonFrame,text="Clear",font=('arial',13,'bold'),bd=5,width=12,bg='#ff0000',fg='Black',pady=10, command=clear)
clearButton.grid(row=0,column=4, pady=20, padx=5)



















root.mainloop()
