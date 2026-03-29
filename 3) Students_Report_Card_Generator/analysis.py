import numpy as np

real_data = np.loadtxt('Students_Report_Card_Generator/data/file.txt', skiprows = 1, dtype = str, encoding = 'utf-8') # extracted data from txt file and whitespaces automatically rejected and started from row 1
student_marks = real_data[ : , 3 :].astype(int)

total_marks = student_marks.sum(axis = 1)

total_percentage = (total_marks/500)*100

subject_wise_grades = np.where((student_marks>0) & (student_marks<=40), 'E', 
                      np.where((student_marks>40) & (student_marks<=60), 'D', 
                      np.where((student_marks>60) & (student_marks<=80), 'C', 
                      np.where((student_marks>80) & (student_marks<=90), 'B',
                      np.where(student_marks>90, 'A', student_marks))))) # where replaces the false value with corresponding element of student_marks

overall_grades = np.where((total_marks>0) & (total_marks<=100), 'E', 
                 np.where((total_marks>100) & (total_marks<=200), 'D', 
                 np.where((total_marks>200) & (total_marks<=300), 'C', 
                 np.where((total_marks>300) & (total_marks<=400), 'B', 
                 np.where(total_marks>400,  'A', total_marks)))))

rank = np.searchsorted(np.sort(-total_marks), -total_marks) + 1      # the method replaces the elements of total_marks with the index position at which they will occur in sorted array if inserted

total_percentile = (((len(rank) - rank) + 1)/len(rank))*100

subject_wise_rank = np.hstack((np.searchsorted(np.sort(-student_marks[0:, 0]), -student_marks[0:, 0]).reshape(len(student_marks), 1),
                               np.searchsorted(np.sort(-student_marks[0:, 1]), -student_marks[0:, 1]).reshape(len(student_marks), 1),
                               np.searchsorted(np.sort(-student_marks[0:, 2]), -student_marks[0:, 2]).reshape(len(student_marks), 1),
                               np.searchsorted(np.sort(-student_marks[0:, 3]), -student_marks[0:, 3]).reshape(len(student_marks), 1),
                               np.searchsorted(np.sort(-student_marks[0:, 4]), -student_marks[0:, 4]).reshape(len(student_marks), 1))) + 1
subject_wise_percentile = (((len(subject_wise_rank) - subject_wise_rank) + 1)/len(subject_wise_rank))*100 

pass_fail_record = np.where(((student_marks > 33).all(axis = 1)) & (total_marks > 200), 'Pass', 'Fail')







