import pandas as pd
import sys

def main():
    try:
        url = "hf://datasets/lavita/ChatDoctor-HealthCareMagic-100k/data/train-00000-of-00001-5e7cb295b9cff0bf.parquet"
        print(f"Reading parquet file from {url}...")
        df = pd.read_parquet(url)

        output_file = "chatdoctor.jsonl.gz"
        print(f"Writing to {output_file}...")
        df.to_json(output_file, orient='records', lines=True, compression='gzip')

        print("Successfully imported data.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
