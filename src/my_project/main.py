from my_project.crew import SimpleAgentCrew

def run():

    inputs = {
        "text": """Data Science is an interdisciplinary field that combines scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data. It involves the use of mathematics, statistics, specialized programming, advanced analytics, artificial intelligence (AI), and machine learning to uncover actionable insights hidden in an organization’s data"""
    }
    # Kicking off the crew
    result = SimpleAgentCrew().crew().kickoff(inputs=inputs)

    # Save the summary result as a Markdown file
    with open("summary.md", "w") as f:
        f.write(result.raw)
