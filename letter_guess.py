import re
from collections import defaultdict


def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound', ...]):
    """Returns a letter from the alphabet.
    Input parameters:
				pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    if '_' not in pattern:
        raise Exception('Have guessed all letters correctly.')

    letter_map = defaultdict(int)
    used_letters_set = set(used_letters)
    for word in word_list:
        # 是否正则匹配
        match_rst = re.fullmatch(pattern.replace('_', '(.)'), word)
        if not match_rst:
            continue
        other_letters = set(match_rst.groups())
        # 单词包含的其他字母已被猜测但未显示在结果中 则跳过
        if other_letters & used_letters_set:
            continue

        for letter in other_letters:
            letter_map[letter] += 1

    if not letter_map:
        raise Exception('No valid letter.')

    letter_item = max([(k, v) for k, v in letter_map.items()], key=lambda x: x[1])
    return letter_item[0]


def test_function_should_return_something():
    pattern = "__e"
    used_letters = list("e")
    word_list = ['age']
    assert guess_next_letter(pattern, used_letters, word_list) is not None


def test_function_should_return_match_world_letter():
    pattern = "__e"
    used_letters = list("ce")
    word_list = ['aae', 'we', 'ssse', 'bee', 'cce', 'bce']
    assert guess_next_letter(pattern, used_letters, word_list) == 'a'


def test_function_should_return_most_probable_letter():
    pattern = "__e"
    used_letters = list("e")
    word_list = ['aae', 'bbe', 'abe', 'cce', 'bce']
    assert guess_next_letter(pattern, used_letters, word_list) == 'b'
