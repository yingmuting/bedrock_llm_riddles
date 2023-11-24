challenge2 = {
    'name':
    '第二章 万物理论',
    'problems': [
        {
            'title': '第1题 认识数字',
            'description': '请你构造一个问题，问题中不能包括阿拉伯数字，使模型的回答中包含0-9这10个阿拉伯数字',
            'validator': lambda response, input: any(str(i) in response for i in range(10)) and all(str(i) not in input for i in range(10))
        },
        {
            'title': '第2题 基本运算',
            'description': '请你构造一个问题，问题中不能包括“3.14”和“6.28”，使模型的回答中包含“6.28”',
            'validator': lambda response, input: '6.28' in response and '3.14' not in input and '6.28' not in input
        },
        {
            'title': '第3题 大就是好',
            'description': '请你构造一个问题，问题中不能包括阿拉伯数字，使模型的回答中包含“10000000000”',
            'validator': lambda response, input: '10000000000' in response and all(str(i) not in input for i in range(10))
        }
    ]
}
