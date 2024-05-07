# DocGitter: Git for Office Files

DocGitter is a command-line tool that allows you to version control your office files (such as Word documents, Excel spreadsheets, and PowerPoint presentations) using Git. It provides an easy way to track changes, collaborate with others, and maintain a backup of your important files.

## Getting Started

note that all changes are commited to main and that you need git working in the location you are running the project

1. **Initialize DocGitter**: Run `glitter init` to set up the necessary configuration.

2. **Create a New Project**: Run `glitter create_project <remote_url>` to create a new project from a remote Git repository URL. Make sure you have permission to push and pull from the repository.

3. **Add Files**: Run `glitter add <file_path>` to add and convert office files to a format that can be tracked by Git. The converted files will be added to the current project.

4. **List Projects**: Run `glitter list_projects` to see the list of available projects and the current active project.

5. **Change Current Project**: Run `glitter change_current_project <project_name>` to switch to a different project.

6. **Delete Project**: Run `glitter delete_project <project_name>` to remove a project from DocGitter.

## Example Usage

```bash
# Initialize DocGitter
glitter init

# Create a new project from a remote URL
glitter create_project https://github.com/user/repo.git

# Add office files to the current project
glitter add /path/to/documents

# List available projects
glitter list_projects

# Switch to a different project
glitter change_current_project another-project

# Delete a project
glitter delete_project old-project
```
