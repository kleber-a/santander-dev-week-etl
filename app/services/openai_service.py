import os
from openai import OpenAI, RateLimitError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    @staticmethod
    def generate_marketing_message(user_name: str) -> str:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um especialista em marketing bancário."
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Crie uma mensagem curta para {user_name} "
                            f"sobre investimentos (máx 100 caracteres)."
                        )
                    }
                ]
            )

            return response.choices[0].message.content.strip()

        except RateLimitError:
            # Fallback realista (simulação)
            return (
                f"{user_name}, investir hoje é o caminho para "
                f"um futuro financeiro mais seguro."
            )
