import click
import subprocess

@click.command()
def begins():
    subprocess.run(["bench", "migrate"])
    subprocess.run(["bench", "clear-cache"])
    subprocess.run(["bench", "build"])

commands = [begins]