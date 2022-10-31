{
    'name': 'Project Task Stage Dependency',
    'version': '16.0.1.0',
    'website': 'https://github.com/ruiznorlan/project',
    'category': 'Services/Project',
    'sequence': 45,
    'summary': 'This module allows to restrict the next/previous stage of a task, in this way a workflow can be carried out correctly without skipping stages.',
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
    'author': 'Norlan Ruiz',
}