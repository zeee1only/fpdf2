from fpdf import FPDF
from datetime import date

def create_exhibit_cover_pages():
    # Create PDF object
    pdf = FPDF()
    
    # Set auto page break
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Define exhibit data
    exhibits = [
        {
            "id": "A-1",
            "title": "BURBANK CONFLICT - PROOF OF MARRIAGE",
            "description": "Dodge County News Article: 'Dodge County Has New Assistant County Attorney'\nConfirming the marital relationship between Investigator Jeff Burbank and Prosecutor Kathryn Burbank."
        },
        {
            "id": "A-2", 
            "title": "BURBANK CONFLICT - OFFICIAL ROLE",
            "description": "State's Witness List (Pages 69-70, 72-73 from Court File)\nNaming 'Investigations Jeffrey Burbank' as a state agent in this prosecution."
        },
        {
            "id": "A-3",
            "title": "BURBANK CONFLICT - PROSECUTORIAL ROLE", 
            "description": "Kathryn Burbank Professional Profile / News Article\nConfirming her role as a County Attorney, creating the conflict of interest."
        },
        {
            "id": "D-1",
            "title": "INEFFECTIVE ASSISTANCE OF COUNSEL",
            "description": "Defense Counsel's 'Omnibus Motion to Dismiss' (Pages 24-25 from Court File)\nDemonstrating the initial, unsuccessful challenge to the evidence."
        },
        {
            "id": "B-5",
            "title": "PRIOR COURT RULING ON EVIDENCE", 
            "description": "Court's 'Order Denying Defendant's Motion to Dismiss' (Pages 43-49 from Court File)\nThe Court's previous ruling on the search warrant challenge, now used to demonstrate ineffective assistance of counsel."
        },
        {
            "id": "H-1",
            "title": "COERCIVE OVERCHARGING",
            "description": "Booking Sheet / Charging Document\nProof the State initially charged Defendant with 3rd Degree Murder (Statute 609.195), a charge later dropped to coerce a plea."
        },
        {
            "id": "E-1",
            "title": "PROPERTY NOT RETURNED",
            "description": "Rice County Sheriff's Office Inmate Property List\nProof that the Defendant's personal property, including his cell phone (the subject of the search), was seized and not returned."
        }
    ]
    
    # Create cover page for each exhibit
    for exhibit in exhibits:
        pdf.add_page()
        
        # Set font for header
        pdf.set_font('Arial', 'B', 14)
        
        # Court information
        pdf.cell(0, 10, 'STATE OF MINNESOTA', 0, 1, 'C')
        pdf.cell(0, 10, 'DISTRICT COURT', 0, 1, 'C')
        pdf.cell(0, 10, 'COUNTY OF RICE', 0, 1, 'C')
        pdf.cell(0, 10, 'THIRD JUDICIAL DISTRICT', 0, 1, 'C')
        pdf.ln(5)
        
        # Case information
        pdf.cell(0, 10, 'State of Minnesota,', 0, 1, 'C')
        pdf.cell(0, 10, '    Plaintiff,', 0, 1, 'C')
        pdf.cell(0, 10, 'v.', 0, 1, 'C')
        pdf.cell(0, 10, 'Zakaria Abdullahi,', 0, 1, 'C')
        pdf.cell(0, 10, '    Defendant.', 0, 1, 'C')
        pdf.ln(5)
        
        pdf.cell(0, 10, f'Court File No.: 66-CR-21-1673', 0, 1, 'C')
        pdf.ln(10)
        
        # Exhibit number
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 15, f'EXHIBIT {exhibit["id"]}', 0, 1, 'C')
        pdf.ln(5)
        
        # Exhibit title
        pdf.set_font('Arial', 'B', 14)
        pdf.multi_cell(0, 10, exhibit["title"], 0, 'C')
        pdf.ln(5)
        
        # Exhibit description
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 8, exhibit["description"], 0, 'C')
        pdf.ln(15)
        
        # Submission line
        pdf.set_font('Arial', 'I', 12)
        pdf.cell(0, 10, 'Submitted in Support of Defendant\'s Motion to Vacate Plea', 0, 1, 'C')
        
        # Date
        pdf.cell(0, 10, f'{date.today().strftime("%B %d, %Y")}', 0, 1, 'C')
    
    # Save the PDF
    pdf.output("Exhibit_Cover_Pages.pdf")
    print("Exhibit cover pages PDF created successfully!")

# Run the function
create_exhibit_cover_pages()
