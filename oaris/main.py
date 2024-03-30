import requests
import base64
from IPython.display import HTML

import click

class Works:
    def __init__(self, oaid):
        """Initialize the Works object.
        oaid : string that is a DOI or OpenAlex Works id.
        """
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def ris(self, cli=False):
        """Return an RIS entry for the Works object."""
        fields = []
        if self.data["type_crossref"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        jname = self.data["primary_location"]["source"]["display_name"]

        fields += [f"JO  - {jname}"]
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        if cli:
            return ris
        else:
            ris64 = base64.b64encode(ris.encode("utf-8")).decode("utf8")
            uri = f'<pre>{ris}</pre><br><a href="data:text/plain;base64,{ris64}" download="ris">Download RIS</a>'
            return HTML(uri)
    
@click.command(help='Get an RIS from a DOI')
@click.argument('oaid')
def main(oaid):
    w = Works(oaid)
    print(w.ris(cli=True))
