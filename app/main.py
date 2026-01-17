from dotenv import load_dotenv
load_dotenv()

from app.etl.extract import Extract
from app.etl.transform import Transform
from app.etl.load import Load

INPUT_PATH = "data/users.csv"
OUTPUT_PATH = "data/users_with_messages.csv"

def main():
    df = Extract.from_csv(INPUT_PATH)
    df = Transform.add_marketing_messages(df)
    Load.to_csv(df, OUTPUT_PATH)
    print("✅ ETL finalizado com sucesso!")

if __name__ == "__main__":
    main()
