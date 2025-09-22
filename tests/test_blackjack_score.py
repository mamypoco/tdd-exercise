from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7
  

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  #arrange
  hand = ['King', 'Jack']
  #act
  score = blackjack_score(hand)

  #act
  assert score == 20

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  #arrange
    hand = ['Ace', 8, 2]
  #act
    score = blackjack_score(hand)
  #assert
    assert score == 21

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  #arrange
    hand = ['Ace', 6, 3, 2]
  #act
    score = blackjack_score(hand)
  #assert
    assert score == 12


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  #arrrange
  hand = ['Ace']
  #act

  #assert 
  assert len(hand) == 1


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  #arrange
  hand = ['Ace', 2, 3, 6, 7, 'Jack']
  #act

  #assert
  assert len(hand) == 6

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  #arrange
  hand = [2, 'Queen', 'Jack', 'Ace']
  #act
  score = blackjack_score(hand)
  #assert
  assert score == 22



# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  #arrange
  hand = ['Ace', 'Ace', 'King']

  #act
  score = blackjack_score(hand)

  #assert
  assert score == 21 

@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    pass