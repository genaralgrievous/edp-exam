class Event:
    def __init__(self, payload):
        self.payload = payload

class JobApplicationRequestEvent(Event):
    name = 'jop_application_request'
    
    def __init__(self, payload):
        super().__init__(payload)

class ApplicationConfirmationEvent(Event):
    name = 'application_confirmation'
    
    def __init__(self, payload):
        super().__init__(payload)
        

communication_queue = [
]

class Worker:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        

    def ask_for_company_application(self, date):
        event = JobApplicationRequestEvent(phone_number = self.phone_number, date = date)
        
        communication_queue.append(event)
        print('Event', event.name, 'emitted!')

class Company:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def handle_application_request(self):
        current_request_event = communication_queue.pop(0)
        print("Received request from worker with Passport:", current_request_event.passport_number)
        
  
        event = ApplicationConfirmationEvent(request_id = current_request_event.passport_number, is_confirmed = True)
        communication_queue.append(event)
        print('Event', event.name, 'emitted!')


         
peter1 = Student("Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')
peter2 = Student("Piotr2", "Brudny", '2.02.1994', 'Ankara', '5435345345', 'ED41423')
peter3 = Student("Piotr3", "Brudny", '4.02.1984', 'Ankara', '54353fds45345', 'ED42723')
peter4 = Student("Piotr4", "Brudny", '1.12.2004', 'Ankara', '5435345345', 'ED423477')

peter1.ask_for_embassy_appointment('10.12.2024')    
polish_embassy = Embassy('Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr')

polish_embassy.handle_appointment_request()