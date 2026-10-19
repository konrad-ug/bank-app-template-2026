from src.account import Account


def test_account_stores_first_name_last_name_and_pesel():
    account = Account("Jan", "Kowalski", "90010112345")

    assert account.first_name == "Jan"
    assert account.last_name == "Kowalski"
    assert account.pesel == "90010112345"
