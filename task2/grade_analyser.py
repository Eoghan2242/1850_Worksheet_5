'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be acheived by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
import csv

def calculate_classification(average_grade):

    if average_grade >= 70:
        return "1"
    elif average_grade >= 60:
        return "2:1"
    elif average_grade >= 50:
        return "2:2"
    elif average_grade >= 40:
        return "3"
    else:
        return "F"

def process_student_grades(filename):
    
    output_filename = filename + "_out.csv"
    
    try:
        
        with open(filename, 'r', newline='') as infile, \
             open(output_filename, 'w', newline='') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
           
            writer.writerow(['student_id', 'average_grade', 'classification'])
            
           
            for row in reader:
                if not row: 
                    continue
                
               
                if row[0].lower().startswith('student_id'):
                    continue
                student_id = row[0]
                
                
                grades = []
                for grade_str in row[1:]:
                   
                    if grade_str and grade_str.strip():
                        try:
                           
                            clean_grade = grade_str.strip().rstrip('.')
                            grades.append(float(clean_grade))
                        except ValueError:
                            
                            continue
                
                
                if grades: 
                    average_grade = sum(grades) / len(grades)
                    
                    
                    classification = calculate_classification(average_grade)
                    
                    
                    writer.writerow([student_id, f"{average_grade:.2f}", classification])
        
        print(f"\nProcessing complete! Results written to: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    filename = input("Enter the filename of the student data file: ").strip()
    
    if filename:
        process_student_grades(filename)
    else:
        print("No filename provided. Exiting.")

if __name__ == "__main__":
    main()



    

