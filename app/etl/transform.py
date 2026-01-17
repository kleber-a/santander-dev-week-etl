from app.services.openai_service import OpenAIService

class Transform:
    @staticmethod
    def add_marketing_messages(df):
        df["message"] = df["name"].apply(
            lambda name: OpenAIService.generate_marketing_message(name)
        )
        return df
