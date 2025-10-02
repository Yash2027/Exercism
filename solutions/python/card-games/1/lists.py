def get_rounds(number):
    """Return current and next two round numbers as list"""
    rounds = []
    for i in range(3):   # current + next two
        rounds.append(number + i)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of rounds"""
    result = []
    # add all from rounds_1
    for r in rounds_1:
        result.append(r)
    # add all from rounds_2
    for r in rounds_2:
        result.append(r)
    return result


def list_contains_round(rounds, number):
    """Check if a round number exists in list"""
    for r in rounds:
        if r == number:
            return True
    return False


def card_average(hand):
    """Return average of hand values"""
    total = 0
    count = 0
    for card in hand:
        total += card
        count += 1
    return total / count


def approx_average_is_average(hand):
    """Check if average equals first+last/2 OR middle"""
    true_avg = card_average(hand)

    # average of first and last
    first_last_avg = (hand[0] + hand[-1]) / 2

    # middle card
    mid_index = len(hand) // 2
    middle_val = hand[mid_index]

    return (true_avg == first_last_avg) or (true_avg == middle_val)


def average_even_is_average_odd(hand):
    """Check if avg of even-indexed == avg of odd-indexed"""
    even_total, even_count = 0, 0
    odd_total, odd_count = 0, 0

    for i in range(len(hand)):
        if i % 2 == 0:  # even index
            even_total += hand[i]
            even_count += 1
        else:
            odd_total += hand[i]
            odd_count += 1

    even_avg = even_total / even_count
    odd_avg = odd_total / odd_count

    return even_avg == odd_avg


def maybe_double_last(hand):
    """Double last card if it is Jack (11)"""
    if len(hand) > 0 and hand[-1] == 11:
        # make a copy so we don't mutate original accidentally
        new_hand = []
        for i in range(len(hand)):
            if i == len(hand) - 1:
                new_hand.append(hand[i] * 2)
            else:
                new_hand.append(hand[i])
        return new_hand
    else:
        return hand
