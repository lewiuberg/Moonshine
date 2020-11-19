from moonshine.misc import unpack_list


def word_search(df, *words):
    """
    [Word search in a DataFrame]

    Args:
        df ([DataFrame]): [Pandas DataFrame to search]
    """
    words = [word for word in words]
    sum_words: int = 0
    found_words: str = []
    # list_of_words: list = []

    if not words:
        return

    for word in words:
        col_count = 0
        sum_word = 0
        for column in df:
            if df[column].dtype == object or df[column].dtype == str:
                col_count += 1
                sum_word += df[column].str.contains(f"^{word}$").sum()
                if df[column].str.contains(f"^{word}$").any():
                    if word not in found_words:
                        found_words.append(word)
        sum_words += sum_word
    if len(found_words) == 0:
        found_words = words
    print("Columns of dtype str or object:", col_count)
    print(f"Instances of {unpack_list(found_words)} in the dataframe: {sum_words}")
