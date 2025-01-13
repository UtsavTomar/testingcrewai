from my_project.crew import SimpleAgentCrew
from markdown_pdf import MarkdownPdf, Section

def run():

    inputs = {
        "text": "he concept of data in the context of computing has its roots in the work of Claude Shannon, an American mathematician known as the father of information theory. He ushered in binary digital concepts based on applying two-value Boolean logic to electronic circuits. Binary digit formats underlie the CPUs, semiconductor memories and disk drives, as well as many of the peripheral devices common in computing today. Early computer input for control and data took the form of punch cards, followed by magnetic tape and the hard disk."
    }
    # Kicking off the crew
    result = SimpleAgentCrew().crew().kickoff(inputs=inputs)

    # Save the summary result as a Markdown file
    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(result.raw))
    pdf.save("inputs_sales_pdf.pdf")
