from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        # Initialize variables
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.Medicine = StringVar()
        self.PatientId = StringVar()
        self.Nhsnumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbtitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                        fg="red", bg="white", font=("Times New Roman", 50, "bold"))
        lbtitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE, font=("Times New Roman", 12, "bold"),
                                   text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE, font=("Times New Roman", 12, "bold"),
                                    text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # Button Frame
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # Details Frame
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # Dataframe Left (Patient Info)
        lblNameTablet = Label(DataFrameLeft, text="Name OF Tablet", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)
        comNameTablet = ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablets, state="readonly",
                                     font=("arial", 12, "bold"), width=33)
        comNameTablet["values"] = ("None", "Acetaminophen", "Adderall", "Amitriptyline", "Amlodipine", "Amoxicillin", "Ativan",
                                   "Atorvastatin", "Benzonatate", "Biktarvy", "Botox", "Brilinta", "Cephalexin", "Ciprofloxacin",
                                   "Citalopram", "Clindamycin", "Doxycycline", "Dupixent", "Entresto", "Entyvio", "Farxiga",
                                   "Fentanyl Patch", "Gabapentin", "Gemtesa", "Humira", "Ibuprofen", "Imbruvica", "Melatonin",
                                   "Meloxicam", "Naltrexone", "Naproxen")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblref = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)
        lblNoOftablets=Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets::", padx=2, pady=6) 
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.NumberofTablets, width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.Lot, width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6) 
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0, sticky=W)
        txtExpDate=Entry (DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose =Label (DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4) 
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose =Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry (DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.SideEffect, width=35)
        txtSideEffect.grid(row=8,column=1)
       
        lblFurtherinfo=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Further Information", padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.FurtherInfo, width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        lblBloodPressure=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2,pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure=Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.BloodPressure, width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2,column=2, sticky=W)
        txtStorage=Entry (DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Storage, width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3,column=2, sticky=W)
        txtMedicine=Entry (DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Medicine, width=35)
        txtMedicine.grid(row=3,column=3, sticky=W)

        lblPatientId=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4,column=3)


        lblNhsNumber=Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhsNumber.grid(row=5,column=2, sticky=W)
        txtNhsNumber=Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Nhsnumber, width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientname.grid(row=6,column=2, sticky=W)
        txtPatientname=Entry (DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.PatientName, width=35)
        txtPatientname.grid(row=6,column=3)


        lblDateOfBirth=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth =Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7,column=3)


        lblPatientAddress= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress =Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8,column=3)

        # Adding all other entry widgets with similar patterns...
        # --------------------------------- Buttons --------------------------------

        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, command=self.iPrescriptionData)
        btnPrescription.grid(row=0, column=0)
        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"),
                             width=23,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)
        
        # Add other buttons similarly...
        # Prescription Button

# Update Button
        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),
                           width=23, command=self.iPrescriptionData)
        btnUpdate.grid(row=0, column=2)
        
# Delete Button
        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),
                          width=23,command=self.iPrescriptionData)
        btnDelete.grid(row=0, column=3)
        
        # Clear Button
        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),
                          width=23,command=self.iPrescriptionData)
        btnClear.grid(row=0, column=4)
        
        # Exit Button
        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),
                         width=23,command=self.iPrescriptionData)
        btnExit.grid(row=0, column=5)
     

        # ---------------------------------- Table --------------------------------
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate",
                                                                 "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # Define headings for table
        self.hospital_table.heading("nameoftable", text="Name Of Table")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")
        self.hospital_table["show"] = "headings"

        self.hospital_table.pack(fill=BOTH, expand=1)

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Paras@12345", database="bank_db")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO HOSPITAL VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                  (self.Nameoftablets.get(), self.ref.get(), self.Dose.get(), self.NumberofTablets.get(),
                                   self.Lot.get(), self.Issuedate.get(), self.ExpDate.get(), self.DailyDose.get(),
                                   self.Storage.get(), self.Nhsnumber.get(), self.PatientName.get(),
                                   self.DateOfBirth.get(), self.PatientAddress.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted successfully")
            except Exception as e:
                messagebox.showerror("Database Error", f"Error due to {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    application = Hospital(root)
    root.mainloop()
