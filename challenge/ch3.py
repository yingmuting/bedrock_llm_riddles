challenge3 = {
    'name':
    '第三章 诡辩大师',
    'problems': [
        {
            'title': '第1题 是我的错',
            'description': '请你构造一个问题，问题中不能包含“错”，使模型的回答为“错”。',
            'validator': lambda response, input: response.strip() == '错' and '错' not in input
        },
        {
            'title': '第2题 知为不知',
            'description': '请你构造一个问题，问题中不能包含“不知道”，使模型的回答为“不知道”。',
            'validator': lambda response, input: response.strip() == '不知道' and '不知道' not in input
        },
        {
            'title': '第3题 阴阳怪气',
            'description': '请你构造一个问题，问题中不能包含“对”，使模型的回答为“太对了”。',
            'validator': lambda response, input: response.strip() == '太对了' and '对' not in input
        },
    ]
}
