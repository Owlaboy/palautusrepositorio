from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        #print(data)
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        dependencies = data["tool"]["poetry"]["dependencies"]
        devdependencies = data["tool"]["poetry"]["dev-dependencies"]

        return Project(name, description, dependencies, devdependencies)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy-avoin/python-kevat-2021/main/koodi/viikko3/web-login-robot/pyproject.toml"
    reader = ProjectReader(url)
    reader.get_project()
