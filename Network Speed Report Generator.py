from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import speedtest

def generate_report():
    # Get the current date and time
    now = datetime.now().strftime('%Y-%m-%d %H_%M_%S')

    # Get the network speed data
    st = speedtest.Speedtest()
    download_speed = round(st.download() / 1000000, 2)
    upload_speed = round(st.upload() / 1000000, 2)
    ping = round(st.results.ping, 2)
    server = st.results.server['sponsor']
    
    # Generate the PDF report
    c = canvas.Canvas(f"network_speed_report_{now}.pdf", pagesize=letter)
    width, height = letter
    
    # Add the report title
    c.setFont('Helvetica-Bold', 16)
    c.drawCentredString(width/2, height-0.75*inch, "Network Speed Report")
    
    # Add the report timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.setFont('Helvetica', 12)
    c.drawCentredString(width/2, height-1*inch, f"Report generated on: {timestamp}")
    
    # Add the network speed table
    data = [['Download Speed (Mbps)', 'Upload Speed (Mbps)', 'Ping (ms)', 'Server'],
            [download_speed, upload_speed, ping, server]]
    table = Table(data, colWidths=[2.5*inch, 2.5*inch, 1.5*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 14),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('TEXTCOLOR', (0,1), (-1,-1), colors.black),
        ('ALIGN', (0,1), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 12),
        ('BOTTOMPADDING', (0,1), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    table.wrapOn(c, width, height)
    # table.drawOn(c, *coord(1*inch, 6*inch, width-1*inch, height-2*inch))
    table.drawOn(c, .1*inch, 6*inch)    # position of text / where to draw
    
    # Save the PDF report
    c.save()

if __name__ == '__main__':
    generate_report()
