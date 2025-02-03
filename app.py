from flask import Flask, Response, request
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import io

app = Flask(__name__)

def generate_table():
    # Create a StringIO stream to capture the Console's output.
    output = io.StringIO()
    # Create a Console that forces terminal output with truecolor (for proper color support)
    console = Console(file=output, force_terminal=True, color_system="truecolor", record=True)
    
    # Use Rich's markup for colors directly in the table title and content.
    table = Table(title="[cyan]My Projects[/cyan]", show_lines=True)
    table.add_column("[bold white]Name[/bold white]")
    table.add_column("[bold white]Description[/bold white]")
    
    table.add_row(
        "[green]P2P File Sync[/green]",
        "[blue]Binary XOR-based sync system[/blue]"
    )
    table.add_row(
        "[green]Blockchain KYC[/green]",
        "[blue]Hybrid Hashgraph & Blockchain[/blue]"
    )
    table.add_row(
        "[green]Rover AI[/green]",
        "[blue]Autonomous navigation[/blue]"
    )
    
    # Wrap the table in a Panel (using plain text for the panel title)
    panel = Panel(table, title="wadups", expand=True)
    console.print(panel)
    
    # Export the rendered output as HTML
    return output.getvalue()

@app.route("/")
def home():
    user_agent = request.headers.get("User-Agent", "")
    print(user_agent)
    output = generate_table()
    # Return the output as plain text so a terminal client (like curl) interprets it.
    return Response(output, content_type="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
