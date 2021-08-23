class SuperUser:
    def __init__(self):
        self.member=dict([])
        self.regimen=dict([])
        
    def create_member(self,Name,Age,Gender,Mobile_num,Email,BMI,Membership_duration):
        self.member[Mobile_num]={}
        self.member[Mobile_num]['Name']=Name
        self.member[Mobile_num]['Age']=Age
        self.member[Mobile_num]['Gender']=Gender
        self.member[Mobile_num]['Mobile_num']=Mobile_num
        self.member[Mobile_num]['Email']=Email
        self.member[Mobile_num]['BMI']=int(BMI)
        if Membership_duration==1 or Membership_duration==3 or Membership_duration==6 or Membership_duration==12:
            self.member[Mobile_num]['Membership_duration']=int(Membership_duration)
            
        else:
            self.member[Mobile_num]['Membership_duration']=1
            
    def view_member(self):
        for i in self.member.keys():
            print('Name :',self.member[i]['Name'])
            print('Age :',self.member[i]['Age'])
            print('Gender :',self.member[i]['Gender'])
            print('Mobile_num :',self.member[i]['Mobile_num'])
            print('Email :',self.member[i]['Email'])
            print('BMI :',self.member[i]['BMI'])
            print('Membership_duration :',self.member[i]['Membership_duration'])
            
            
            
    def delete_member(self,Mobile_num):
        
        return self.member.pop(Mobile_num)
    
    def update_member(self,Mobile_num,Membership_duration):
        self.member[Mobile_num]['Membership_duration']=int(Membership_duration)
        
    def create_regimen(self,BMI):
        self.regimen[BMI]={}
        if float(BMI)<18.5:
            self.regimen[BMI]['Mon']='Chest'
            self.regimen[BMI]['Tue']='Biceps'
            self.regimen[BMI]['Wed']='Rest'
            self.regimen[BMI]['Thu']='Back'
            self.regimen[BMI]['Fri']='Triceps'
            self.regimen[BMI]['Sat']='Rest'
            self.regimen[BMI]['Sun']='Rest'
            
        elif int(BMI)<25:
            self.regimen[BMI]['Mon']='Chest'
            self.regimen[BMI]['Tue']='Biceps'
            self.regimen[BMI]['Wed']='Cardio/Abs'
            self.regimen[BMI]['Thu']='Back'
            self.regimen[BMI]['Fri']='Triceps'
            self.regimen[BMI]['Sat']='Legs'
            self.regimen[BMI]['Sun']='Rest'
            
        elif int(BMI)<30:
            self.regimen[BMI]['Mon']='Chest'
            self.regimen[BMI]['Tue']='Biceps'
            self.regimen[BMI]['Wed']='Abs/Cardio'
            self.regimen[BMI]['Thu']='Back'
            self.regimen[BMI]['Fri']='Triceps'
            self.regimen[BMI]['Sat']='Legs'
            self.regimen[BMI]['Sun']='Cardio'
            
        elif int(BMI)>=30:
            self.regimen[BMI]['Mon']='Chest'
            self.regimen[BMI]['Tue']='Biceps'
            self.regimen[BMI]['Wed']='Cardio'
            self.regimen[BMI]['Thu']='Back'
            self.regimen[BMI]['Fri']='Triceps'
            self.regimen[BMI]['Sat']='Cardio'
            self.regimen[BMI]['Sun']='Cardio'
            
            
    def view_regimen(self):
        return self.regimen
    
    def delete_regimen(self,BMI):
        self.regimen.pop(int(BMI))
        return self.regimen
    
    def update_regimen(self,BMI,week_no,value):
        week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        self.regimen[BMI][week[week_no-1]]=value
        
        
class User:
    def __init__(self,member,regimen,phone):
        self.myprofile=member[phone]
        self.myregimen=regimen
        self.phone=phone
        
    def view_myprofile(self):
        return self.myprofile

    
    def view_myregimen(self):
        return self.myregimen[self.myprofile['BMI']]
    
obj=SuperUser()
opt=True
while(opt==True):
    print('Do you want to enter as User or SuperUser')
    print('For SuperUser press 1 and for User press 2')
    val = int(input())
    if val==1:
        sup=True
        print('Congrats for successful login as SuperUser')
        while(sup==True):
            print('\n 1.create member \n 2.view member \n 3.delete member \n 4.update member \n 5.create regimen \n 6.view regimen \n 7.delete regimen \n 8.update regimen')
            num=int(input())
            if num==1:
                name=input('Enter Name :')
                age=input('Enter Age :')
                gender=input('Enter Gender :')
                mob=input('Enter mob :')
                email=input('Enter email :')
                BMI=float(input('Enter BMI :'))
                mem_dur=int(input('Enter Membership_duration :'))
                obj.create_member(name,age,gender,mob,email,BMI,mem_dur)
            elif num==2:
                print(obj.view_member())
            elif num==3:
                Mobile_num=input("Enter the mobile number for the user which should be deleted : ")
                obj.delete_member(Mobile_num)
            elif num==4:
                Mobile_num=input('Enter mobile number to be updated: ')
                Membership_duration=int(input('Enter the duration upto which you want to extend: '))
                try:
                    obj.update_member(Mobile_num,Membership_duration)
                except:
                    print('Invalid user details please enter again')
                    
            elif num==5:
                create_reg=float(input('Enter the BMI index for creating the regimen : '))
                obj.create_regimen(int(create_reg))
            elif num==6:
                print(obj.view_regimen())
            elif num==7:
                BMI=input('enter the BMI you want to delete : ')
                try:
                    obj.delete_regimen(BMI)
                except:
                    print('Invalid number')
                    
            elif num==8:
                create_reg=float(input('Enter the BMI index for updating the regimen : '))
                week=input('enter the week Mon to Sun: ')
                week_no=int(input('enter the week number : '))
                value=input('enter the value of regimen: ')
                try:
                    obj.update_regimen(int(create_reg),week_no,value)
                except:
                    print('Invalid user details')
                    
            
            
            else:
                print('Invalid Input')
                
            print('Do you want to enter more y/n')
            sup = input() == 'y'
    elif val == 2:
        user1=True
        print('congrats you are a user now')
        while(user1==True):
            phone=input('Enter phone number')
            try:
                obj2=User(obj.member,obj.regimen,phone)
                print('select any of the following \n 1.view myregimen \n2.view myprofile \n 0.exit')
                val=int(input())
                if val==1:
                     print(obj2.view_myregimen())
                    
                elif val==2:
                     print(obj2.view_myprofile())
                        
                elif val==0:
                    user1=False
                    
            except:
                 print('Invalid details!!!')
                    
                    
        
                    
    
                
    
        