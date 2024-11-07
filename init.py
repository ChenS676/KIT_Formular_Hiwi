from pdfrw import PdfReader, PdfWriter, PageMerge

# Load the PDF template
template_path = '/mnt/data/KIT Formular Arbeitszeitdokumentation MiLoG.pdf'
output_path = '/mnt/data/Filled_KIT_Arbeitszeitdokumentation_MiLoG.pdf'

# Define example data to fill in
data = {
    'Monat / Jahr': '11 / 2023',
    'Name, Vorname des/r Beschäftigten': 'Max Mustermann',
    'Personalnummer': '123456',
    'GF': 'GF01',
    'UB': 'UB02',
    'OE': 'OE03',
    'Vertraglich vereinbarte Arbeitszeit': '40 Std',
    'Stundensatz': '15 €',

    # Fill sample activities and working hours
    'Tätigkeit Stichwort ProjektRow1': 'Projekt A',
    'ttmmjjRow1': '01.11.23',
    'hhmmRow1': '09:00',
    'hhmmRow1_2': '12:00',
    'hhmmRow1_3': '00:30',
    'hhmmRow1_4': '02:30',

    'Tätigkeit Stichwort ProjektRow2': 'Projekt B',
    'ttmmjjRow2': '02.11.23',
    'hhmmRow2': '10:00',
    'hhmmRow2_2': '13:00',
    'hhmmRow2_3': '00:30',
    'hhmmRow2_4': '02:30',

    # Fill summary data
    'Urlaub anteilig': '0',
    'Summe': '5:00',
    'monatliche SollArbeitszeit': '160 Std',
    'Übertrag vom Vormonat': '10:00',
    'Übertrag in den Folgemonat': '5:00',

    'Ich bestätige die Richtigkeit der Angaben:': 'Max Mustermann',
}

# Function to fill PDF fields
def fill_pdf(input_pdf, output_pdf, data_dict):
    template = PdfReader(input_pdf)
    for page in template.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                field = annotation.get('/T')
                if field:
                    field_name = field[1:-1]  # Remove parentheses
                    if field_name in data_dict:
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[field_name]))
                        )
                        annotation.update(pdfrw.PdfDict(Ff=1))  # Set as read-only

    PdfWriter(output_pdf, trailer=template).write()

# Fill the PDF and save it
fill_pdf(template_path, output_path, data)

print(f"Filled PDF saved to {output_path}")

