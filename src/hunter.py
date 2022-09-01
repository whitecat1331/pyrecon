from pyhunter import PyHunter
from api import Api


# redo paramters to match api
class Hunter(Api):
    NAME = "hunter"
    ENV_VAR = "hunter_api_key"

    def __init__(self):
        Api.__init__(self, self.NAME, self.ENV_VAR)
        self.hunter = PyHunter(self.key)

    @Api.save
    def domain_search(
        self, domain, company=None, limit=None, offset=None, emails_type=None
    ):

        response = self.hunter.domain_search(
            domain,
            company=company,
            limit=limit,
            offset=offset,
            emails_type=emails_type
        )
        return response

    @Api.save
    def email_finder(self, domain, first_name=None, last_name=None):
        response = self.hunter.email_finder(
            domain, first_name=first_name, last_name=last_name
        )

        return response

    @Api.save
    def emails_finder(self, company=None, full_name=None):
        response = self.hunter.email_finder(
            company=company, full_name=full_name, raw=True
        )

        return response

    @Api.save
    def email_verifier(self, domain):
        response = self.hunter.email_verifier(domain)
        return response

    @Api.save
    def email_count(self, file_name=None, domain=None, company=None):
        response = self.hunter.email_count(domain=domain, company=company)
        return response

    @Api.save
    def get_leads(
        self,
        offset=None,
        limit=None,
        lead_list_id=1,
        first_name=None,
        last_name=None,
        email=None,
        company=None,
        phone_number=None,
        twitter=None,
    ):
        response = self.hunter.get_leads(
            offset=offset,
            limit=limit,
            lead_list_id=lead_list_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
            phone_number=phone_number,
            twitter=twitter,
        )
        return response

    @Api.save
    def get_lead(self, id):
        response = self.hunter.get_lead(id)
        return response

    def create_lead(
            self,
            first_name,
            last_name,
            email=None,
            position=None,
            company=None,
            confidence_score=None,
            website=None,
            country_code=None,
            postal_code=None,
            source=None,
            linkedin_url=None,
            phone_number=None,
            twitter=None,
            leads_list_id=None
            ):
        self.hunter.create_lead(
                first_name,
                last_name,
                email=email,
                position=position,
                company=company,
                confidence_score=confidence_score,
                website=website,
                country_code=country_code,
                postal_code=postal_code,
                source=source,
                linkedin_url=linkedin_url,
                phone_number=phone_number,
                twitter=twitter,
                leads_list_id=leads_list_id
                )

    def update_lead(
            self,
            id,
            first_name=None,
            last_name=None,
            email=None,
            position=None,
            company=None,
            confidence_score=None,
            website=None,
            country_code=None,
            postal_code=None,
            source=None,
            linkedin_url=None,
            phone_number=None,
            twitter=None,
            leads_list_id=None
            ):
        self.hunter.update_lead(
                id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                position=position,
                company=company,
                confidence_score=confidence_score,
                website=website,
                country_code=country_code,
                postal_code=postal_code,
                source=source,
                linkedin_url=linkedin_url,
                phone_number=phone_number,
                twitter=twitter,
                leads_list_id=leads_list_id
                )

    def delete_lead(self, id):
        self.hunter.delete_lead(id)

    @Api.save
    def get_leads_lists(self, id, offset=None, limit=None):
        response = self.hunter.get_leads_lists(id, offset=offset, limit=limit)
        return response

    def update_leads_list(self, id, name, team_id=None):
        self.hunter.update_leads_list(id, name, team_id=team_id)

    def delete_leads_list(self, name, id):
        self.hunter.create_leads_list(name, id)

    @Api.save
    def account_info(self):
        return self.hunter.account_info()
