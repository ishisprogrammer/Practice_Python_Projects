import multiprocessing
import analysis as an
from reportlab.pdfgen import canvas
from reportlab.lib.colors import grey, black, blue, red, purple, white, green
import os

def generate_report(report_num):    
    print(f"Generating Report {report_num}")
    ## Generating Report Card Frame
    c = canvas.Canvas(f"Students_Report_Card_Generator/report/{an.real_data[report_num, 1]}.pdf", pagesize = (580, 580))
    
    c.setFillColor(red)
    c.rect(28, 500, 524, 56, fill = 1, stroke = 0)     # heading box
    c.rect(28, 390, 70, 84, fill = 0, stroke = 1)      # photo box
    c.setFillColor(grey)
    c.rect(126, 439, 240, 24, fill = 1, stroke = 0)    # name box
    c.rect(126, 410, 130, 24, fill = 1, stroke = 0)    # dob box
    c.rect(276, 410, 120, 24, fill = 1, stroke = 0)    # roll no. box
    
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 50)
    c.drawString(114, 510, 'REPORT CARD')
    c.setFillColor(black)
    c.setFont('Times-Roman', 15)
    c.drawString(132, 446, 'NAME : ')
    c.drawString(132, 416, 'DOB : ')
    c.drawString(280, 416, 'ROLL_NO. : ')
    
    c.setStrokeColor(blue) 
    c.setFillColor(purple)
    c.rect(43, 337, 40, 35, fill = 1, stroke = 1)      # S.No. box
    c.rect(84, 337, 108, 35, fill = 1, stroke = 1)     # Subject box
    c.rect(193, 337, 140, 35, fill = 1, stroke = 1)    # Marks box
    c.rect(334, 337, 128, 35, fill = 1, stroke = 1)    # Percentile box
    c.rect(463, 337, 70, 35, fill = 1, stroke = 1)     # Grade box
    
    # creating first grid
    x = [43, 84, 193, 334, 463]
    width = [40, 108, 140, 128, 70]
    height = 25
    y = 337
    for j in range(5):
        y -= 26
        for i in range(5):
            c.rect(x[i], y, width = width[i], height = height, fill = 0, stroke = 1)
    
    c.setFillColor(white)
    c.drawString(46, 349, 'S.No:')    
    c.drawString(113, 349, 'Subject')
    c.drawString(215, 349, 'Marks_Scored')
    c.drawString(363, 349, 'Percentile')
    c.drawString(480, 349, 'Grade')
    
    # fillings serial numbers
    c.setFillColor(black)
    y = 337
    for i in range(5):
        y -= 26
        c.drawString(58, y+7, f'{i+1}')
    
    # filling subject names
    y = 337
    subjects = ['Math', 'Hindi', 'English', 'SST', 'Science']
    for i in range(5):
        y-=26
        c.drawString(112, y+7, f'{subjects[i]}')
    
    c.setFillColor(green)
    c.setStrokeColor(black)
    c.rect(43, 138, 60, 41, fill = 1, stroke = 1)   # Total Marks box
    c.rect(103, 138, 39, 41, fill = 1, stroke = 1)  # Rank box
    c.rect(142, 138, 74, 41, fill = 1, stroke = 1)  # Total Percentile box
    c.rect(216, 138, 74, 41, fill = 1, stroke = 1)  # Overall Grade box
    c.rect(290, 138, 74, 41, fill = 1, stroke = 1)  # Total Percentage box
    c.rect(364, 138, 65, 41, fill = 1, stroke = 1)  # Result box
    
    c.setFillColor(white)
    c.drawString(56, 159, 'Total')
    c.drawString(54, 147, 'Marks')
    c.drawString(106, 153, 'Rank')
    c.drawString(161, 159, 'Total')
    c.drawString(149, 147, 'Percentile')
    c.drawString(230, 159, 'Overall')
    c.drawString(235, 147, 'Grade')
    c.drawString(309, 159, 'Total')
    c.drawString(294, 147, 'Percentage')
    c.drawString(378, 153, 'Result')
    
    # creating last grid
    y = 117
    x = [43, 103, 142, 216, 290, 364]
    width = [60, 39, 74, 74, 74, 65]
    height = 22
    c.setStrokeColor(blue)
    for i in range(6):
        c.rect(x[i], y, width[i], height)
    
    c.setFillColor(black)
    c.drawString(15, 38, 'Signature of Candidate')
    c.drawString(430, 38, "Principal's Signature")
    
    ## Filling Details
    c.setFillColor(white)
    c.drawString(188, 446, an.real_data[report_num, 0]) # name filled
    c.drawString(175, 416, an.real_data[report_num, 2]) # dob filled
    c.drawString(364, 416, an.real_data[report_num, 1]) # roll no. filled
    
    # Filling the first grid
    c.setFillColor(black)
    y = 337
    for j in range(5):
        y -= 26        
        c.drawString(253, y+7, f"{an.real_data[report_num, j+3]}")                 # marks cell filled
        c.drawString(376, y+7, f"{an.subject_wise_percentile[report_num, j]:.2f}") # percentile cell filled
        c.drawString(492, y+7, f"{an.subject_wise_grades[report_num, j]}")         # grade cell filled

    # Filling the last grid
    y = 122
    x = [59, 114, 161, 245, 307, 383]
    c.drawString(59, 122, f"{an.total_marks[report_num]}")                    # total_marks filled
    c.drawString(114, 122, f"{an.rank[report_num]}")                          # rank filled
    c.drawString(144, 122, f"{an.total_percentile[report_num]:.2f} %ile")     # total_percentile filled
    c.drawString(245, 122, f"{an.overall_grades[report_num]}")                # overall grades filled
    c.drawString(307, 122, f"{an.total_percentage[report_num]:.2f}")          # total_percentage filled
    c.drawString(383, 122, f"{an.pass_fail_record[report_num]}")              # result filled

    # pasting the image
    path = os.path.abspath(f"Students_Report_Card_Generator/images/img{report_num}.png")
    c.drawImage(rf"{path}",  28, 390, width = 70, height = 84) 
    c.save()
    print(f"Finished Generating Report {report_num}")


if __name__ == '__main__':
    processes = []
    for i in range(len(an.real_data)):
        process = multiprocessing.Process(target = generate_report, args = (i, ))
        processes.append(process)
        process.start()       
    for x in processes:
        x.join()

