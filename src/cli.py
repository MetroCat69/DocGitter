import click
from config import glitter_init


@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def init():
    glitter_init()