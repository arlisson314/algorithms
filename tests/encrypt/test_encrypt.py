from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    """verifca se a funccão encrypt_message retorna erro quando
    o tipo de key e message são diferentes de int e str"""
    with pytest.raises(TypeError):
        encrypt_message(1, "string") or encrypt_message("string", "string")

    """verifica se retornar o valor esperado quando key é impar"""
    assert encrypt_message("xablau", 3) == "bax_ual"

    """verifica se retornar o valor esperado quando key é par"""
    assert encrypt_message("xablau", 2) == "ualb_ax"

    """verifica se retornar o valor esperado quando key não é
    um index válido"""
    assert encrypt_message("xablau", 6) == "ualbax"
