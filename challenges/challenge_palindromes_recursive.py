"""O nível de complexidade desse código é O(n), onde n é o comprimento da
palavra a ser verificada. Isso porque a função é recursiva e realiza a
verificação comparando o primeiro caractere com o último, o segundo caractere
com o penúltimo, e assim por diante, até que os índices de início e fim se
encontrem ou não sejam iguais. Em cada iteração, o comprimento da string a
ser verificada é dividido aproximadamente pela metade, o que significa que
o número de comparações necessárias é proporcional ao tamanho da string."""


def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False
    if low_index >= high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
