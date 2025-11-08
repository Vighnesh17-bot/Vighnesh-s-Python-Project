import csv
import extras
def tlogin():
    l2=[]
    count=0
    print('You may enter data for CAT 1, CAT 2 or FAT')
    with open('subdatabase.csv','a+',newline='') as file:
         ans='y'
         while ans=='y':
            write=csv.writer(file)
            l1=[]
            l3=[]
            exam=input('Enter exam here : ')
            l1.append(exam)
            write.writerow(l1)
            c='yes'
            while c=='yes':
                sname=input('Enter student name here : ')
                sub=input('Enter sub here ')
                count+=1
                mks=float(input('Enter mks'))
                l2=[sname,sub,mks]
                l3.append(l2)
                c=input('Do you want to add more records (yes/no) ? ')
            ans=input('Do you want to logout (yes/no) ? ')
         write.writerows(l3)
         
