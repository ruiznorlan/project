{
    'name': 'Project Task Stage Dependency',
    'version': '16.0.1.0',
    'website': 'https://github.com/ruiznorlan/project',
    'category': 'Services/Project',
    'sequence': 45,
    'summary': 'This module allows to restrict the next stage of a task',
    'depends': [
        'base',
        'project'
    ],
    'data': [
        'views/project_task_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}