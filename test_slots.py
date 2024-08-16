from project import Player
from project import Slot
from project import Roulette

def test_Player():
    p1 = Player(5,"test")
    p2 = Player(10,"test2")
    assert str(p1) == (f"\nHello test, you have $5 available")
    assert str(p2) == (f"\nHello test2, you have $10 available")

def test_slotwin10(capsys):
    s1 = Slot()
    s1.testwin(10,"test")
    result = capsys.readouterr()
    assert result.out == ("\n\n['⭐']|['⭐']|['⭐']\n\nCongrats test, YOU JUST WON $50!!!!!\n")

def test_slotwin20(capsys): #should be the same as above but testing to ensure that the winnings = amount*5
    s2 = Slot()
    s2.testwin(25,"test")
    result = capsys.readouterr()
    assert result.out == ("\n\n['⭐']|['⭐']|['⭐']\n\nCongrats test, YOU JUST WON $125!!!!!\n")


def test_slotloss(capsys):
    s1 = Slot()
    s1.testloss(10,"test")
    result = capsys.readouterr()
    assert result.out == "\n\n['⭐']|['🍒']|['⭐']\n\nBetter luck next time!\n"

def test_roulette10(capsys):
    r1 = Roulette()
    r1.testevenwin(10, "test")
    result = capsys.readouterr()
    assert result.out == "\n\n🔴:6\nGood job test, you won 20!\n"

def test_roulette40(capsys):
    r1 = Roulette()
    r1.testevenwin(40, "test")
    result = capsys.readouterr()
    assert result.out == "\n\n🔴:6\nGood job test, you won 80!\n" #Tests that winnings are doubled
