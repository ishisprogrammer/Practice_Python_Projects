# Students Report Card Generator

## Description

The Students Report Card Generator is a Python-based automation project that reads student data from a text file, calculates total marks, percentage, grades, class rank, and percentile, and generates formatted PDF report cards for each student with their photograph.

This project uses **NumPy** for data analysis and **ReportLab** for PDF generation. It also uses **multiprocessing** to generate multiple report cards in parallel, making the system faster and efficient.

---

## Features

* Automatic total marks calculation
* Percentage calculation
* Subject-wise grade calculation
* Overall grade calculation
* Class rank calculation
* Percentile calculation
* Pass/Fail status generation
* PDF report card generation
* Student image included in report card
* Parallel report generation using multiprocessing

---

## Technologies Used

* Python
* NumPy
* ReportLab
* Multiprocessing
* File Handling

---

## Folder Structure

```
Students-Report-Card-Generator/
│
├── analysis.py
├── report_generator.py
├── README.md
├── requirements.txt
│
├── data/
│   └── file.txt
│
├── images/
│   ├── img0.png
│   ├── img1.png
│   ├── img2.png
│   └── ...
│
├── reports/
```

---

## Data File Format (data/file.txt)

The data file must be a **space-separated text file** with the following format:

```
Name Roll_No DOB Math Hindi English SST Science
Aman 101 12-05-2006 78 67 88 91 73
Riya 102 03-09-2006 85 79 92 88 90
Karan 103 21-01-2006 65 55 70 60 72
Simran 104 11-11-2006 90 92 89 94 95
```

### Rules:

* First row must be the header.
* Columns must be space-separated.
* First 3 columns must be:

  * Name
  * Roll_No
  * DOB
* Remaining 5 columns must be subject marks (out of 100).

---

## Image File Naming (Very Important)

Student images must be stored in the **images** folder using the following naming convention:

```
img0.png
img1.png
img2.png
img3.png
...
```

### Mapping Rule:

* img0.png → First student in the data file
* img1.png → Second student in the data file
* img2.png → Third student in the data file
* and so on...

**Note:** The image number must match the student’s position in the data file (excluding header).
If the order of students in the data file changes, the image names must also be updated accordingly.

Image format can be `.png` only.

---

## How to Run the Project

### Step 1 — Install Required Libraries

```
pip install -r requirements.txt
```

### Step 2 — Add Student Data File

Place the student data file in:

```
data/file.txt
```

### Step 3 — Add Student Images

Place student images in:

```
images/
```

### Step 4 — Run the Program

```
python generate_report_card.py
```

### Step 5 — Get Reports

Generated report cards will be saved in:

```
reports/
```

---

## Output

The program generates a PDF report card for each student containing:

* Student Name
* Roll Number
* Date of Birth
* Subject Marks
* Subject Percentile
* Subject Grade
* Total Marks
* Percentage
* Rank
* Overall Grade
* Result (Pass/Fail)
* Student Photograph

---

## Example Workflow

```
data/file.txt  →  analysis.py  →  report_generator.py  →  reports/student_report.pdf
```

---

## Future Improvements

* Dynamic subject handling
* GUI interface
* Excel report generation
* Performance charts in report card
* Email report cards to students

---

## Author

Ishdeep
