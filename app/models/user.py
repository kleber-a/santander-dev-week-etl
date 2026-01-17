class User:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self):
        return self.data["id"]

    @property
    def name(self):
        return self.data["name"]

    def add_news(self, description: str):
        self.data["news"].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": description
        })
