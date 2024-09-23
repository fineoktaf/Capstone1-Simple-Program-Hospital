## **RSUD SANJIWANI**

## Program for Hospital

# Any Six Feature :
# 1. All Patient Data
# 2. Add New Patient
# 3. Update Patient Data
# 4. Filter Patient by KTP or BPJS
# 5. Sort Patient Data by poli / clinic
# 6. Delete Patient by filter feature

# 2 user : Doctor and Admin
# - Doctor can access all feature except delete feature and update diagnose only in update feature
# - Admin can access all feature execpt update diagnose in update feature

# In this program we have 6 clinic or poli : 
# 1. Obgyn 
# 2. Internist
# 3. Dental
# 4. Cardiology
# 5. Pulmonology
# 6. Neurology



from datetime import datetime

# Database Data Pasien
patients = [
    {"Medical Record Number": "001","KTP": "317506671012345","BPJS": "00012217788","Name": "Saprudin","Birthdate": "1996-01-01","Gender": "Male","Poli": "Cardiology","Diagnosis": "Hypertension","Registration Date": "2017-09-10","Visit Date": "2024-09-02"},
    {"Medical Record Number": "002","KTP": "317888888888888","BPJS": "00012237721","Name": "Tiara Ahmad","Birthdate": "1998-02-01","Gender": "Female","Poli": "Obgyn","Diagnosis": "Pregnancy","Registration Date": "2022-01-18","Visit Date": "2024-09-22"},
    {"Medical Record Number": "003","KTP": "123677724488034","BPJS": "98765432106","Name": "Saskia Gotik","Birthdate": "1999-01-03","Gender": "Female","Poli": "Dental","Diagnosis": "Caries","Registration Date": "2004-06-17","Visit Date": "2024-09-18"},
    {"Medical Record Number": "004","KTP": "875638323222233","BPJS": "00012267899","Name": "Andini Astuti","Birthdate": "1997-01-01","Gender": "Female","Poli": "Cardiology","Diagnosis": "Hypertension","Registration Date": "2014-09-18","Visit Date": "2024-09-18"},
    {"Medical Record Number": "005","KTP": "317564982023244","BPJS": "00012233333","Name": "Sutomo","Birthdate": "2002-01-11","Gender": "Male","Poli": "Pulmonology","Diagnosis": "Asthma","Registration Date": "2004-11-20","Visit Date": "2024-09-18"},
    {"Medical Record Number": "006","KTP": "619384389934343","BPJS": "00012245671","Name": "Putra Prabowo","Birthdate": "2003-01-15","Gender": "Male","Poli": "Neurology","Diagnosis": "Epilepsy","Registration Date": "1999-09-10","Visit Date": "2024-09-18"},
    {"Medical Record Number": "007","KTP": "763232943943034","BPJS": "00012222222","Name": "Siska Utomo","Birthdate": "1990-04-01","Gender": "Female","Poli": "Internist","Diagnosis": "Diabetic","Registration Date": "2020-09-08","Visit Date": "2024-09-18"},
    {"Medical Record Number": "008","KTP": "317506671096004","BPJS": "00012278122","Name": "Ineke Putri","Birthdate": "2000-07-08","Gender": "Female","Poli": "Cardiology","Diagnosis": "ECG","Registration Date": "2021-09-11","Visit Date": "2024-08-18"},
    {"Medical Record Number": "009","KTP": "317534390909099","BPJS": "00012277777","Name": "Ni Putu Ayu","Birthdate": "1987-01-01","Gender": "Female","Poli": "Obgyn","Diagnosis": "Pregnancy","Registration Date": "2024-07-18","Visit Date": "2024-09-17"},
    {"Medical Record Number": "010","KTP": "231648494839399","BPJS": "00012238888","Name": "Kartika Putri","Birthdate": "1970-10-26","Gender": "Female","Poli": "Dental","Diagnosis": "Oral Infections","Registration Date": "2022-01-10","Visit Date": "2024-09-18"},
    {"Medical Record Number": "011","KTP": "277793997392921","BPJS": "00012265656","Name": "Ahmad Sahroni","Birthdate": "1993-05-04","Gender": "Male","Poli": "Cardiology","Diagnosis": "Hypertension","Registration Date": "2019-09-28","Visit Date": "2024-09-22"},
    {"Medical Record Number": "012","KTP": "223889278382392","BPJS": "00012211111","Name": "Titik Puspa","Birthdate": "2001-10-01","Gender": "Female","Poli": "Cardiology","Diagnosis": "Hypertension","Registration Date": "2019-09-28","Visit Date": "2024-08-18"},
    {"Medical Record Number": "013","KTP": "317666666666999","BPJS": "00012299999","Name": "Brono Mars","Birthdate": "1990-11-01","Gender": "Male","Poli": "Neurology","Diagnosis": "Celebral Palsy","Registration Date": "2012-09-18","Visit Date": "2024-09-16"},
    {"Medical Record Number": "014","KTP": "317675432900006","BPJS": "00012290909","Name": "Veronika","Birthdate": "2007-01-09","Gender": "Female","Poli": "Internist","Diagnosis": "Fever","Registration Date": "2023-11-27","Visit Date": "2024-08-15"},
    {"Medical Record Number": "015","KTP": "317635219993030","BPJS": "00012213131","Name": "Michael Wongso","Birthdate": "2013-01-07","Gender": "Male","Poli": "Internist","Diagnosis": "Kidney Disease","Registration Date": "2021-10-18","Visit Date": "2024-09-18"},
    {"Medical Record Number": "016","KTP": "317607080991111","BPJS": "00012214141","Name": "Kelvin Sanjaya","Birthdate": "1998-12-01","Gender": "Male","Poli": "Pulmology","Diagnosis": "Pneumonia","Registration Date": "2001-09-18","Visit Date": "2024-09-21"},
    {"Medical Record Number": "017","KTP": "317699991212122","BPJS": "00012215151","Name": "Farhan Maulana","Birthdate": "1990-10-10","Gender": "Male","Poli": "Cardiology","Diagnosis": "Hypertension","Registration Date": "2023-09-18","Visit Date": "2024-09-21"},
    {"Medical Record Number": "018","KTP": "444447782398990","BPJS": "00012216161","Name": "Krisna Putra","Birthdate": "1993-11-11","Gender": "Male","Poli": "Dental","Diagnosis": "Caries","Registration Date": "2024-01-11","Visit Date": "2024-09-18"},
    {"Medical Record Number": "019","KTP": "317402019734733","BPJS": "00012217171","Name": "Rayyanza","Birthdate": "1991-06-07","Gender": "Male","Poli": "Internist","Diagnosis": "Fever","Registration Date": "2024-09-18","Visit Date": "2024-09-19"},
    {"Medical Record Number": "020","KTP": "388892000125675","BPJS": "00012218181","Name": "Kartika Putri","Birthdate": "2017-01-01","Gender": "Female","Poli": "Obgyn","Diagnosis": "Pregnancy","Registration Date": "2023-12-18","Visit Date": "2024-09-20"},

]

#Function to feature read all patient data
def read_patients():
    if patients:
        # Header
        print(f"\n{'Medical Record':<15}{'KTP':<20}{'BPJS':<15}{'Name':<20}{'Birthdate':<15}{'Gender':<10}{'Poli':<15}{'Diagnosis':<20}{'Reg Date':<12}{'Visit Date':<12}")
        print("="*152)

        # Display all patients' data in a formatted table
        for patient in patients:
            print(f"{patient['Medical Record Number']:<15}{patient['KTP']:<20}{patient['BPJS']:<15}{patient['Name']:<20}{patient['Birthdate']:<15}{patient['Gender']:<10}{patient['Poli']:<15}{patient['Diagnosis']:<20}{patient['Registration Date']:<12}{patient['Visit Date']:<12}")
    else:
        print("\nNo patients in the system.\n")


# Function to feature add new patient

def add_patient():
    while True:
        print("\nNew Patient")
        
        new_record_number = str(len(patients) + 1).zfill(3)  
        while True:
            ktp = int(input("Enter KTP Number: "))
            if any(patient["KTP"] == ktp for patient in patients):
                print("KTP already exists. Please enter a different KTP number.")
            else:
                break
        while True:
            bpjs = int(input("Enter BPJS Number: "))
            if any(patient["BPJS"] == bpjs for patient in patients):
                print(" BPJS already exists. Please enter a different BPJS number.")
            else:
                break

        name = input("Enter Name: ")
        birthdate = input("Enter Birthdate (YYYY-MM-DD): ")
        gender = input("Enter Gender (Male/Female): ")
        poli = input("Enter Clinic (Poli): ")
        diagnosis = input("Enter Diagnosis: ")
        registration_date = datetime.now().strftime("%Y-%m-%d") 
        visit_date = datetime.now().strftime("%Y-%m-%d")  

        new_patient = {
            "Medical Record Number": new_record_number,
            "KTP": ktp,
            "BPJS": bpjs,
            "Name": name,
            "Birthdate": birthdate,
            "Gender": gender,
            "Poli": poli,
            "Diagnosis": diagnosis,
            "Registration Date": registration_date,
            "Visit Date": visit_date,
        }
        patients.append(new_patient)
        print(f"\nPatient {name} successfully added with Medical Record Number: {new_record_number}.\n")

        more_data = input("Do you want to add more data for a patient? (YES/NO): ")
        if more_data.upper() != "YES":
            break

            
# Function to feature sort patients by Poli
def sort_patients():
    poli_name = input("\nEnter poli/clinic : ").capitalize()
    
    filtered_patients = [patient for patient in patients if patient["Poli"] == poli_name]
    
    if filtered_patients:
        print(f"\nPatients visiting {poli_name} clinic:")
        print(f"\n{'Medical Record':<18}{'KTP':<20}{'BPJS':<15}{'Name':<20}{'Birthdate':<15}{'Gender':<10}{'Poli':<15}{'Diagnosis':<20}{'Reg Date':<12}{'Visit Date':<12}")
        print("="*152)
        for patient in filtered_patients:
            print(f"{patient['Medical Record Number']:<18}{patient['KTP']:<20}{patient['BPJS']:<15}{patient['Name']:<20}{patient['Birthdate']:<15}{patient['Gender']:<10}{patient['Poli']:<15}{patient['Diagnosis']:<20}{patient['Registration Date']:<12}{patient['Visit Date']:<12}")
    else:
        print(f"\nNo patients found in {poli_name} clinic.")
    

# Function to featurefind patients
# filter by KTP or BPJS
def filter_patient():
    id_type = input("\nSearch by KTP/BPJS? ").upper()
    id_number = input(f"Enter {id_type} Number: ")

    for patient in patients:
        if patient[id_type] == id_number:
            print("\nPatient data found:")
            print(f"\n{'Medical Record':<18}{'KTP':<20}{'BPJS':<15}{'Name':<20}{'Birthdate':<15}{'Gender':<10}{'Poli':<15}{'Diagnosis':<20}{'Reg Date':<12}{'Visit Date':<12}")
            print("="*152)
            print(f"{patient['Medical Record Number']:<18}{patient['KTP']:<20}{patient['BPJS']:<15}{patient['Name']:<20}{patient['Birthdate']:<15}{patient['Gender']:<10}{patient['Poli']:<15}{patient['Diagnosis']:<20}{patient['Registration Date']:<12}{patient['Visit Date']:<12}")
            return patient
    print("\nNo patient found with that ID number.")
    return None

# Function to feature update patient data
# Admin can update all data execpt diagnosis, doctor can only update diagnosis
def update_patient(user):
    patient = filter_patient()
    if patient:
        if user == "admin":
            print(f"\nCurrent Data:")
            print(f"{'Medical Record':<18}{'KTP':<20}{'BPJS':<15}{'Name':<20}{'Birthdate':<15}{'Gender':<10}{'Poli':<15}{'Diagnosis':<20}{'Reg Date':<12}{'Visit Date':<12}")
            print("="*152)
            print(f"{patient['Medical Record Number']:<18}{patient['KTP']:<20}{patient['BPJS']:<15}{patient['Name']:<20}{patient['Birthdate']:<15}{patient['Gender']:<10}{patient['Poli']:<15}{patient['Diagnosis']:<20}{patient['Registration Date']:<12}{patient['Visit Date']:<12}")

            patient["Name"] = input(f"Update Name ({patient['Name']}): ") or patient["Name"]
            patient["Birthdate"] = input(f"Update Birthdate ({patient['Birthdate']}): ") or patient["Birthdate"]
            patient["Poli"] = input(f"Update Clinic ({patient['Poli']}): ") or patient["Poli"]
            print("\nPatient data successfully updated.\n")
        elif user == "doctor":
            patient["Diagnosis"] = input(f"Update Diagnosis ({patient['Diagnosis']}): ") or patient["Diagnosis"]
            print("\nDiagnosis successfully updated.\n")

       

# Function to feature delete data patient
# admin can delete data filtered by KTP or BPJS number
def delete_patient():
    patient = filter_patient()
    if patient:
        print(f"\nPatient to delete:")
        print(f"{'Medical Record':<18}{'KTP':<20}{'BPJS':<15}{'Name':<20}{'Birthdate':<15}{'Gender':<10}{'Poli':<15}{'Diagnosis':<20}{'Reg Date':<12}{'Visit Date':<12}")
        print("="*152)
        print(f"{patient['Medical Record Number']:<18}{patient['KTP']:<20}{patient['BPJS']:<15}{patient['Name']:<20}{patient['Birthdate']:<15}{patient['Gender']:<10}{patient['Poli']:<15}{patient['Diagnosis']:<20}{patient['Registration Date']:<12}{patient['Visit Date']:<12}")

        confirm = input(f"\nAre you sure you want to delete patient {patient['Name']}? (yes/no): ").lower()
        if confirm == "yes":
            patients.remove(patient)
            print(f"\nPatient with Medical Record Number {patient['Medical Record Number']} successfully deleted.\n")
        else:
            print("\nDeletion canceled.\n")

   

# Main program function
def main():
    user = input("\nAre You (Admin/Doctor)? ").lower()
    
    while True:
        print("\nWelcome to RSUD Sanjiwani, Please Choose Menu")
        print("1. All Patient Data")
        print("2. Add New Patient" if user == "admin" else "")
        print("3. Update Patient Data")
        print("4. Filter Patient")
        print("5. Sort Patient Data")
        print("6. Delete Patient" if user == "admin" else "")
        print("0. Logout")
        
        choice = input("\nChoose a menu option: ")
        
        if choice == "1":
            read_patients()
        elif choice == "2" and user == "admin":
            add_patient()
        elif choice == "3":
            update_patient(user)
        elif choice == "4":
            filter_patient()
        elif choice == "5":
            sort_patients()  
        elif choice == "6" and user == "admin":
            delete_patient()
        elif choice == "0":
            print("\n RSUD Sanjiwani, Optimal Health, Excellent Care ")
            break
        else:
            print("\nInvalid input. Please try again.\n")

# Run program

main()