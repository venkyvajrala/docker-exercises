import click


@click.group()
def calc():
    """A simple command-line calculator."""
    pass


@calc.command()
@click.argument("numbers", nargs=-1, type=int)
def add(numbers):
    """Add numbers together."""
    total = sum(numbers)
    click.echo(f'Total is: {total}')


if __name__ == '__main__':
    calc()
