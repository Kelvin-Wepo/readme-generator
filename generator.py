from inquirer.shortcuts import PromptSession, prompt

questions = [
    {
        'type': 'input',
        'name': 'title',
        'message': 'What is the title of your project?'
    },
    {
        'type': 'input',
        'name': 'description',
        'message': 'Please enter a brief description of your project:'
    },
    {
        'type': 'input',
        'name': 'installation',
        'message': 'Please enter any installation instructions for your project:'
    },
    {
        'type': 'input',
        'name': 'usage',
        'message': 'Please enter any usage instructions for your project:'
    },
    {
        'type': 'input',
        'name': 'contributing',
        'message': 'Please enter any guidelines for contributing to your project:'
    },
    {
        'type': 'input',
        'name': 'tests',
        'message': 'Please enter any instructions for running tests on your project:'
    },
    {
        'type': 'list',
        'name': 'license',
        'message': 'Which license would you like to use for your project?',
        'choices': [
            'MIT',
            'Apache 2.0',
            'GPL 3.0',
            'BSD 3',
            'None'
        ]
    },
    {
        'type': 'input',
        'name': 'username',
        'message': 'Please enter your GitHub username:'
    },
    {
        'type': 'input',
        'name': 'email',
        'message': 'Please enter your email address:'
    }
]

session = PromptSession()
answers = session.prompt(questions)

print(answers)
