# Custom exception for project already existing
class ProjectExistsError(Exception):
    def __init__(self,path):
        super().__init__(f"Directory with project name already exists at path: {path}")