
import pandas as pd


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='clean some data')
    parser.add_argument("contact_info_file", help="Path to the respondent_contact.csv file")
    parser.add_argument("other_info_file", help="Path to the respondent_other.csv file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    contact_info = pd.read_csv(args.contact_info_file)
    other_info = pd.read_csv(args.other_info_file)

# merge the two input data files based on the ID of each respondent.
merged_data = pd.merge(contact_info, other_info, left_on='respondent_id', right_on='id')

# drop any rows with missing values
merged_data = merged_data.dropna()

# drop rows if the job value contains ‘insurance’ or ‘Insurance’
merged_data = merged_data[~merged_data['job'].str.contains('insurance|Insurance')]

# Select the desired columns
cleaned = merged_data[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]

cleaned.to_csv(args.output_file, index=False)
