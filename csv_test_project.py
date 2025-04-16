# Lab 3
# Author:Maciej Dziewulski
# Date: 04.15.2025
import csv


def split_countries_by_region(input_csv='country_full.csv'):
    """
    Reads a CSV file that contains countries information
    and splits them into multiple CSV files by region.
    """

    try:
        with open(input_csv, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Store the original column headers
            fieldnames = reader.fieldnames

            data_by_region = {}

            # Group rows by region
            for row in reader:
                region = row.get('region', 'Unknown')
                if region not in data_by_region:
                    data_by_region[region] = []
                # Append the entire row as read from the CSV
                data_by_region[region].append(row)

    except FileNotFoundError:
        print(f"Error: The file '{input_csv}' was not found.")
        return
    except PermissionError:
        print(f"Error: Insufficient permissions to read '{input_csv}'.")
        return
    except IOError as e:
        print(f"IO error occurred: {e}")
        return

    # Create separate CSV files by region
    for region_name, rows in data_by_region.items():
        # Make the region name safe for file systems
        safe_region_name = "".join(char if char.isalnum() else "_" for char in region_name)
        output_filename = f"{safe_region_name}.csv"

        try:
            with open(output_filename, 'w', newline='', encoding='utf-8') as region_file:
                writer = csv.DictWriter(region_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print(f"File '{output_filename}' created successfully.")
        except PermissionError:
            print(f"Error: Insufficient permissions to write '{output_filename}'.")
        except IOError as e:
            print(f"IO error occurred while writing '{output_filename}': {e}")


if __name__ == "__main__":
    split_countries_by_region()
