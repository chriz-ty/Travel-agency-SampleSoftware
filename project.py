import mysql.connector as dbm
conn=dbm.connect(host="localhost",user="root",passwd=" ",database="software")
cur=conn.cursor()


#clearing python IDLE console
def clear():
    print("\n"*50)


                    #PACKAGE TABLE

   
##to add a new package
def package_new():
    ch='y'
    while(ch.lower()=='y'):
        packages=input("\n\n\tEnter the new package :")
        budget=int(input("\tEnter the buget for the package :"))
        no_days=int(input("\tEnter the duration for the new package :"))
        food_and_accomodation=input("\tEnter whether the food and accommodation are provided or not :")
        data=(packages,budget,no_days,food_and_accomodation)
        cur.execute("insert into packtab(packages,budget,no_days,food_and_accomodation) values(%s,%s,%s,%s)",(data))
        print()
        print()
        print(cur.rowcount,"records inserted")
        conn.commit()
        ch=input("\n\t Do you want to continue inserting??  press y/n :")
        if ch.lower()=='n':
            clear()
            return
        


#to view packages
def pack_view():
    print("\n\nPackage_Id          place                        Buget         No of days        Stay and Food")
    print("===============================================================================================================")
    for x in cur:
        print("%-15s   %-28s  %-15s   %-12s   %-15s"%(x[0],x[1],x[2],x[3],x[4]))
    return
def display():
    cur.execute("select*from packtab")
    pack_view()
    clear()

    
##to update a package
def update_pack():
    so='y'
    while so.lower()=='y':
        plname=input("\n\tEnter the name of the place/destination which you need to update :")
        cur.execute("select*from packtab where packages='{}'".format(plname))
        pack_view()
        Id=int(input("\n\n\tPlease enter the Id of the Packages to be updated :"))
        print("\n\n\tPLEASE ENTER THE NEW DETAILS...")
        place=input("\n\tEnter the Destination :")
        buget=int(input("\tEnter the budget :"))
        days=int(input("\tEnter the Duration :"))
        fa=input("\tEnter whether food and accommodation is provided or not :")
        data=(place,buget,days,fa,Id)
        cur.execute("update packtab set packages=%s,budget=%s,no_days=%s,food_and_accomodation=%s where package_id=%s",(data))
        conn.commit()
        print("\n\n\tRecord Updated Successfully...!")
        ch=input("\n\tDo you want to view the updated list?  press y/n :")
        if ch.lower()=='y':
            display()
            conn.commit()
        else:
            print("\n\n\tTHANK YOU FOR UPDATING...!")
        so=input("\n\n\t\tDo you want to continue updating??  press y/n :")
        if so.lower()=='n':
            clear()
            return


##to delete a package
def del_pack():
    ch='y'
    while(ch.lower()=='y'):
        cur.execute("select*from packtab")
        pack_view()
        nm=input("\n\n\tplease enter the name of the package to be cancelled :")
        cur.execute("select*from packtab where packages='{}'".format(nm))
        pack_view()
        Id=int(input("\n\tPlease enter the id of the package to be deleted :"))
        cur.execute("\tDelete from packtab where package_id='{}'".format(Id))
        conn.commit()
        print("\n\n\tRECORD DELETED SUCCESSFULLY....!")
        ch=input("\n\tDo you want to continue?  press y/n :")
        if ch.lower()=='n':
            clear()
            return
        


                   #ORGANISER TABLE
                     
#to add a new organiser
def new_org():
    ch='y'
    while(ch.lower()=='y'):
        Or_id=input("\n\n\tEnter the new organiser id :")
        name=input("\tEnter the name :")
        dept=input("\tEnter the department of the new member :")
        ph_no=input("\tEnter the phone number :")
        add=input("\tEnter the address :")
        doj=input("\tEnter the date of joining :")
        data=(Or_id,name,dept,ph_no,add,doj)
        cur.execute("insert into orgtab(or_id,name,dept,ph_no,address,doj) values(%s,%s,%s,%s,%s,%s)",(data))
        print()
        print()
        print(cur.rowcount,"records inserted")
        conn.commit()
        ch=input("\n\n\tDo you want to insert more??  Press y/n :")
        if ch.lower()=='n':
            clear()

#to view all organisers
def org_top():
    print("\n\nSI_no     OR_Id      Name          Department           Ph_no          Address                    DOJ")
    print("------------------------------------------------------------------------------------------------------------")
    for a,s,d,f,h,j,k in cur:
                print("%-5s  %-10s  %-15s  %-17s  %-12s  %-27s %-10s"%(a,s,d,f,h,j,k)) 
    return
def view_org():
    while True:
        print("\n\n\tChechk Via....")
        print("\n\t1 :By DEPARTMENT")
        print("\t2 :By DOJ")
        print("\t3 :To VIEW THE FULL LIST")
        print("\t4 :Return")
        opt=int(input("Enter your choice :"))
        if opt==1:
            dpt=input("\n\tEnter  the depatment you need to view :")
            cur.execute("select*from orgtab where dept='{}'".format(dpt))
            org_top()
        elif opt==2:
            dt=input("\n\tEnter the date you need to view :")
            cur.execute("select*from orgtab where doj='{}'".format(dt))
            org_top()
        elif opt==3:
            cur.execute("select*from orgtab")
            org_top()
        elif opt==4:
            return
        else:
            print("\n\n\tPLEASE ENTER A VALID OPTION AND TRY AGAIN :)")
            return
        conn.commit()
        ch=input("\n\n\tDo you want to view/search more??  press y/n :")
        if ch.lower()=='n':
            clear()
            return


##to update the details 
def upd_org():
    while True:
        dpt=input("\n\nEnter the Department Of the member to be updated :")
        cur.execute("select*from orgtab where dept='{}'".format(dpt))
        org_top()
        no=input("\n\nPlease enter the Si no of the record to be updated :")
        print("\n\n\t\tPLEASE ENTER THE NEW DETAILS....")
        Id=input("\n\tEnter the id of the member :")
        nm=input("\tEnter the name of the member :")
        dept=input("\tEnter the department :")
        pno=input("\tEnter the phone no :")
        add=input("\tEnter the address :")
        dj=input("\tEnter the Date of Join :")
        data=(Id,nm,dept,pno,add,dj,no)
        cur.execute("update orgtab set or_id=%s,name=%s,dept=%s,ph_no=%s,address=%s,doj=%s where si_no=%s",(data))
        print("\n\n\tRECORD UPDATED SUCCESSFULLY...!")
        conn.commit()
        ch=input("\n\n\tDo you want to continue??  press y/n  :")
        if ch.lower()=='n':
            clear()
            return
        



##to delete a member
def del_org():
    ch='y'
    while ch.lower()=='y':
        dpt=input("\n\n\tEnter the Department Of the member to be deleted :")
        cur.execute("select*from orgtab where dept='{}'".format(dpt))
        org_top()
        no=input("\n\n\tPlease enter the Si no of the record to be deleted :")
        cur.execute("delete from orgtab where si_no='{}'".format(no))
        print("\n\n\t\tRECORD DELETED.....")
        conn.commit()
        ch=input("\n\nDo you want to delete more??  please press y/n :")
        if ch.lower()=='n':
            clear()
       
                                           #CLIENT TABLE
                          
##to add a client
def add_clnt():
    ch='y'
    while(ch.lower()=='y'):
        cusname=input("\n\n\tEnter the name of the customer :")
        pn_no=input("\tEnter the phone no :")
        add=input("\tEnter the address :")
        pkid=int(input("\tEnter the id of the opted package :"))
        buget=int(input("\tEnter the buget of the opted package :"))
        pdsts=input("\tEnter whether the amount is paid or not :")
        data=(cusname,pn_no,add,pkid,buget,pdsts)
        cur.execute("insert into custab(cusname,pn_no,address,package_id,budget,paid_status)values(%s,%s,%s,%s,%s,%s)",(data))
        print()
        print()
        print(cur.rowcount,"Records Inserted Successfully...!")
        conn.commit()
        ch=input("\n\n\tDo you want to insert more?? press y/n :")
        if ch.lower()=='n':
            clear()



##to view the clients by the organisers                                                     ##
def clnt_top():
    print("\n\nUser Id      Name          Phno             Address                   Package Id     Budget    Paid Status")
    print("------------------------------------------------------------------------------------------------------------------")
    for a,s,d,f,g,h,j in cur:
        print("%-10s %-15s %-15s %-30s %-10s %-10s %-15s"%(a,s,d,f,g,h,j))
    return
def clnt_view():                                                                            ##
    while True:
        print("\n\n\t\tCheck Via......")
        print("\n\t1:BY PLACE OPTED")
        print("\t2:BY PAID STATUS")
        print("\t3:TO VIEW THE FULL LIST")
        ch=int(input("\n\tPlease enter your choice :"))
        if ch==1:
            display()
            Id=int(input("\n\n\tPlease Enter the package id  :"))
            cur.execute("select*from custab where package_id='{}'".format(Id))
            clnt_top()
            ask=input("\n\n\tDo you want to search more?? press y/n :")
            if ask.lower()=='n':
                clear()
                return
        elif ch==2:
            sts=input("\n\n\tEnter whether the budget is paid/not paid :")
            cur.execute("select*from custab where paid_status='{}'".format(sts))
            clnt_top()
            conn.commit()
            ask=input("\n\n\tDo you want to search more?? press y/n :")
            if ask.lower()=='n':
                clear()
                return
        elif ch==3:
            cur.execute("select*from custab")
            clnt_top()
            conn.commit()
            ask=input("\n\n\tDo you want to search more?? press y/n :")
            if ask.lower()=='n':
                clear()
                return
        else:
            print("\n\tPlease enter a valid value and try again :) ")
            
##to view the bio of the clients
def vw_bio():
    Id=int(input("\n\n\tPlease enter your UserId :"))
    cur.execute("select*from custab where user_id='{}'".format(Id))
    clnt_top()
    conn.commit()
    return


##to update the client bio by organisers
def clnto_upd():                                                                                     ##
    while True:
        Id=int(input("\n\n\tPlease enter the User Id of the client :"))
        cur.execute("select*from custab where User_id='{}'".format(Id))
        clnt_top()
        nm=input("\n\n\tEnter the name of the client :")
        pno=input("\tEnter the Phone no  :")
        add=input("\tEnter the address of the client :")
        pkid=int(input("\tEnter the ID of the opted package :"))
        bgt=int(input("\tEnter the calculated buget :"))
        pdst=input("\tConform the paid status :")
        data=(nm,pno,add,pkid,bgt,pdst,Id)
        cur.execute("update custab set cusname=%s,pn_no=%s,address=%s,package_id=%s,budget=%s,paid_status=%s where user_id=%s",(data))
        print()
        print(cur.rowcount,"RECORD UPDATED...!")
        conn.commit()
        ch=input("\n\n\tDo you want to continue??  press y/n  :")
        if ch.lower()=='n':
            clear()
            return
        


##to update the bio of a client by themself

def clnt_upd():
    while True:
        Id=int(input("\n\n\tPlease enter the User Id :"))
        cur.execute("select*from custab where User_id='{}'".format(Id))
        print("\n\t\tYour current bio is :")
        clnt_top()
        print("\n\nYOU COULD ONLY CHANGE THE NAME AND PERSONAL DETAILS HERE..FOR FURTHER UPDATION ON THE PACKAGES, PLEASE CONTACT THE ADMINISTRATORS..")
        nm=input("\n\n\tEnter the name :")
        pno=input("\tEnter the Phone no  :")
        add=input("\tEnter the address :")
        data=(nm,pno,add,Id)
        cur.execute("update custab set cusname=%s,pn_no=%s,address=%s where user_id=%s",(data))
        print()
        print(cur.rowcount,"RECORD UPDATED...!")
        conn.commit()
        ch=input("\n\n\tDo you want to continue??  press y/n  :")
        if ch.lower()=='n':
            clear()
            return




##to delete a client
def del_clnt():
    ch='y'
    while ch.lower()=='y':  
        cur.execute("select*from custab")
        clnt_top()
        conn.commit()
        Id=int(input("\n\n\tEnter the ID of the client to be deleted :"))
        cur.execute("delete from custab where user_id='{}'".format(Id))
        print("\n\n\t\tRECORD DELETED.....")
        conn.commit()
        ch=input("\n\tDo you want to delete more??  please press y/n :")
        if ch.lower()=='n':
            clear()




                                  ##USING CSV CONCEPT##
                  

##to book a package by a customer
def book():
    print("\n\n\t\t\t\t\tBOOKING....")
    clid=int(input("\n\n\tPlease enter yours User ID  :"))
    nm=input("\tPlease enter your name  :")
    print("\n\n\tTHE AVAILABLE PACKAGES...")
    cur.execute("select*from packtab")
    pack_view()
    print("\t\t\tPLEASE FILL UP THE FOLLOWING...")
    pkgid=int(input("\n\n\tPlease enter the Package ID you wish to order :"))
    pls=input("\tPlease enter the corresponding Destination name  :")
    bklst=[clid,nm,pkgid,pls]
    import csv
    with open("project1.csv",'w',newline='')as newfile:
        newfilewriter=csv.writer(newfile)
        newfilewriter.writerow(bklst)
        newfile.close()
    print("\n\n\t\t\tTHE DATA YOU'VE ENTERED IS :")
    with open("project1.csv",'r')as newfile:
        newfilereader=csv.reader(newfile)
        for row in newfilereader:
            for x in row:
                print('\t',x,end=' ')
##            print()
##            print(row)
        newfile.close()
    print("\n\n\tTHANKYOU FOR BOOKING....OUR ADMINISTRATORS WILL CONTACT YOU...")
    print("\n\n\t\t\t\tSEE YOU SOON.... :)")




##to cancel a product by an user

    
def cancel():
    import csv
    print("\n\n\t\t\t\t\tCANCELLATION.....")
    did=int(input("\n\n\tEnter your User ID :"))
    cur.execute("select user_id from custab")
    pkgid=int(input("\tEnter the Package ID you need to cancel  :"))
    lines=list()
    delid=did
    with open("project1.csv",'r')as readfile:
        reader=csv.reader(readfile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field==did:
                    lines.remove(row)
    with open("project1.csv",'w',newline='')as writefile:
        writer=csv.writer(writefile)
        writer.writerows(lines)
        writefile.close()
    print("\n\n\n\t\t\tTHE ORDER CANCELLED SUCCESSFULLY....")
    print("\n\t\t\tTHANKYOU FOR CONTACTING US....")
    print("\n\n\n\t\t\t\t\tSEE YOU SOON  :)")

                            ##MAIN MENU

                           

print("  WELCOME TO SKY HIGH TRAVELS  ".center(100,"*"))
print("  DREAM SKY HIGH :) ;)..!  ".center(100,"*"))
print("Sky High Travels Ltd. Mumbai".center(100))
print("Contact: skyhitravels@gmail.com , Ph. 9355728884,8744888234".center(100))
print()
s='#'*100
print(s.center(100))
p=input("\n\n\n\t\tPress enter key to continue :")
while True:
    print("\n\n\tLogin as :")
    print("\n\t1 :Admin/Organiser")
    print("\t2 :Client/User")
    print("\t3 :Create a new account")
    dis=int(input("\nPlease enter your choice :"))
    if dis==1:
        lgid=[]
        print()
        print()
        print("  EXECUTIVE PANEL  ".center(100,"%"))
        idd=input("\n\n\tPlease Enter your OR_ID :")
        lgid.append(idd)
        b=tuple(lgid)
        cur.execute("select or_id from orgtab")
        sm=cur.fetchall()
        if b not in sm:
            print("\n\t\tWRONG ID...  :(")
            break
        while True:
            print("\n\n\t\tWHAT DO YOU WANT TO DO??")
            print("\n\t\tSELECT THE REQUIRED FIELD :")
            print("\n\t1 :ORGANISER SECTION")
            print("\t2 :PACKAGE SECTION")
            print("\t3 :CLIENT SECTION")
            sh=int(input("\n\n\tPlease enter your choice :"))
            if sh==1:
                print()
                print()
                print(" ORGANISER SECTION ".center(100,'^'))
                print("\n\n\tCONTENTS :")
                print("\n\t1 :ADD A MEMBER")
                print("\t2 :VIEW MEMBERS")
                print("\t3 :UPDATE BIO OF MEMBERS")
                print("\t4 :DELETE A MEMBER")
                print("\t5 :GO BACK")
                print("\t6 :EXIT")
                cho=int(input("\n\n\tPlease enter your choice :"))
                if cho==1:
                    new_org()
                elif cho==2:
                    view_org()
                elif cho==3:
                    upd_org()
                elif cho==4:
                    del_org()
                elif cho==5:
                    q=input("\n\nAre you sure you sure to go back?? ")
                elif cho==6:
                    q=input("\nAre you sure you sure to quit?? ")
                    print()
                    print()
                    print("  THANKYOU..!  ".center(60,'*'))
                    print()
                    print(" VISIT AGAIN..!  ".center(60,'*'))
                    exit()
                else:
                    print("\n\n\t\tPLEASE ENTER A VALID OPTION AND TRY AGAIN :)")
            elif sh==2:
                print()
                print()
                print("  PACKAGE SECTION  ".center(100,'^'))
                print("\n\n\tCONTENTS :")
                print("\n\n\t1 :ADD A NEW PACKAGE")
                print("\t2 :VIEW THE PACKAGES")
                print("\t3 :UPDATE PACKAGE (like changing place name,increase/decresase budget etc.)")
                print("\t4 :CANCEL A PACKAGE")
                print("\t5 :GO BACK")
                print("\t6 :EXIT")
                cho=int(input("Please enter your choice :"))
                if cho==1:
                    package_new()
                elif cho==2:
                    display()
                elif cho==3:
                    update_pack()
                elif cho==4:
                    del_pack()
                elif cho==5:
                    q=input("\n\nAre you sure you sure to go back?? ")
                elif cho==6:
                    q=input("\nAre you sure you sure to quit?? ")
                    print()
                    print()
                    print("  THANKYOU..!  ".center(60,'*'))
                    print()
                    print("  VISIT AGAIN..!  ".center(60,'*'))
                    exit()
                else:
                    print("\n\n\t\tPLEASE ENTER A VALID VALUE ANDD TRY AGAIN :)")
                
                    
            elif sh==3:
                print()
                print()
                print("  CLIENT SECTION  ".center(100,'^'))
                print("\n\n\tCONTENTS :")
                print("\n\n\t1 :ADD A NEW CLIENT")
                print("\t2 :VIEW/SEARCH CLIENTS")
                print("\t3 :UPDATE CLIENT BIO")
                print("\t4 :DELETE A CLIENT")
                print("\t5 :GO BACK")
                print("\t6 :EXIT")
                cho=int(input("\n\tPlease enter your choice :"))
                if cho==1:
                    add_clnt()
                elif cho==2:
                    clnt_view()
                elif cho==3:
                    clnto_upd()
                elif cho==4:
                    del_clnt()
                elif cho==5:
                    q=input("\n\nAre you sure you sure to go back?? ")
                elif cho==6:
                    q=input("\nAre you sure you sure to quit?? ")
                    print()
                    print()
                    print("  THANKYOU..!  ".center(60,'*'))
                    print()
                    print("  VISIT AGAIN..!  ".center(60,'*'))
                    exit()
                else:
                    print("\n\n\tPlease enter the correct choice and try again :)")
    elif dis==2:
        ugid=[]
        print()
        print()
        print("  USER PANEL  ".center(100,'%'))
        idd=int(input("\n\n\tPlease enter your User ID :"))
        ugid.append(idd)
        c=tuple(ugid)
        cur.execute("select user_id from custab")
        mm=cur.fetchall()
        if c not in mm:
            print("\n\n\t\tWRONG ID...  :(")
            break
        while True:
            print("\n\n\t\tWHAT DO YOU WANT TO DO??")
            print("\n\t\tSELECT THE REQUIRED FIELD :")
            print("\n\t1 :VIEW YOUR BIO")
            print("\t2 :VIEW PACKAGES")
            print("\t3 :BOOK A PACKAGE")
            print("\t4 :CANCEL BOOKING")
            print("\t5 :EDIT YOUR BIO")
            print("\t6 :EXIT")
            sho=int(input("\n\n\tPlease enter your choice :"))
            if sho==1:
                vw_bio()
            elif sho==2:
                display()
            elif sho==3:
                book()
            elif sho==4:
                cancel()
            elif sho==5:
                clnt_upd()
            else:
                q=input("\nAre you sure you sure to quit?? ")
                print()
                print()
                print(" THANKYOU..! ".center(60,'*'))
                print()
                print(" VISIT AGAIN..! ".center(60,'*'))
                exit()
            
    elif dis==3:
        print()
        print()
        print("  NEW ACCOUNT  ".center(100,'*'))
        nm=input("\n\n\tPlease enter your name :")
        ph=input("\tPlease enter your phone no :")
        add=input("\tPlease enter your address :")
        data=(nm,ph,add)
        cur.execute("insert into custab(cusname,pn_no,address)values(%s,%s,%s)",(data))
        print()
        print()
        print(cur.rowcount,"Records Inserted Successfully...!")
        conn.commit()
        print("\n\n\tYOUR USER ID IS :")
        cur.execute("select user_id from custab where pn_no='{}'".format(ph))
        for i in cur:
            a=[i]
            print("\t\t\t",i[0])
        print("\n\n\tPLEASE USE THIS ID TO LOGIN NEXT TIME :)")
        upq=input("\n\n\tDo you want to book a package??  press y/n  :")
        if upq.lower()=='y':
            book()
        else:
            print("\n\n\t\tFOR FURTHER DETAILS PLEASE CONTACT OUR ADMINISTRATORS :)")
            print()
            print()
            print("  THANKYOU FOR CONTACTING US :)  ".center(60,'*'))
            
        
    else:
        print("\n\n\tPlease enter the correct choice and try again :)")
        
        
           
                
            
                
        
        
            
        
        
 
