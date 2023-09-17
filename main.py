import pdfplumber


def extract_pdf(pdf_path):
    """
    Extract text from a PDF file using pdfplumber library.

    Args:
        pdf_path (str): The path to the PDF file to be extracted.

    Returns:
        str: The extracted text from the PDF file.

    Raises:
        Exception: If an error occurs during PDF extraction, it's caught and a message is printed.

    Usage:
        pdf_path = 'files/file.pdf'
        extracted_text = extract_pdf(pdf_path)
    """
    try:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Initialize an empty string to store the text
            text = ""

            # Iterate through each page and extract text
            for page in pdf.pages:
                text += page.extract_text()

            return text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def save_txt(text, output_file):
    """
    Save text to a text file.

    Args:
        text (str): The text to be saved.
        output_file (str): The path to the output text file.

    Raises:
        Exception: If an error occurs during file saving, it's caught and a message is printed.

    Usage:
        output_file = 'extracts/text.txt'
        save_txt(extracted_text, output_file)
    """
    try:
        # Open the output file in write mode
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")


# Example usage
pdf_path = 'files/file.pdf'
output_file = 'extracts/text.txt'

extracted_text = extract_pdf(pdf_path)

if extracted_text:
    save_txt(extracted_text, output_file)
