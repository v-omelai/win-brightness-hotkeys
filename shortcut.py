import click
import winshell


@click.command()
@click.option('--path', required=True, help='Shortcut path (*.lnk)')
@click.option('--target', required=True, help='Shortcut target (*.py, *.pyw, *.bat, *.exe)')
@click.option('--arguments', default='', help='Shortcut arguments')
def cli(path: str, target: str, arguments: str):
    """
    For more reference see:

    Windows Shell: https://winshell.readthedocs.io/en/latest/shortcuts.html

    CLI: https://click.palletsprojects.com/en/7.x/options/
    """
    winshell.CreateShortcut(Path=path, Target=target, Arguments=arguments)


if __name__ == '__main__':
    cli()
