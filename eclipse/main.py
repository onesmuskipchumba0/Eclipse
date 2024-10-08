#Import all tools for styling
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table
from rich.syntax import Syntax
from rich.prompt import Prompt
import sys
import random
import time

#initialize the console function
console = Console()
styles = ['bold','italic','underline','dim','blink','reverse','strikethrough','reset']
n = [2,1]
class Styled:
    def __init__(self, text, style,color) -> None:
        self.text = text
        self.style = style
        self.color = color
    #info
    def info():
        text = """[bright][green]
Welcome to Eclipse by onesmus bett co. \nEclipe is an opensource module developed for easy console manipulation and decoration.[/bright][green]
\n[bold]Usage[/bold]:\n[green]There are six funtions as of version  0.0.10:
[cyan]
\nStyled.info()
\nStyled.progress():for a progress bar.
\t-[bold]Params:[/bold]
\ttext,
\tcolor,
\tfont:['bold','italic','underline','dim','blink','reverse','strikethrough','reset'],
\ttime_out:default=0.1,
\ttotal:default=100,
\tadvance:default=1
\nStyled.table():creating tables
\t-[bold]Params:[/bold]
\ttitle,
\trows=n-d array
\tcols:1-d array of strings of column names
\tcolor
\tfont:['bold','italic','underline','dim','blink','reverse','strikethrough','reset']
\nStyled.Box():create a panel
\t-[bold]Params:[/bold]
\ttext,
\tcolor,
\tfont:['bold','italic','underline','dim','blink','reverse','strikethrough','reset']
\nStyle.inputf()
\t-[bold]Params:[/bold]
\ttext,
\tcolor,
\tisPassWord:false
\nStyle.printf()
\t-[bold]Params:[/bold]
\ttext,
\tcolor,
\tfont:['bold','italic','underline','dim','blink','reverse','strikethrough','reset']
\nStyle.ascii(text,fonts,color): create ascii art
\t-[bold]Params:[/bold]
\ttext,
\tfont:['r','kb','b','rt','st','sl','3d','4m','5l']
\tcolor,
[/cyan]
\nThank you for downloading this module. Happy coding :)
[/green]
                
        """
        console.print(text)
    #Progress bars
    def progress(text='Loading',color='green',font='bold',time_out=0.1,total=100,advance=1):
        with Progress() as progress:
            task = progress.add_task(f"[{color}]{text}[/{color}]",total=total)
            for i in range(total):
                time.sleep(time_out)
                progress.update(task,advance=advance)
            console.print(task)

    #tables
    def table(
            title='Table name',
            rows=[['item1','1'],['item 2','2']],
            cols=['column 1','column 2'],
            color='white',
            font='bold'
            ):
        table = Table(title=title)
        #Add columns
        for col in cols:
            table.add_column(f"[{font}]{col}[/{font}]",style=color)
        for row in rows:
            if len(row) == len(cols):
                #to add rows it needs same number of argments as len of cols
                table.add_row(*row)
        console.print(table)
                

    #boxes
    def Box(text='Sample Box',color='green',font='bold'):
        panel = Panel(f"[{font}]{text}[/{font}]",style=color)
        console.print(panel)
    #Prompts
    def inputf(text='You did not ask a question. Set text to question',color='white',isPassWord=False):
        #take user input
        n = Prompt.ask(f"[{color}]{text}[/{color}]",password=isPassWord)
        return n
    #return console output
    def printf(text='Sample output',font='bold',color='white'):
        #select from styles
        console.print(f"[{color}]{text}[/{color}]",style=font)

    #return ascii-art text
    def ascii(text='',font = 'r',color='white'):
        if text != '':
            # a dictionary for mapping fonts
            fonts = {
                'r':'rounded',
                'kb':'keyboard',
                'b':'banner',
                'st':'stellar',
                'sl':'slant',
                '3d':'3d-ascii',
                '4m':'4max',
                '5l':'5lineoblique',

            }
        
        
            #check for font typed in function
            if font in fonts.keys():
                ascii_art = pyfiglet.figlet_format(text,font=fonts[f'{font}'])
                return f"[{color}]{ascii_art}[/{color}]"
            else:
                return f"[red]Invalid font[/red]: '[bold]{font}[/bold]'\nAvailable fonts: {list(fonts.keys())}"
        else:
            return f"[red]Text parameter is missing: positional argument required in Style.ascii()[/red]\nRequired:Styled.ascii('text')"
if len(sys.argv) > 1:
    if '--info' in sys.argv[1]:
        Styled.info()
    elif '--ascii' in sys.argv[1]:
        console.print(Styled.ascii("Eclipse",'3d','purple'))

if __name__ == '__main__':
    pass