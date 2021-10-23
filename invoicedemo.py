#!/usr/local/bin/python
import datetime
import os

from reportlab.lib import colors, styles
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class Bill():
    def __init__(self, service, part, cust, vehicle, emp):
        print('bill class')
        doc = SimpleDocTemplate("test_report_lab.pdf", pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                                bottomMargin=18)
        # doc.pagesize = landscape(A4)
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
        elements = []

        total = 0
        cust_veh = [
            [Paragraph("Customer ID : {0}".format(cust[0]), styles["Normal"]),
             Paragraph("Service ID : {0}".format(service[0]), styles["Normal"])],
            [Paragraph("Name : {0}".format(cust[1]), styles["Normal"]),
             Paragraph("Job Desc. : {0}".format(service[1]), styles["Normal"])],
            [Paragraph("Address : {0}".format(cust[2]), styles["Normal"]),
             Paragraph("Job Date : {0}".format(service[2]), styles["Normal"])],
            [Paragraph("Mobile : {0}".format(cust[3]), styles["Normal"]),
             Paragraph("Distance : {0}".format(service[3]), styles["Normal"])],
            [Paragraph("Email : {0}".format(cust[4]), styles["Normal"])],
            [Paragraph("Vehicle ID : {0}".format(vehicle[0]), styles["Normal"]),
             Paragraph("Service Advisor : {0}".format(emp[0]), styles["Normal"])],
            [Paragraph("Reg. no : {0}".format(vehicle[1]), styles["Normal"]),
             Paragraph("SA Contact no : {0}".format(emp[1]), styles["Normal"])],
            [Paragraph("Company : {0}".format(vehicle[2]), styles["Normal"])],
            [Paragraph("Model : {0}".format(vehicle[3]), styles["Normal"])],
            [Paragraph("Type : {0}".format(vehicle[4]), styles["Normal"])]
        ]
        csv = TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')])
        table_cust = Table(cust_veh)
        table_cust.setStyle(csv)
        data = [["Sr \nno.", "Part ID", "Part", "Rate", 'Quantity', "Amount"]]
        i = 1
        for x in part:
            s = [str(i)]
            for a in x:
                s.append(str(a))
            total += x[4]
            data.append(s)
            i += 1
        data.append(['', '', '', '', 'Total Amount', str(total)])

        # TODO: Get this line right instead of just copying it from the docs
        style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                            ('VALIGN', (0, 0), (0, -1), 'TOP'),
                            ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                            ('BOX', (0, 0), (-1, -2), 0.25, colors.black),
                            ('BOX', (0, 0), (5, 0), 0.25, colors.black),
                            ('BOX', (0, -1), (-1, -1), 0.25, colors.black)
                            ])

        # Configure style and word wrap
        s = getSampleStyleSheet()
        s = s["BodyText"]
        s.wordWrap = 'CJK'
        data2 = [[Paragraph(cell, s) for cell in row] for row in data]
        t = Table(data2, colWidths=[0.5*inch, None])
        t.setStyle(style)
        sign_style = TableStyle([('ALIGN', (0, 0), (0, 0), 'LEFT'),
                                 ('ALIGN', (1, 0), (1, 0), 'RIGHT')
                                 ])
        sign = [[Paragraph("(Customer Signature)", styles["Normal"]),
                 Paragraph("(Authorized Signature)", styles["Right"])]]
        sign_table = Table(sign)
        sign_table.setStyle(sign_style)

        # Send the data and build the file
        now = datetime.datetime.now()
        now = "<font size=8>Print Date: {0} Timing: {1}</font size>".format(now.strftime("%Y-%b-%d"),
                                                                            now.strftime("%H:%M:%S"))
        elements.append(Paragraph(now, styles["Right"]))
        elements.append(table_cust)
        elements.append(Spacer(1, 10))
        elements.append(t)
        elements.append(Spacer(1, 70))
        elements.append(sign_table)
        doc.build(elements)
        os.startfile("test_report_lab.pdf")


# b = Bill((2, 'Maintenance', datetime.date(2018, 10, 1), 6769, 'Dent on left', 2782.0, 5, 1),
#          [(1, 'Bumper Front', 1355.0, 1, 1355.0), (5, 'Engine oil', 450.0, 1, 450.0),
#           (3, 'High-pitched Horn', 665.0, 1, 665.0), (4, 'Windshield Wiper', 156.0, 2, 312.0)],
#          (2, 'Rushi', 'Chemburasfn nansofnfas asin oaisnf a nsfoains  n oi asnfo iansfo in', 9563272653, 'rushipowar@gmail.com'),
#           (5, 'MH31W2657', 'Renalt', 'Duster', 'SUV'),
#          ('Ashish', 8615742365))
