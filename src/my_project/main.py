from my_project.crew import SimpleAgentCrew

def run():

    inputs = {
        "text": "text"
    }
    # Kicking off the crew
    result = SimpleAgentCrew().crew().kickoff(inputs=inputs)

    # Save the summary result as a Markdown file
    with open("summary.md", "w") as f:
        f.write(result.raw)
