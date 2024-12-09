import argparse
import csv
import re
import os


def clean_csv(input_file, output_file, column_to_clean, remove_duplicates=False):
    try:
        # Read CSV content
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames

            # Check if the CSV has headers
            if not fieldnames:
                raise ValueError(f"The input file '{input_file}' has no headers.")

            rows = list(reader)

        # Check if the column to clean exists
        if column_to_clean not in fieldnames:
            raise KeyError(f"Column '{column_to_clean}' not found in the CSV headers.")

        # Handle empty input files
        if not rows:
            with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()  # Write only the header if input is empty
            print(f"The input file '{input_file}' is empty. Only headers were written to '{output_file}'.")
            return

        # Clean and process rows
        cleaned_rows = []
        seen_rows = set()

        for row in rows:
            # Clean a specific column with a regex
            if column_to_clean in row:
                row[column_to_clean] = re.sub(r'\s+', ' ', row[column_to_clean].strip())

            # Remove duplicates if enabled
            if remove_duplicates:
                row_tuple = tuple(row.items())
                if row_tuple in seen_rows:
                    continue
                seen_rows.add(row_tuple)

            cleaned_rows.append(row)

        # Write cleaned data to output file
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(cleaned_rows)

        print(f"CSV cleaned and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Clean up messy CSV data by removing duplicates and correcting formatting issues."
    )

    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to save the cleaned CSV file")
    parser.add_argument("-c", "--column", required=True,
                        help="The name of the column to clean using a regular expression")
    parser.add_argument("-d", "--deduplicate", action="store_true", help="Remove duplicate rows from the CSV")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        return

    clean_csv(args.input_file, args.output_file, args.column, args.deduplicate)


if __name__ == "__main__":
    main()
