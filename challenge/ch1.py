def is_chinese_char(char: str) -> bool:
    """Checks whether `char` is a Chinese character."""
    return '\u4e00' <= char <= '\u9fff'

def is_chinese_str(string: str) -> bool:
    """Checks whether `string` is a Chinese string."""
    return all(is_chinese_char(char) for char in string)

def is_chinese_punctuation(char: str) -> bool:
    """Checks whether `char` is a Chinese punctuation."""
    return char in '，。？！；：、【】「」『』《》“”‘’（）…—'

def has_chinese_punctuation(string: str) -> bool:
    """Checks whether `string` has Chinese punctuation."""
    return any(is_chinese_punctuation(char) for char in string)

def remove_chinese_punctuation(string: str) -> str:
    """Removes Chinese punctuation from `string`."""
    return ''.join(char for char in string if not is_chinese_punctuation(char))

challenge1 = {
    'name':
    '第一章 急停仙人',
    'problems': [
        {
            'title': '第1题 没有停顿',
            'description': '请你构造一个问题，使模型的回答仅包含中文，字数在10字以上，且不包含任何标点符号。',
            'validator': lambda response, input: is_chinese_str(response) and len(response) > 10 and not has_chinese_punctuation(response)
        },
        {
            'title': '第2题 全是停顿',
            'description': '请你构造一个问题，使模型的回答仅包含中文标点符号，字数在5个以上。',
            'validator': lambda response, input: len(response) > 5 and all(is_chinese_punctuation(char) for char in response)
        },
        {
            'title': '第3题 精准停顿',
            'description': '请你构造一个问题，使模型的回答仅包含中文，字数为10字（可以有标点符号，标点符号不计入字数）。',
            'validator': lambda response, input: is_chinese_str(remove_chinese_punctuation(response)) and len(remove_chinese_punctuation(response)) == 10
        },
    ]
}
