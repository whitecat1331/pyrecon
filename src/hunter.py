from pyhunter import PyHunter 
from api import Api


# redo paramters to match api
class Hunter(Api):
    PATH = "hunter"
    ENV_VAR = "hunter_api_key"

    def __init__(self):
        Api.__init__(self, PATH, ENV_VAR)
        hunter = PyHunter(self.key)

    def domain_search(self, 
        domain, file_name=None, company=None, 
        limit=None, offset=None, emails_type=None):

        response = self.huter.domain_search(domain, company=company, 
                limit=limit, offset=offset, 
                emails_type=emails_type)
        self.save_to_file(response, file_name)
        return response

    def email_finder(self, domain, file_name=None, first_name=None, last_name=None):
        response = self.hunter.domain_finder(domain,
                first_name=first_name, last_name=last_name)
        self.save_to_file(response, file_name)
        return response

    def emails_finder(self, company=None, full_name=None):
        response = self.hunter.domain_finder(company=company, full_name=full_name, raw=True)
        save_to_file(response, file_name)
        return response

    def email_verifier(self, domain, file_name=None):
        response = self.hunter.email_verifier(domain)
        self.save_to_file(response, file_name)
        return response

    def email_count(self, file_name=None, domain=None, company=None):
        response = self.hunter.email_count(domain=domain, company=company)
        self.save_to_file(response, file_name)
        return response

    def get_leads(self, 
            file_name=None, offset=None, limit=None, 
            lead_list=1, first_name=None, last_name=None,
            email=None, company=None, phone_number=None
            twitter=None):
        response = self.hunter.get_leads(offset=offset, limit=limit, lead_list=lead_list, 
               first_name=first_name, last_name=last_name, email=email, 
               company=company, phone_number=phone_number, twitter=twitter)
        self.save_to_file(response, file_name)
        return response

    # redo
    def get_lead(self, id, file_name=None):
        response = self.hunter.get_lead(id)
        self.save_to_file(resonse, file_name)
        return response

    def create_lead(self, first_name, last_name, **kwargs):
        self.hunter.create_lead(first_name, last_name, **kwargs)

    def update_lead(self, id, **kwargs):
        self.hunter.create_lead(first_name, last_name, **kwargs)

    def delete_lead(self, id):
        self.hunter.delete_lead(id)

    def get_leads_lists(self, file_name=None, **kwargs):
        response = self.hunter.get_leads_lists(**kwargs)
        self.save_to_file(response, file_name)
        return response

    def get_leads_list(self, id, file_name=None):
        response = self.hunter.get_leads_list(id)
        self.save_to_file(response, file_name)
        return response

    def create_leads_list(name, **kwargs):
        self.hunter.create_leads_list(name, **kwargs)

    def account_info(self, file_name=None):
        self.save_to_file()
        return self.hunter.account_info()
