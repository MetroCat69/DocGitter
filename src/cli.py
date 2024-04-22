import click
import os
from config import glitter_init
from glitter_project import create_new_project_from_remote_url,delete_project_and_remove_config,list_created_projects,add_and_update_files,move_current_project

@click.group()
def cli():
    pass

@cli.command()
def init():
    glitter_init()

@cli.command()
@click.argument('remote_url')
def create_project(remote_url):
    click.echo("Creating project from remote URL: {}".format(remote_url))
    create_new_project_from_remote_url(remote_url)

@cli.command()
@click.argument('project_name',type=click.STRING)
def delete_project(project_name):
    click.echo("Deleting project : {}".format(project_name))
    delete_project_and_remove_config(project_name)


@cli.command()
def list_projects():
    current_project,projects = list_created_projects()
    if not (current_project ==None and projects==None):
        click.echo(f"Current project: {current_project} \n projects : {projects}")


@cli.command()
@click.argument('input_path')
def add(input_path):
    add_and_update_files(input_path)


@cli.command()
@click.argument('project_name')
def change_current_project(project_name):
    move_current_project(project_name)

if __name__ == '__main__':
    cli()