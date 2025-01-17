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


class RecruitmentApprovalEvent(Event):
    name = 'recruitment_approval'

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
        if communication_queue:
            current_request_event = communication_queue.pop(0)
            print("Received request from worker with phone number:", current_request_event.payload["phone_number"])
            
            event = ApplicationConfirmationEvent(payload={"request_id": current_request_event.payload["phone_number"], "is_confirmed": True})
            communication_queue.append(event)
            print('Event', event.name, 'emitted!')


class Recruiter:
    def __init__(self, name):
        self.name = name

    def approve_recruitment(self):
        if communication_queue:
            current_event = communication_queue.pop(0)
            print(f"{self.name} handling confirmation event for request ID:", current_event.payload["request_id"])

            event = RecruitmentApprovalEvent(payload={"recruiter": self.name, "approval_status": "Approved"})
            communication_queue.append(event)
            print('Event', event.name, 'emitted!')

class GovernmentAgency:
    def __init__(self, name):
        self.name = name

    def handle_recruitment_approval(self):
        if communication_queue:
            current_event = communication_queue.pop(0)
            print(f"{self.name} received recruitment approval from recruiter:", current_event.payload["recruiter"])
            print("Recruitment process finalized.")

         
# Example Usage
worker = Worker("John", "Doe", "1990-01-01", "123 Elm St", "555-1234")
company = Company("TechCorp", "456 Maple Ave", "555-5678", "info@techcorp.com")
recruiter = Recruiter("Alice")
gov_agency = GovernmentAgency("Employment Bureau")

worker.ask_for_company_application("2025-01-20")
company.handle_application_request()
recruiter.approve_recruitment()
gov_agency.handle_recruitment_approval()

