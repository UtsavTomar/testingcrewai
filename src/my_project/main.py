from my_project.crew import SimpleAgentCrew
from markdown_pdf import MarkdownPdf, Section

def run():

    inputs = {
        "text": "<your_text>"
    }
    # Kicking off the crew
    result = SimpleAgentCrew().crew().kickoff(inputs=inputs)

    # Save the summary result as a Markdown file
    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(result.raw))
    pdf.save("inputs_sales_pdf.pdf")
