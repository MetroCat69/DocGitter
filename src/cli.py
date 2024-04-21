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
@click.option('--glitter_project_path', default=os.path.join(os.path.expanduser('~'), '.glitter'), help='Path where Glitter projects will be stored')
def create_project(remote_url, glitter_project_path):
    click.echo("Creating project from remote URL: {}".format(remote_url))
    create_new_project_from_remote_url(remote_url, glitter_project_path)

@cli.command()
@click.argument('project_name',type=click.STRING)
@click.option('--glitter_project_path', default=os.path.join(os.path.expanduser('~'), '.glitter'), help='Path where Glitter projects will be stored')
def delete_project(project_name, glitter_project_path):
    click.echo("Deleting project : {}".format(project_name))
    delete_project_and_remove_config(project_name, glitter_project_path)


@cli.command()
@click.option('--glitter_project_path', default=os.path.join(os.path.expanduser('~'), '.glitter'), help='Path where Glitter projects will be stored')
def list_projects(glitter_project_path):
    current_project,projects = list_created_projects(glitter_project_path)
    click.echo(f"Current project: {current_project} \n projects : {projects}")


@cli.command()
@click.argument('input_path')
@click.option('--glitter_project_path', default=os.path.join(os.path.expanduser('~'), '.glitter'), help='Path where Glitter projects will be stored')
def add(input_path,glitter_project_path):
    add_and_update_files(input_path,glitter_project_path)


@cli.command()
@click.argument('project_name')
@click.option('--glitter_project_path', default=os.path.join(os.path.expanduser('~'), '.glitter'), help='Path where Glitter projects will be stored')
def change_current_project(project_name,glitter_project_path):
    move_current_project(project_name,glitter_project_path)

if __name__ == '__main__':
    cli()