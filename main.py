#   HOSPITAL MANAGEMENT SYSTEM

patients = []
doctors = []
appointments = []
medicines = []
rooms = []
bills = []

#   PATIENT FUNCTIONS

def add_patient():
    print("\n Add Patient ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter gender: ")
    phone = input("Enter phone number: ")
    disease = input("Enter disease/problem: ")

    patient = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "disease": disease
    }
    patients.append(patient)
    print("\nPatient added successfully!")

def view_patients():
    print("\n Patient List ")

    if len(patients) == 0:
        print("No patients found.")
        return

    i=1
    for patient in patients:
        print("\nPatient", i)
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Phone:", patient["phone"])
        print("Disease:", patient["disease"])
        i=i+1


def search_patient():
    print("\n Search Patient ")
    name = input("Enter patient name: ")

    for patient in patients:
        if patient["name"] == name:

            print("\nPatient Found!")
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Phone:", patient["phone"])
            print("Disease:", patient["disease"])
            return

    print("\nPatient not found.")

#   DOCTOR FUNCTIONS

def add_doctor():
    print("\n Add Doctor")
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    phone = input("Enter phone number: ")

    doctor = {
        "name": name,
        "specialization": specialization,
        "phone": phone
    }

    doctors.append(doctor)
    print("\nDoctor added successfully!")


def view_doctors():
    print("\nDoctor List ")

    if len(doctors) == 0:
        print("No doctors found.")
        return

    i=1
    for doctor in doctors:
        print("\nDoctor", i)
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Phone:", doctor["phone"])
        i=i+1

#   APPOINTMENT FUNCTIONS

def book_appointment():
    print("\n Book Appointment ")

    if len(patients) == 0:
        print("Please add a patient first.")
        return

    if len(doctors) == 0:
        print("Please add a doctor first.")
        return

    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date: ")
    time = input("Enter appointment time: ")

    appointment = {
        "patient": patient_name,
        "doctor": doctor_name,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    print("\nAppointment booked successfully!")


def view_appointments():
    print("\n Appointment List ")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    i=1
    for appointment in appointments:

        print("\nAppointment", i)
        print("Patient:", appointment["patient"])
        print("Doctor:", appointment["doctor"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        i=i+1

#   MEDICINE FUNCTIONS

def add_medicine():
    print("\n Add Medicine ")
    name = input("Enter medicine name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")

    medicine = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    medicines.append(medicine)
    print("\nMedicine added successfully!")

def view_medicines():
    print("\n Medicine List ")

    if len(medicines) == 0:
        print("No medicines found.")
        return

    i=1
    for medicine in medicines:

        print("\nMedicine", i)
        print("Name:", medicine["name"])
        print("Quantity:", medicine["quantity"])
        print("Price:", medicine["price"])
        i=i+1

#    ROOM FUNCTIONS

def add_room():
    print("\n Add Room ")
    room_number = input("Enter room number: ")
    room_type = input("Enter room type: ")
    status = input("Enter room status (Available/Occupied): ")

    room = {
        "number": room_number,
        "type": room_type,
        "status": status
    }

    rooms.append(room)
    print("\nRoom added successfully!")

def view_rooms():
    print("\n Room List ")

    if len(rooms) == 0:
        print("No rooms found.")
        return

    i=1
    for room in rooms:

        print("\nRoom", i)
        print("Room Number:", room["number"])
        print("Room Type:", room["type"])
        print("Status:", room["status"])
        i=i+1

#   BILL FUNCTIONS

def create_bill():
    print("\n Create Bill ")
    patient_name = input("Enter patient name: ")
    doctor_charge = float(input("Enter doctor charge: "))
    medicine_charge = float(input("Enter medicine charge: "))
    room_charge = float(input("Enter room charge: "))
    total = doctor_charge + medicine_charge + room_charge

    bill = {
        "patient": patient_name,
        "doctor_charge": doctor_charge,
        "medicine_charge": medicine_charge,
        "room_charge": room_charge,
        "total": total
    }

    bills.append(bill)
    print("\nBill created successfully!")
    print("Total Amount:", total)


def view_bills():
    print("\n Bill List ")

    if len(bills) == 0:
        print("No bills found.")
        return

    i=1

    for bill in bills:
        print("\nBill", i)
        print("Patient:", bill["patient"])
        print("Doctor Charge:", bill["doctor_charge"])
        print("Medicine Charge:", bill["medicine_charge"])
        print("Room Charge:", bill["room_charge"])
        print("Total Amount:", bill["total"])
        i=i+1

#   HOSPITAL REPORT

def hospital_report():
    print("\n Hospital Report ")
    print("Total Patients:", len(patients))
    print("Total Doctors:", len(doctors))
    print("Total Appointments:", len(appointments))
    print("Total Medicines:", len(medicines))
    print("Total Rooms:", len(rooms))
    print("Total Bills:", len(bills))

#    MAIN MENU

while True:
    print("\n")
    print(" HOSPITAL MANAGEMENT SYSTEM")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Add Doctor")
    print("5. View Doctors")
    print("6. Book Appointment")
    print("7. View Appointments")
    print("8. Add Medicine")
    print("9. View Medicines")
    print("10. Add Room")
    print("11. View Rooms")
    print("12. Create Bill")
    print("13. View Bills")
    print("14. Hospital Report")
    print("15. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        add_doctor()

    elif choice == "5":
        view_doctors()

    elif choice == "6":
        book_appointment()

    elif choice == "7":
        view_appointments()

    elif choice == "8":
        add_medicine()

    elif choice == "9":
        view_medicines()

    elif choice == "10":
        add_room()

    elif choice == "11":
        view_rooms()

    elif choice == "12":
        create_bill()

    elif choice == "13":
        view_bills()

    elif choice == "14":
        hospital_report()

    elif choice == "15":
        print("\nThank you for using the Hospital Management System!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice!")
        print("Please enter a number from 1 to 15.")