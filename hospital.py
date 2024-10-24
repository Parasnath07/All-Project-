from tkinter import*
import tkinter as tk
from tkinter import ttk
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector
 

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")
        lbtitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("time new roman ",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)
        #---------------------DATAFRAME---------------------------------

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                                 font=(" time new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)
         
        DataFrameRight=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                                 font=("time new roman",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        #--------------------------BUTTON FRAME------------------------------------------------------------------------------------------------------------
           
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)   

        #--------------------------BUTTON FRAME------------------------------------------------------------------------------------------------------------
           
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)   
        
     
        #----------------------------Dataframe left--------------------------------------------------------------------------------------------

        lblNameTablet=Label(DataFrameLeft,text = "Name OF Tablet",font=(" time new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row =0,column=0)

        comNameTablet=ttk.Combobox(DataFrameLeft ,font=("arial",12,"bold"),
                                                                        width=33 )
        comNameTablet["values"]=("None","Acetaminophe","Adderall", "Amitriptyline" ,"Amlodipine","Amoxicillin", "Ativan","Atorvastati",
        "Benzonatate","Biktarvy","Botox","Brilinta","Cephalexin","Ciprofloxacin","Citalopram","Clindamycin","Doxycycline","Dupixent","Entresto","Entyvio",
        "Farxiga","Fentanyl Patch","Gabapentin","Gemtesa","Humira","Ibuprofen","Imbruvica","Melatonin","Meloxicam","Naltrexone","Naltrexone","Naproxen")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)                                                
        
        lblref=Label(DataFrameLeft, font=("arial", "12","bold"), text ="Reference No:", padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry (DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets::", padx=2, pady=6) 
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6) 
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0, sticky=W)
        txtExpDate=Entry (DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose =Label (DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4) 
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose =Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry (DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8,column=1)
       
        lblFurtherinfo=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Further Information", padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        lblBloodPressure=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2,pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure=Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2,column=2, sticky=W)
        txtStorage=Entry (DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3,column=2, sticky=W)
        txtMedicine=Entry (DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtMedicine.grid(row=3,column=3, sticky=W)

        lblPatientId=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtPatientId.grid(row=4,column=3)


        lblNhsNumber=Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhsNumber.grid(row=5,column=2, sticky=W)
        txtNhsNumber=Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientname.grid(row=6,column=2, sticky=W)
        txtPatientname=Entry (DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtPatientname.grid(row=6,column=3)


        lblDateOfBirth=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth =Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtDateOfBirth.grid(row=7,column=3)


        lblPatientAddress= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress =Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35)
        txtPatientAddress.grid(row=8,column=3)
 #---------------------------------Dataframeright-----------------------------------------------------------
        self.txtPrescription=Text(DataFrameRight,font=("arial", 12, "bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
#------------------------------------Buttons-----------------------------------------------------------------------------
        btnPrescription=Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0) 

        btnPrescriptionData=Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12,"bold" ),width=23,height=16,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12,"bold"), width=23,height=16,padx=2, pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button (Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12,"bold"), width=23,height=16, padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button (Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12,"bold"), width=23,height=16, padx=2, pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12,"bold"), width=23,height=16, padx=2, pady=6)
        btnExit.grid (row=0,column=5)
    

if __name__ == "__main__":
    root=tk.Tk()
    application=Hospital(root)
    root.mainloop()
    



