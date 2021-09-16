import json
from bs4 import BeautifulSoup
import requests
from requests import Session


class DatabaseOperation:
    metabase_url: str
    session: Session

    def __init__(self, metabase_url, username, password) -> None:
        self.metabase_url = metabase_url

        # set up session for auth
        self.session = requests.Session()

    def list_databases(self):
        r = self.session.get("{}/METABASE_API_URL".format(self.metabase_url))

        ## example:
        if r.status_code == 401:
            raise Exception("Invalid credentials")
        elif r.status_code == 404:
            raise Exception("Invalid metabase URL, 404 returned")
        elif r.status_code != 200:
            raise Exception("Unable to perform operation: {}".format(r.text))

        return list(filter(lambda db: db.get('backend') == 'trino', all_databases))

    def create_database(self, metriql_url, database_name):
        pass

    def sync(self, database_id, metadata):
        pass

        ## print something like:
        print("Successfully synchronized existing {} datasets, created {} datasets".format(
            len(metriql_datasets) - new_dataset_count, new_dataset_count))
