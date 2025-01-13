from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class SimpleAgentCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def simple_agnet(self) -> Agent:
        return Agent(
            config=self.agents_config["simple_agent"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )
    
    @task
    def process_text_task(self) -> Task:
        return Task(
            config=self.tasks_config["process_text_task"],
            agent=self.simple_agnet(),
            output_file="ticket_summary.md"
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Ticket Analysis Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Tasks will run sequentially
            verbose=True,
        )
    